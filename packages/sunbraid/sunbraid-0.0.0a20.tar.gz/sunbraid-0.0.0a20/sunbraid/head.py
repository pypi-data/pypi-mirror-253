from sunbraid import __version__ as version
import os
from glob import glob

dir_path = '/'.join(os.path.abspath(__file__).split('/')[:-1])

css_files = glob(f"{dir_path}/static/css/*", recursive=True)
functions_files = glob(f"{dir_path}/static/functions/*", recursive=True)
scripts_files = glob(f"{dir_path}/static/scripts/*", recursive=True)


if len(version) > 12:
    path_maker = lambda s: s
else:
    path_maker = lambda s: f"https://cdn.jsdelivr.net/gh/estevaouyra/sunbraid@{version}/sunbraid{s.replace(dir_path, '')}"

css_imports = '\n\t'.join([f"""<link href="{path_maker(file)}" rel="stylesheet">""" for file in css_files])
function_defs = '\n\t'.join([f"""<script src="{path_maker(file)}"></script>""" for file in functions_files])
scripts = '\n\t'.join([f"""<script src="{path_maker(file)}"></script>""" for file in scripts_files])


def render_page(html, mode='return', path=None):
    """
    Params
    ------
    html: str
        HTML body to be rendered
    mode: str
        One of ['return', 'save', 'show']
    path: str
        Path to save the HTML file. Only used when mode='save'
    
    """
    full_page = f"""
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <script src="https://d3js.org/d3.v6.min.js"></script>
        {css_imports}
        {function_defs}
    </head>
    <body style="margin:100;padding:0">
        {html}
        {scripts}
    </body>
    """
    assert mode in ['return', 'save', 'show'], "mode must be one of ['return', 'save', 'show']"
    if mode=='return':
        return full_page
    elif mode=='save':
        try: # if path is not None
            with open(path, 'w') as f:
                f.write(full_page)
        except TypeError:
            raise TypeError("When mode='save', path must be a string")
    elif mode=='show':
        print("displaying")
        from IPython.display import display, HTML
        display(HTML(full_page))
        return None


def get_imports():
    return f"""
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
            <script src="https://d3js.org/d3.v6.min.js"></script>
            <script src="{base_path}/static/functions/line.js"></script>
            <link href="{base_path}/static/css/containers.css" rel="stylesheet">
            """

def make_head():
    all_imports = get_imports()
    return '<head>' + all_imports + '</head>'

def make_body(html):
    return (
        '<body>' + 
        html + 
        f'<script src="https://cdn.jsdelivr.net/gh/estevaouyra/sunbraid@{version}/static/functions/containers.js"></script>'+
        '</body>'
    )
