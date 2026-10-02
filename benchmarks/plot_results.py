"""Render vendor-native observations. Requires matplotlib and numpy; no API calls."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT/'benchmarks/2026-10-02/results.json').read_text(encoding='utf-8'))
variants = ['source', 'rewrite', 'v12', 'v13', 'v14']
cases = ['en-library', 'ko-library', 'en-cache', 'ko-cache']
services = ['GPTZero', 'QuillBot', 'Sapling', 'ZeroGPT']
units = ['Whole-document AI class probability (%)',
         'Words likely generated/refined by AI (%)',
         'Whole-text AI-generation estimate (%)',
         'Vendor AI GPT score (%)']
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':10, 'svg.fonttype':'none'})
fig, axes = plt.subplots(2, 2, figsize=(12, 7.2))
cmap = LinearSegmentedColormap.from_list('observed', ['#f2f4f3','#afc8c1','#517c72'])
cmap.set_bad('#eeeeee')
for ax, service, unit in zip(axes.flat, services, units):
    scores=np.full((4,5),np.nan)
    for r in data['records']:
        if r['service']==service:
            scores[cases.index(r['case']),variants.index(r['variant'])]=r['displayed_ai_percent']
    ax.imshow(scores, cmap=cmap, vmin=0, vmax=100, aspect='auto')
    for row in range(4):
        for col in range(5):
            value=scores[row,col]
            ax.text(col,row,'N/A' if np.isnan(value) else f'{value:g}',
                    ha='center',va='center',color='#666666' if np.isnan(value) else ('white' if value>=75 else '#202725'))
    ax.set_xticks(range(5),['Source','v1.1','v1.2','v1.3','v1.4'])
    ax.set_yticks(range(4),['EN library','KO library','EN cache','KO cache'])
    ax.set_title(service+'\n'+unit,loc='left',fontsize=11,pad=12)
    ax.tick_params(length=0,pad=8)
    for spine in ax.spines.values():spine.set_visible(False)
fig.suptitle('Commercial observations on four synthetic documents',x=.03,ha='left',fontsize=17,y=.98)
fig.text(.03,.923,'Compare within a service. Native metrics differ; no pooled accuracy or pass rate.',fontsize=10,color='#4f5653')
fig.text(.03,.032,'N/A = not tested or unavailable, never zero. All sources and rewrites were AI-produced.\nAdaptive development sample, 2026-10-02; no human-authored control. See REPORT.md for settings and limits.',fontsize=9,color='#4f5653')
fig.subplots_adjust(left=.115,right=.98,top=.82,bottom=.16,wspace=.36,hspace=.48)
for ext in ['png','svg']:
    fig.savefig(ROOT/f'docs/assets/detector-observations.{ext}',dpi=180,facecolor='white')

