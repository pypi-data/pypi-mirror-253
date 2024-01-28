from ._get_sparkline import get_sparkline_import
DEFAULT_TABLE_CLASSES = ['table', 'table-striped', 'table-bordered', 'table-hover', 'table-condensed']

SIMPLE_PACKAGES = {
    'bootstrap': """<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">""",
    'd3': """<script src="https://d3js.org/d3.v6.min.js"></script>""",
}

COMPLEX_PACKAGES = {
    'sparkline': get_sparkline_import
}

def to_table(df, classes=DEFAULT_TABLE_CLASSES):
    classes = ' '.join(classes)
    return df.style.set_table_attributes(f'class="{classes}"').to_html()

def get_packs(packages):
    imports = []
    for package in packages:
        if package in SIMPLE_PACKAGES:
            imports.append(SIMPLE_PACKAGES[package])
        elif package in COMPLEX_PACKAGES:
            imports.append( COMPLEX_PACKAGES[package]() )
    return '\n'.join(imports)
    

