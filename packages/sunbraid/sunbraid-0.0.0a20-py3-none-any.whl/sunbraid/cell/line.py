import uuid
import seaborn as sns
import numpy as np
import seaborn as sns
from .backend import make_sns_plotter

DASH_ORDER = []
def get_colors(palette, N):
    return [f'rgb{tuple(c)}' for c in (np.array(sns.color_palette(palette, N))*255).astype(int)]


def prep_group(df, x, y, color, line_dash):
    result = df.sort_values(x).copy()
    return (
        result
        .assign(x = lambda d: d[x])
        .assign(y = lambda d: d[x])
    )

def prep(df, row, x, y, color, line_dash):
    (
        df.groupby(row)
    )



def make_lineplot(data, height=50):
    random_id = str(uuid.uuid4()).replace('-', '')
    return f"""
    <div class="magnifiable">
        <div id="rdivRUID{random_id}"></div>
    </div>
    <script>
        const dataRUID{random_id} = {data};
        createLinePlot(dataRUID{random_id},  'rdivRUID{random_id}', {height});
    </script>
"""

def lineplot(df, level, x, y, color=None, line_dash=None, backend='seaborn', name='lineplot', 
             post_fig = None, **kwargs):
    if backend == 'seaborn':
        plotter = make_sns_plotter(sns.lineplot, post_fig=post_fig, **kwargs)
        return (
            df.groupby(level).apply(lambda d: plotter(d, x=x, y=y, hue=color, style=line_dash)).rename(name).reset_index()
        )