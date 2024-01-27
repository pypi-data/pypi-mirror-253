# Constant variables
import sys, os, re, logging
from os.path import join, expanduser, abspath
from typing import Generator

PROJECT_APP_NAME = 'BBLogger'
if 'PROJECT_APP_NAME' in os.environ and os.environ['PROJECT_APP_NAME']:
    PROJECT_APP_NAME = os.environ['PROJECT_APP_NAME']

APPUTILS_TEST_MODE = False
BBLOGGER_INIT_OUTPUT = False
FILE_DATE_FORMAT = '_%Y-%m-%d_%H-%M-%S'
LOG_APPNAME    = 'BBLogger'
LOG_AVOID_OVERWRITE = True
LOG_COLORED_OUTPUT = True
LOG_CONSOLE_FORMAT = 'basic'
LOG_FILEPATH = ''
LOG_FILE_FORMAT = 'html'
LOG_FILE_ROTATE_TIME = -1
LOG_FILE_VERBOSITY = logging.DEBUG
LOG_MAX_FILESIZE = 7878736
LOG_OUTPUT = sys.stderr
LOG_TO_CONSOLE = True
LOG_VERBOSITY = 3
LOG_WRITE_MODE = 'a'
SET_BBLOGGER_CLASS = True
STRING_SEQUENCE_MATCH_RATIO = 0.7

__mutable__ = { 'APPUTILS_TEST_MODE'            : ( False, "test mode - AppData will create files iand folders in temp directory" ),
                'BBLOGGER_APPNAME'              : ( 'BBLogger', "default" ),
                'BBLOGGER_AVOID_OVERWRITE'      : ( True, "avoid overwriting logfile - takes precedence and assumes 'b' for write mode" ),
                'BBLOGGER_COLORED_OUTPUT'       : ( True, "add colored output to console log" ),
                'BBLOGGER_CONSOLE_STREAM'       : ( True, "whether or not to open a stream handler for the console" ),
                'BBLOGGER_CONSOLE_FORMAT'       : ( 'basic', "type of formatting done with console logging - 'debug' adds more info" ),
                'BBLOGGER_FILE_FORMAT'          : ( 'html', "type of logfile - 'html' or 'plaintext'" ),
                'BBLOGGER_FILE_ROTATE_TIME'     : ( -1, "time in seconds to append, backup, or overwrite logfile if specified - ignored if < 0" ),
                'BBLOGGER_FILE_VERBOSITY'       : ( 1, "verbosity for logfile" ),
                'BBLOGGER_FILE_WRITE_MODE'      : ( 'a', "'a' append; 'b' backup; 'o' overwrite <--( ignored when LOG_AVOID_OVERWRITE = True )" ),
                'BBLOGGER_FILEPATH'             : ( '', "path to write logfile - no file is written to if blank" ),
                'BBLOGGER_MAX_FILE_SIZE'        : ( -1, "max logfile size before 'WRITE_MODE' setting takes place" ),    # TODO
                'BBLOGGER_OUTPUT_STREAM'        : ( sys.stderr, "use variable names 'STDOUT' and 'STDERR' to set" ),
                'BBLOGGER_ROOT_VERBOSITY'       : ( 1, "root logging level - limits child loggers to this level" ),
                'BBLOGGER_VERBOSITY'            : ( 2, "default logging verbosity" ),
                'BBLOGGER_INIT_OUTPUT'          : ( False, "show debugging info when bblogger is initialized" ),
                'FILE_DATE_FORMAT'              : ( '_%Y-%m-%d_%H-%M-%S', "date formatting to use with datetime.strftime()" ),
                'PROJECT_APP_NAME'              : ( 'PyDevUtils', "App name to use for creating folders - base directory is $HOME" ),
                'SET_BBLOGGER_CLASS'            : ( True, "set to False to skip bblogger initialization" ),
                'STRING_SEQUENCE_MATCH_RATIO'   : ( 0.7, "ratio threshold between 0 - 1 for 'apputils.tools.matchSimilar', which uses difflib.SequenceMatcher" ),
                }

#-------------------------------------------------------------------------#
#             Certain variables can be set by exporting the               #
#     variable name from the shell. These are listed in '__mutable__'     #
#-------------------------------------------------------------------------#

def __err__(s):
    sys.stderr.write(f"\x1b[1;31m  [ERROR]\x1b[2;37;3m {s}\x1b[0m")
    sys.stderr.flush()

_USER_SHELL_SETTINGS_ = set( os.environ )&set(__mutable__)
new = []
for name in _USER_SHELL_SETTINGS_:
    new.append( os.environ[name] )
    current = globals()[name]
    try:
        if isinstance( current, bool ):
            if new[-1] in ( 'true', 'True', 'TRUE', '1', 'yes', 'Yes', 'y', 'Y' ):
                globals()[name] = True
            elif new[-1] in ( 'false', 'False', 'FALSE', '0', 'no', 'No', 'n', 'N' ):
                globals()[name] = False
            else:
                raise ValueError
        else:
            new.append( type(current)( new[-1] ))
            globals()[name] = new[-1]
    except:
        __err__(f"Invalid value '{new[-1]}' for '{name}'")
        continue

