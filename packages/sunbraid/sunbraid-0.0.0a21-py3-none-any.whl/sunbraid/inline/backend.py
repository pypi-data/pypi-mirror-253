import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64


def b64encode(fig):
    if type(fig) == plt.Axes:
        fig = fig.figure

    if type(fig) == plt.Figure:
        buf = io.BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
        buf.seek(0)
        b64_string = base64.b64encode(buf.read()).decode('utf-8')
    return f"data:image/png;base64,{b64_string}"

def embed_to_img(obj):
    if type(obj)!=str:
        img_src = b64encode(obj)
    else:
        img_src = obj

    return f'<img src="{img_src}" style="max-width:100%; max-height:100%;">'
        
def container(content, uid='', classes=''):
    div_start = ''
    if classes != '':
        div_start += f' class="{classes}"'
    if uid != '':
        div_start += f' id="{uid}"'
    return f"""<div{div_start}>
    {content}
    </div>
    """

def make_sns_plotter(f, post_fig=None, classes='incell'):
    def g(data, *args, **kwargs):
        fig, ax = plt.subplots()
        fig = f(data, *args, **kwargs, ax=ax)
        plt.sca(ax)
        fig = plt.gcf()
        if post_fig is not None:
            post_fig(data=data, fig=fig, ax=ax)
        plt.close(fig)
        return container(embed_to_img(fig), classes=classes)
    return g