# Constant variables
import re, os
from typing import Generator

PROJECT_APP_NAME = 'TextTools'
if 'PROJECT_APP_NAME' in os.environ and os.environ['PROJECT_APP_NAME']:
    PROJECT_APP_NAME = os.environ['PROJECT_APP_NAME']

# texttools
ANSI_ITERABLES = list|tuple|set|Generator|filter
ANSI_MOD_PERCENTAGE = 15
COLORS_RGB_DIFF_KEY = 'max'
RE_16COLOR_ESCAPE = re.compile( '([012]{1};[34]{1}[0-7]{1}){1}|([34]{1}[0-7]{1}){1}[;m]+' )
RE_CURSOR_CONTROL_ESCAPE = re.compile( '^\x1b\[(\?25[lh]{1}|[0-9]*[ABCDGJK]{1})+$' )
RE_RGB_ESCAPE = re.compile( '(38|48){1};2((;25[0-5]{1}){1}|(;2[0-4]{1}[0-9]{1}){1}|(;1?[0-9]{1,2}?){1}){3}[;m]+' )
RE_STYLE_ESCAPE = re.compile( '[\[;]{1}2?[13459]{1}[;m]{1}' )

# texttools.types
COMPARE_FUNCTIONS = ( '__eq__', '__ne__', '__gt__', '__ge__', '__lt__', '__le__' )
STRING_FUNCTIONS = ( '__str__', '__len__', '__bool__', '__add__', '__radd__' )

# texttools._ansi_html
HTML_SINGLE_CHAR_CODES = (( ' ', '&nbsp;' ),
                          ( '\n', '<br>' ),
                          ( '\t', '&#09;' ),
                          ( '&', '&amp' ),
                          )

def getLogger(name):
    try:
        import bblogger.logger as bbl
        logger = bbl.getLogger( name, consoleformat = 'debug' )
    except Exception as E:
        import logging
        logger = logging.getLogger(__name__)
    return logger
