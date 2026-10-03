"""Bounded local inference experiment on synthetic sources; no external scoring API."""
from pathlib import Path
import os,sys,json,time,hashlib

ROOT=Path(__file__).resolve().parent
MODEL_DIR=ROOT/'local-model'
os.environ['HF_HOME']=str(MODEL_DIR/'cache')
os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN']='1'
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING']='1'
os.environ['HF_HUB_DISABLE_PROGRESS_BARS']='1'
os.environ['HF_HUB_DISABLE_XET']='1'
os.environ['TOKENIZERS_PARALLELISM']='false'
sys.path.insert(0,str(ROOT/'hip-deps'))
manifest=json.loads((MODEL_DIR/'model-manifest.json').read_text('utf-8'))
def write(name,value):(MODEL_DIR/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n','utf-8')
if sys.argv[1]=='download':
    from huggingface_hub import snapshot_download
    for entry,directory in zip(manifest,['base','adapter']):
        print('Downloading',entry['repo'],entry['sha'],flush=True)
        snapshot_download(entry['repo'],revision=entry['sha'],local_dir=MODEL_DIR/directory,
                          token=False,allow_patterns=['*.json','*.safetensors','merges.txt','vocab.json','LICENSE','README.md'])
        print('Downloaded',directory,flush=True)
    write('download-hashes.json',{str(p.relative_to(MODEL_DIR)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest()
          for d in ['base','adapter'] for p in (MODEL_DIR/d).rglob('*') if p.is_file() and '.cache' not in p.parts})
    print('All model files hashed.',flush=True)
elif sys.argv[1]=='run':
    import torch,transformers,peft
    from transformers import AutoTokenizer,AutoModelForCausalLM
    from peft import PeftModel
    torch.set_num_threads(4)
    torch.manual_seed(20261003)
    start=time.monotonic()
    tok=AutoTokenizer.from_pretrained(MODEL_DIR/'adapter',local_files_only=True,trust_remote_code=False)
    model=AutoModelForCausalLM.from_pretrained(MODEL_DIR/'base',local_files_only=True,trust_remote_code=False,
          dtype=torch.float32,low_cpu_mem_usage=True,attn_implementation='sdpa')
    model=PeftModel.from_pretrained(model,MODEL_DIR/'adapter',local_files_only=True)
    model.eval()
    print('Model loaded',round(time.monotonic()-start,2),'seconds',flush=True)
    metadata={'torch':torch.__version__,'transformers':transformers.__version__,'peft':peft.__version__,
              'device':'cpu','dtype':'float32','threads':4,'seed':20261003,'temperature':1.0,'top_p':0.95,
              'max_new_tokens':1200,'max_time_seconds_per_document':240,'trust_remote_code':False,
              'input_truncation':False,'rounds':1,'records':[]}
    for case in ['en-museum','ko-library']:
        source=(ROOT/'sources'/f'{case}.txt').read_text('utf-8').strip()
        # Match the adapter's documented plain-text source/target framing; no chat template.
        prompt='<source_text>\n'+source+'\n</source_text>\n\n<target_text>\n'
        encoded=tok(prompt,return_tensors='pt',truncation=False)
        input_tokens=encoded['input_ids'].shape[-1]
        if input_tokens>4096:raise ValueError('Unexpected input size; do not truncate')
        begin=time.monotonic()
        with torch.inference_mode():
            out=model.generate(**encoded,max_new_tokens=1200,max_time=240,do_sample=True,temperature=1.0,top_p=0.95,
                               pad_token_id=tok.pad_token_id or tok.eos_token_id)
        continuation=out[0,input_tokens:]
        raw=tok.decode(continuation,skip_special_tokens=True)
        clean=raw.split('</target_text>',1)[0].strip()
        (MODEL_DIR/f'{case}-raw.txt').write_text(raw,'utf-8')
        (MODEL_DIR/f'{case}.txt').write_text(clean+'\n','utf-8')
        rec={'case':case,'seconds':round(time.monotonic()-begin,2),'input_tokens':input_tokens,
             'new_tokens':len(continuation),'closing_tag_present':'</target_text>' in raw,
             'last_token_eos':int(continuation[-1])==tok.eos_token_id if len(continuation) else False,
             'source_sha256':hashlib.sha256((ROOT/'sources'/f'{case}.txt').read_bytes()).hexdigest(),
             'output_sha256':hashlib.sha256((MODEL_DIR/f'{case}.txt').read_bytes()).hexdigest()}
        metadata['records'].append(rec);write('inference-metadata.json',metadata)
        print(json.dumps(rec),flush=True)
    print('Inference complete; outputs require fidelity review before detector testing.',flush=True)
