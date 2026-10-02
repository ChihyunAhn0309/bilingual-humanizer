"""Plot native vendor scores; no cross-vendor aggregation or accuracy claim."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

base=Path(__file__).resolve().parent
old=json.loads((base/'2026-10-02/results.json').read_text('utf-8'))['records']
new=json.loads((base/'2026-10-02-v15/results.json').read_text('utf-8'))['records']
idx={r['id']:r for r in new}
cases=['en-library','en-cache','ko-library','ko-cache']
labels=['English library','English cache','Korean library','Korean cache']
providers=[('GPTZero','AI class probability (%)'),('QuillBot','AI-word share (%)'),('Sapling','AI probability (%)'),('ZeroGPT','AI GPT (%)')]
fig,axs=plt.subplots(2,2,figsize=(11.8,7.6))
for ax,(vendor,metric) in zip(axs.flat,providers):
    ax.set_title(vendor,loc='left',fontweight='bold',fontsize=13,pad=10)
    for y,case in enumerate(cases):
        prior=next((r['displayed_ai_percent'] for r in old if r['service']==vendor and r['case']==case and r['variant']=='v14'),None)
        suffix='-v15-reviewed' if case=='en-cache' else '-v15'
        current=idx.get(vendor.lower()+'-'+case+suffix)
        if prior is None or current is None:
            ax.text(50,y,'not tested / N/A',color='#818a99',ha='center',va='center',fontsize=9)
            continue
        now=current['score']
        ax.plot([prior,now],[y-.08,y+.08],color='#a5adb8',lw=1.5,zorder=2)
        ax.scatter([prior],[y-.08],c='#326da8',s=40,zorder=3)
        ax.scatter([now],[y+.08],c='#d2752a',s=40,zorder=3)
        ax.text(107,y,f'{prior:g} → {now:g}',fontsize=9,va='center',color='#273849')
    ax.set_yticks(range(4),labels,fontsize=9)
    ax.set_ylim(3.55,-.6);ax.set_xlim(-3,139)
    ax.set_xticks([0,25,50,75,100]);ax.set_xlabel(metric,fontsize=10)
    ax.grid(axis='x',alpha=.18);ax.set_axisbelow(True)
    for side in ['top','right','left']:ax.spines[side].set_visible(False)
    ax.tick_params(axis='y',length=0)
fig.suptitle('Observed scores on four reused development texts',x=.03,ha='left',fontsize=17,fontweight='bold')
legend=[Line2D([0],[0],marker='o',color='w',markerfacecolor='#326da8',markersize=7,label='v1.4'),Line2D([0],[0],marker='o',color='w',markerfacecolor='#d2752a',markersize=7,label='v1.5 final candidate')]
fig.legend(handles=legend,loc='upper left',bbox_to_anchor=(.027,.951),ncol=2,frameon=False)
fig.text(.03,.03,'Native vendor metrics; lower score is not proof of human authorship. No cross-vendor average.\nEnglish cache uses the final fidelity-repaired candidate. Fresh-text comparisons and all intermediate results are in the report.',fontsize=9,color='#526171',linespacing=1.5)
fig.tight_layout(rect=[.015,.095,.99,.90],h_pad=2.1,w_pad=2.4)
out=base.parent/'docs/assets';out.mkdir(exist_ok=True,parents=True)
fig.savefig(out/'detector-v15-comparison.png',dpi=200,facecolor='white')
fig.savefig(out/'detector-v15-comparison.svg',facecolor='white')
print('Saved PNG and SVG comparison')
