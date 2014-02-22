"""HTML to HTML DEFAULT Converter Style

Copies the html file and evaluates the python instructions.

"""

from lexor import init
from lexor.core.converter import NodeConverter
from lexor.core.parser import Parser

INFO = init(
    version=(0, 0, 1, 'final', 0),
    lang='html',
    to_lang='html',
    type='converter',
    description='Copy html file and evaluate python instructions.',
    url='http://jmlopez-rod.github.io/lexor-lang/html-converter-html-default',
    author='Manuel Lopez',
    author_email='jmlopez.rod@gmail.com',
    license='BSD License',
    path=__file__
)
DEFAULTS = {
    'error': 'on',
    'exec': 'on',
}


class PythonNC(NodeConverter):
    """Append a node with python instructions to a list. """

    def process(self, node):
        self.converter.python.append(node)


MAPPING = {
    '?python': PythonNC,
}
PARSER = Parser('html', 'default')


def init_converter(converter):
    """Initializes a list to hold references to python embeddings. """
    converter.python = list()


def convert(converter, _):
    """Evaluate the python embeddings. """
    err = True
    if converter.defaults['error'] in ['off', 'false']:
        err = False
    if converter.defaults['exec'] in ['on', 'true']:
        for num, node in enumerate(converter.python):
            converter.exec_python(node, num, PARSER, err)
