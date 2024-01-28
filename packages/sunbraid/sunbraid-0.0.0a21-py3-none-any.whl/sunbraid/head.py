import os
from glob import glob
import pkg_resources
import pandas as pd
from .conf import to_table, get_packs

version = pkg_resources.get_distribution('sunbraid').version
dir_path = '/'.join(os.path.abspath(__file__).split('/')[:-1])

css_files = glob(f"{dir_path}/static/css/*", recursive=True)
functions_files = glob(f"{dir_path}/static/functions/*", recursive=True)
scripts_files = glob(f"{dir_path}/static/scripts/*", recursive=True)


def get_static(mode='full'):
    """
    Params
    ------
    mode: str
        One of ['full', 'cdn', 'local']
        If 'full', includes the full content of the files
        If 'cdn', includes a link to the CDN
        If 'local', includes a link to the local files
    """
    if mode == 'full':
        script = lambda s: f"<script>{open(s).read()}</script>"
        css_imports = '\n\t'.join([f"""<style>{open(file).read()}</style>""" for file in css_files])
        function_defs = '\n\t'.join([script(file) for file in functions_files])
        scripts = '\n\t'.join([script(file) for file in scripts_files])

    else:
        if mode == 'local':
            path_maker = lambda s: s
        else:
            path_maker = lambda s: f"https://cdn.jsdelivr.net/gh/estevaouyra/sunbraid@{version}/sunbraid{s.replace(dir_path, '')}"

        css_imports = '\n\t'.join([f"""<link href="{path_maker(file)}" rel="stylesheet">""" for file in css_files])
        function_defs = '\n\t'.join([f"""<script src="{path_maker(file)}"></script>""" for file in functions_files])
        scripts = '\n\t'.join([f"""<script src="{path_maker(file)}"></script>""" for file in scripts_files])

    return css_imports, function_defs, scripts

def render(html_or_df, mode='show', path=None, lib_mode='full', packages = ['bootstrap', 'd3']):
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
    if type(html_or_df) == pd.DataFrame:
        html = to_table(html_or_df)
    else:
        html = html_or_df

    imports = get_packs(packages)
    css_imports, function_defs, scripts = get_static(mode=lib_mode)

    html = html.replace('\n', '\n\t')    


    full_page = f"""
<head>
    {imports}
    {css_imports}
    {function_defs}
</head>
<body>

    <div style="margin:300;padding:0">
        <div style="max_width:100%">
        {html}
        </div>
    </div>
    {scripts}
</body>
    """
    #     
    #     <div style="max_width:100%">
    #     {html}
    #     </div>
    # </div>
    #     
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