__all__ = sorted(filter( lambda x: bool( not x.startswith('_') and x.isupper() ), dir() ))

def _viewShellSettings( *, view_constants = False, view_details = False ):
    import sys
    from io import TextIOWrapper
    from texttools import FG as c, Styles as S, Ansi, AnsiList, blockTxt
    from apputils import Path
    R = AnsiList([ '', f"  {c.dl&S.B&S.U}BB_PyUtils User Shell Options{S.U_}:{c._}", '' ], strsep = '\n' )
    def _getVal(v):
        if isinstance( v, TextIOWrapper ):
            name = v.name[1:-1].upper()
            if name == 'STDERR':
                return Ansi( f"{c.R&S.B&S.I}STDERR{c._}" )
            else:
                return Ansi( f"{c.gr.blend(c.b, 35)&S.B&S.I}STDOUT{c._}" )
        elif isinstance( v, bool ) or ( isinstance( v, str ) and v.title() in ('True', 'False') ):
            if v:
                return Ansi( f"{c.G&S.B&S.I}{str(v).title()}{c._}" )
            else:
                return Ansi( f"{c.R&S.B&S.I}{v}{c._}" )
        elif isinstance( v, float ) or ( isinstance( v, str ) and re.match( '^[0-9]*\.?[0-9]+$', v )):
            return Ansi( f"{(c.g.bright()&S.I).blend( c.c, 40 )}{v}{c._}" )
        elif isinstance( v, int ) or ( isinstance( v, str ) and v.isnumeric() ):
            return Ansi( f"{c.g&S.I}{v}{c._}" )
        elif v == sys.stderr or ( isinstance( v, str ) and v.lower() in ( 'sys.stderr', 'stderr' )):
            return Ansi( f"{(c.r&S.B&S.I).dim(35)}'STDERR'{c._}" )
        elif v == sys.stdout or ( isinstance( v, str ) and v.lower() == ( 'sys.stdout', 'stdout' )):
            return Ansi( f"{c.dl&S.B&S.I}'STDOUT'{c._}" )
        elif isinstance( v, str ):
            if Path.isfile(v) or Path.isdir(v):
                return Ansi( f"{(c.ce&S.I).blend( c.C, 60 )}{v}{c._}" )
            elif not v:
                return Ansi( f"{c.S&S.I}''{c._}" )
            else:
                return Ansi( f"{c.S&S.I}{v}{c._}" )
        else:
            try:
                r = v.__name__
            except:
                r = v

            return f"{c.Gr&S.I}{repr(r)}{c._}"

    width = os.get_terminal_size().columns - 10
    for key, ( _def, com ) in sorted( __mutable__.items(), key = lambda x: x[0] ):
        if key in Path.env:
            add = str( AnsiList( [ f"{c.gr&S.B&S.I}{repr(key)+':':>32}{c._} {_getVal( Path.env[key] )}",
                                   f"{c.dGr}{'  ':.<{width - len(add)}}{c.g&S.B} [env]{c._}" ],
                                 strsep = '\n' ))
        else:
            add = Ansi( f"{c.gr&S.B&S.I}{repr(key)+':':>32}{c._} {_getVal( _def )}" )

        if view_details:
            add += str( AnsiList([ f'\n{c.ce&S.I}{"":<14}"""',
                                   f"{'':<14}Default = {_getVal(_def).clean}",
                                   blockTxt( f"{c.ce&S.I}{'':<16}{' - '+com}", indent = 14, width = 50, width_includes_indent = False ),
                                   f'{c.ce&S.I}{"":<14}"""{c._}' ],
                                 strsep = '\n' ))
        R.append( add )

    if view_constants:
        R += [ '', f"  {c.dl&S.B&S.U}BB_PyUtils Constants{S.U_}:{c._}", '' ]
        for key in filter( lambda x: x.isupper() and x not in __mutable__, __all__ ):
            R.append( f"{c.gr&S.B&S.I}{repr(key)+':':>32}{c._} {_getVal( globals()[ key ])}" )

    R.append('')
    return str(R)

del __err__

def _script():
    import sys
    from . import getLogger
    log = getLogger(__name__)

    OPTS = {}
    opts = sys.argv[1:]
    while opts:
        opt = opts.pop(0)
        if opt in ( '-d', '--details' ):
            OPTS['view_details'] = True
        elif opt in ( '-c', '--constants' ):
            OPTS['view_constants'] = True
        else:
            log.error(f"Invalid option '{opt}'")
            sys.exit(1)

    string = _viewShellSettings( **OPTS )
    print(string)
    sys.exit(0)
