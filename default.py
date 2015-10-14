"""HTML to HTML DEFAULT Converter Style

Evaluates python instructions.

"""
from lexor import init

INFO = init(
    version=(0, 0, 2, 'final', 0),
    lang='html',
    to_lang='html',
    type='converter',
    description='Copy html file and evaluate python instructions.',
    git={
        'host': 'github',
        'user': 'jmlopez-rod',
        'repo': 'html-converter-html-default'
    },
    author={
        'name': 'Manuel Lopez',
        'email': 'jmlopez.rod@gmail.com'
    },
    docs='http://jmlopez-rod.github.io/'
         'lexor-lang/html-converter-html-default',
    license='BSD License',
    path=__file__
)
