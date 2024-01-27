import sys, logging, os, re, atexit, io, traceback
from datetime import ( datetime as dt,
                       timedelta as td )
from os.path import ( isabs,
                      isdir,
                      isfile,
                      join as JN,
                      basename as BN,
                      dirname as DN,
                      expanduser as HOME,
                      splitext  )
from os import ( getcwd as pwd,
                 listdir as ls )

from functools import update_wrapper, wraps
from importlib.resources import files as _src

from . import _data
import texttools.texttools as TT
import texttools.ansitools as AT
import apputils
from ._constants import ( BBLOGGER_INIT_OUTPUT,
                          PROJECT_APP_NAME,
                          LOG_COLORED_OUTPUT,
                          LOG_CONSOLE_FORMAT,
                          LOG_OUTPUT,
                          LOG_TO_CONSOLE,
                          LOG_VERBOSITY,
                          LOG_AVOID_OVERWRITE,
                          LOG_FILE_FORMAT,
                          LOG_FILE_ROTATE_TIME,
                          LOG_FILEPATH,
                          LOG_FILE_VERBOSITY,
                          LOG_MAX_FILESIZE,
                          LOG_WRITE_MODE ,
                          SET_BBLOGGER_CLASS    )

global APPNAME, ROOTLEVEL, COLORED_OUTPUT, CONSOLE_FORMAT, OUTPUT, TO_CONSOLE, VERBOSITY, AVOID_OVERWRITE, FILE_FORMAT, FILE_ROTATE_TIME, FILEPATH, FILE_VERBOSITY, MAX_FILESIZE, WRITE_MODE, INIT_OUTPUT
if 'BBLOGGER_INIT_OUTPUT' in os.environ:
    INIT_OUTPUT = apptools.getBoolFromString( os.environ['BBLOGGER_INIT_OUTPUT'] )
else:
    INIT_OUTPUT = BBLOGGER_INIT_OUTPUT

# logger options
appname = apputils.findProjectName() if PROJECT_APP_NAME == 'BB_PyDev' else ''
if appname:
    APPNAME = appname
else:
    APPNAME = PROJECT_APP_NAME

ROOTLEVEL = logging.DEBUG

# stream handler options
COLORED_OUTPUT = LOG_COLORED_OUTPUT
CONSOLE_FORMAT = LOG_CONSOLE_FORMAT
OUTPUT         = LOG_OUTPUT
TO_CONSOLE     = LOG_TO_CONSOLE
VERBOSITY      = LOG_VERBOSITY

# file handler options
AVOID_OVERWRITE  = LOG_AVOID_OVERWRITE
FILE_FORMAT      = LOG_FILE_FORMAT
FILE_ROTATE_TIME = LOG_FILE_ROTATE_TIME
FILEPATH         = LOG_FILEPATH
FILE_VERBOSITY   = LOG_FILE_VERBOSITY
MAX_FILESIZE     = LOG_MAX_FILESIZE      # TODO
WRITE_MODE       = LOG_WRITE_MODE

Path              = apputils.Path
Date              = apputils.Date
readFile          = apputils.readFile
writeFile         = apputils.writeFile
getBoolFromString = apputils.getBoolFromString
FileLock          = apputils.FileLock
TextTools         = TT.TextTools
Ansi              = AT.Ansi
AnsiList          = AT.AnsiList

c  = TextTools.FG_Colors
bg = TextTools.BG_Colors
s  = TextTools.Styles

def _out_(s, **kwargs):
    if INIT_OUTPUT:
        sys.stderr.write(f"  {s}\n")
        sys.stderr.flush()

def _get_logger_environment_variables_(func):
    """
    User Shell Options:
      'BBLOGGER_APPNAME'         : (string) set a name for the root logger
      'BBLOGGER_AVOID_OVERWRITE' : (bool value) don't overwrite log file [default = True]
      'BBLOGGER_COLORED_OUTPUT'  : (bool value) use color in console logging [default = True]
      'BBLOGGER_CONSOLE_FORMAT'  : 'debug'|'basic' provide more info on each line with 'debug' [default = 'basic']
      'BBLOGGER_CONSOLE_STREAM'  : output stream - 'stderr'[default] or 'stdout'
      'BBLOGGER_FILE_FORMAT'     : 'html'|'plaintext' [default = 'html']
      'BBLOGGER_FILE_ROTATE_TIME': amount of seconds before log file is overwritten (default -1)
                                    - ignored if less than 0
      'BBLOGGER_FILE_VERBOSITY'  : (1 - 5) logging level for file output [default = 1]
      'BBLOGGER_FILE_WRITE_MODE' : (string) 'a' - append, 'b' - backup, or 'w' - write
      'BBLOGGER_FILEPATH'        : path to log file to [default = None]
      'BBLOGGER_MAX_FILE_SIZE'   : maximum size for logfile in bytes before rotation
      'BBLOGGER_ROOT_VERBOSITY'  : (1 - 5) log level to set the root logger [default = 1]
      'BBLOGGER_VERBOSITY'       : (1 - 5) log level for console output [default = 3]
    """
    global VERBOSITY

    @wraps(func)
    def __wrap( *args, **opts ):
        variables = [( 'BBLOGGER_APPNAME'               , 'appname'         ),
                     ( 'BBLOGGER_AVOID_OVERWRITE'       , 'avoid_overwrite' ),
                     ( 'BBLOGGER_COLORED_OUTPUT'        , 'color'           ),
                     ( 'BBLOGGER_CONSOLE_STREAM'        , 'console'         ),
                     ( 'BBLOGGER_CONSOLE_FORMAT'        , 'consoleformat'   ),
                     ( 'BBLOGGER_FILE_FORMAT'           , 'fileformat'      ),
                     ( 'BBLOGGER_FILE_ROTATE_TIME'      , 'overwrite_time'  ),
                     ( 'BBLOGGER_FILE_VERBOSITY'        , 'filelevel'       ),
                     ( 'BBLOGGER_FILEPATH'              , 'filepath'        ),
                     ( 'BBLOGGER_MAX_FILE_SIZE'         , 'max_file_size'   ),
                     ( 'BBLOGGER_OUTPUT_STREAM'         , 'output_stream'   ),
                     ( 'BBLOGGER_ROOT_VERBOSITY'        , 'rootlevel'       ),
                     ( 'BBLOGGER_FILE_WRITE_MODE'       , 'file_write_mode' ),
                     ( 'BBLOGGER_VERBOSITY'             , 'global_level'    )]

        env = os.environ
        for shell_var, mod_var in variables:
            if shell_var in env:
                _out_(f'{c.gr&s.I}  Found "{c._&c.dl&s.B}{shell_var}{c.g} ={c.dl} {env[shell_var]}{c._&c.gr&s.I}" in user shell variables')
                opts[mod_var] = env[shell_var]

        return func( *args, **opts )
    return __wrap

class BBFormatter(logging.Formatter):
    """
    BBFormatter - Color logging output with ansi or html

        mode = 'basic' (console)
                Basic logging for end user messages

               'debug' (console)
                More output information for debugging

               'html' (file)
                Uses html format to color logs to send to an html file or gui
                program that supports html formatting

               'plaintext' (file)
                No escapes inserted for logging plaintext to a file

    """

    def __init__(self, *, mode = 'basic', colored = COLORED_OUTPUT ):
        super().__init__()

        # logging colors
        _debug  = str( c._ & c.Gr & s.B  )  # debug                 #a0a0a0
        _infoo  = str( c._ & c.ice & s.B )  # info                  #719bcf
        _warnn  = str( c._ & c.Gd  & s.B )  # warning               #cccc00
        _error  = str( c._ & c.r   & s.B )  # error                 #ff6666
        _critt  = str( c._ & c.R & s.B   )  # critical              #cc0000 + Underline

        _time   = str( c._ & c.gr        )  # time                  #e0e0e0
        _num    = str( c._ & c.g & s.B   )  # lineno                #e0e0e0
        _msg    = str( c._ & c.dl & s.I  )  # msg text              #9eb0a0 + Italic
        _name   = str( c._ & c.C & s.I   )  # filename text         #009987 + Italic
        _errm   = str( c._ & c.nO & s.I  )  # error message text    #eaa938 + Italic
        _crmsg  = str( c._ & c.dR & s.I  )  # critical message text #990000 + Italic

        _g      = str(c.dGr)                # dark gray
        __      = str(c.W +'.'+ c._)        # white dot
        _time_  = '%(asctime)s'             # TIMESTAMP
        _mod_   = '%(module)s'              # MODULE
        _name_  = '%(filename)s'            # NAME
        _func_  = '%(funcName)s'            # FUNCTION
        _num_   = '%(lineno)s'              # LINE NO
        _lvl_   = '[%(levelname)s]'         # LOG LEVEL NAME
        _msg_   = '%(msg)s'

        self.colors = { 'DEBUG'   : _debug,
                        'INFO'    : _infoo,
                        'WARNING' : _warnn,
                        'ERROR'   : _error,
                        'CRITICAL': _critt }

        if mode == 'basic':
            __debug    = Ansi(f"{_debug}  {_lvl_} {_g}<{_num}{_num_}{_g}>{_debug}:{c._} {_msg_}")
            __info     = Ansi(f"{_infoo}  {_lvl_} {_g}<{_num}{_num_}{_g}>{_infoo}:{c._} {_msg_}")
            __warning  = Ansi(f"{_warnn}  {_lvl_} {_g}<{_num}{_num_}{_g}>{_warnn}:{c._} {_msg_}")
            __error    = Ansi(f"{_error}  {_lvl_} {_g}<{_num}{_num_}{_g}>{_error}:{c._} {_msg_}")    # {_error}"
            __critical = Ansi(f"{_critt}  {_lvl_} {_g}<{_num}{_num_}{_g}>{_critt}:{c._} {_msg_}")    # {_critt}"

        elif mode == 'debug':
            __debug    = Ansi(f"{_debug} {_lvl_} {_name}{_name_} {_debug}{_func_} <{_num}{_num_}{_debug}>:{c._} {_msg_}")    # {_debug}{_name_}{__}
            __info     = Ansi(f"{_infoo} {_lvl_} {_name}{_name_} {_infoo}{_func_} <{_num}{_num_}{_infoo}>:{c._} {_msg_}")    # {_infoo}{_name_}{__}
            __warning  = Ansi(f"{_warnn} {_lvl_} {_name}{_name_} {_warnn}{_func_} <{_num}{_num_}{_warnn}>:{c._} {_msg_}")    # {_warnn}{_name_}{__}
            __error    = Ansi(f"{_error} {_lvl_} {_name}{_name_} {_error}{_func_} <{_num}{_num_}{_error}>:{c._} {_msg_}")    # {_error}{_name_}{__}
            __critical = Ansi(f"{_critt} {_lvl_} {_name}{_name_} {_critt}{_func_} <{_num}{_num_}{_critt}>:{c._} {_msg_}")    # {_critt}{_name_}{__}

        elif mode == 'plaintext':
            __debug = __info = __warning = __error = __critical = f"  {_time_} {_num_:^14}{_name_}.{_mod_}.{_func_} {_lvl_}: {_msg_}"

        elif mode == 'html':
            # def getTable( msg, color ):
            #     return ''.join([ '    <table>',
            #                      f'<tr><td style="font-size: 14pt; padding-left: 2em; margin-left: 0;" colspan=5>{Ansi( f"{color}[%(levelname)s]:" ).html()}',
            #                      f'&nbsp&nbsp<span style="font-size: 12pt;">{Ansi( msg ).html()}</span></td>',
            #                      f'<td style="text-align: right;">{Ansi( f"{_time}%(asctime)s" ).html()}</td>',
            #                      '</tr><tr><td style="width: 1em; margin: 0; padding: 0;"></td>',
            #                      f'<td style="text-align: left;" colspan=3>{Ansi( f"{c.S}File:&nbsp{_name}%(pathname)s" ).html()}</td>',
            #                      f'<td style="text-align: left;">{Ansi( f"{c.S}Line:&nbsp&nbsp{c._&c.g&s.B}%(lineno)d" ).html()}</td>',
            #                      f'<td style="text-align: left; margin-left: 0;">{Ansi( f"{color}%(name)s{__}{color}%(funcName)s" ).html()}</td>',
            #                      '<td style="width: 6em;"></td>',
            #                      '</tr></table>' ])
            #
            # __debug    = getTable( f"{_msg}%(message)s", _debug )
            # __info     = getTable( f"{_msg}%(message)s", _infoo )
            # __warning  = getTable( f"{_msg}%(message)s", _warnn )
            # __error    = getTable( f"{_errm}%(message)s", _error )
            # __critical = getTable( f"{_crmsg}%(message)s", _critt )

            __debug    = ''.join([ "\n    <p><span style=\"color: #717e73;\">%(asctime)s </span>",
                                   "<span style=\"color: #474f48;\"> %(name)s>%(module)s.%(funcName)s </span>",
                                   "<b>[ %(lineno)d ]</b>", "<span style=\"color: #474f48;\"> %(levelname)s: </span>",
                                   "<span style=\"color: #5c675e; font-style: italic;\">%(message)s</span></p>" ])
            __info     = ''.join([ "\n    <p><span style=\"color: #717e73;\">%(asctime)s </span>",
                                   "<span style=\"color: #2b3b4f;\"> %(name)s>%(module)s.%(funcName)s </span>",
                                   "<b>[ %(lineno)d ]</b>", "<span style=\"color: #2b3b4f;\"> %(levelname)s: </span>",
                                   "<span style=\"color: #5c675e; font-style: italic;\">%(message)s</span></p>" ])
            __warning  = ''.join([ "\n    <p><span style=\"color: #717e73;\">%(asctime)s </span>",
                                   "<span style=\"color: #8d891c;\"> %(name)s>%(module)s.%(funcName)s </span>",
                                   "<b>[ %(lineno)d ]</b>", "<span style=\"color: #8d891c;\"> %(levelname)s: </span>",
                                   "<span style=\"color: #5c675e; font-style: italic;\">%(message)s</span></p>" ])
            __error    = ''.join([ "\n    <p><span style=\"color: #717e73;\">%(asctime)s </span>",
                                   "<span style=\"color: #4f1b1b;\"> %(name)s>%(module)s.%(funcName)s </span>",
                                   "<b>[ %(lineno)d ]</b>", "<span style=\"color: #4f1b1b;\"> %(levelname)s: </span>",
                                   "<span style=\"color: #cf6d6d; font-style: italic;\">%(message)s</span></p>" ])
            __critical = ''.join([ "\n    <p><span style=\"color: #717e73;\">%(asctime)s </span>",
                                   "<span style=\"color: #fc0202;\"> %(name)s>%(module)s.%(funcName)s </span>",
                                   "<b>[ %(lineno)d ]</b>", "<span style=\"color: #fc0202;\"> %(levelname)s: </span>",
                                   "<span style=\"color: #a33e3e; font-style: italic;\">%(message)s</span></p>" ])

        self.mode    = mode
        self.color   = colored
        self.__crit  = __critical
        if colored:
            self.FORMAT  = { logging.DEBUG    : __debug,
                             logging.INFO     : __info,
                             logging.WARNING  : __warning,
                             logging.ERROR    : __error,
                             logging.CRITICAL : __critical }
        else:
            self.FORMAT  = { logging.DEBUG    : __debug.clean,
                             logging.INFO     : __info.clean,
                             logging.WARNING  : __warning.clean,
                             logging.ERROR    : __error.clean,
                             logging.CRITICAL : __critical.clean }

    def formatException(self, exc_info):
        # From builtin ---------------------------------------
        sio = io.StringIO()
        tb = exc_info[2]
        traceback.print_exception(exc_info[0], exc_info[1], tb, None, sio)
        string = sio.getvalue()
        sio.close()
        # ----------------------------------------------------

        if self.mode in ( 'basic', 'debug' ):
            try:
                termwidth = os.get_terminal_size().columns
            except:
                termwidth = 200

            max_width = max([ len(line) for line in string.split('\n') ])
            width = max_width + 4 if max_width + 8 <= termwidth else termwidth
            if width < termwidth:
                _in = f"{'':<{int(( termwidth - width - 8 )/4 )}}"
            else:
                _in = ''

            _s = AnsiList( f"{_in}{bg.ch:<{width+4}}{c._}", strsep = '\n' )
            for line in string.split('\n'):
                line = Ansi(line)
                if line and line.split()[0] == 'File':
                    _a, _b, _c = line.partition('File')
                    for _c_ in re.findall( '[0-9+]', _c ):
                        _c = Ansi( _c.replace( _c_, f"{c._&c.g&bg.ch}{_c_}{c._&c.W&bg.ch}" ))
                    _s.append( f"{_in}{bg.ch}    {Ansi( f'{c.ice}{_a}{c._&bg.ch&c.W&s.B}{_b}: {_c} ' ):<{width}}{c._}" )

                elif line and line[0] != ' ':
                    if re.match( '^[A-Z]{1}[a-zA-Z]+:$', line.split()[0] ):
                        if len(line.split()) > 1:
                            _s.append( f"{_in}{bg.ch}    {c.R&s.B}{line.split()[0]}{c._&bg.ch&c.Gr} {' '.join(line.split()[1:]):<{ width - len(line.split()[0]) - 1 }}{c._}" )
                        else:
                            _s.append( f"{_in}{bg.ch}    {c.R&s.B}{line.split()[0]:<{width}}{c._}" )

                    else:
                        _s.append( f"{_in}{bg.ch}    {c.ice&s.B}{line:<{width}}{c._}" )
                else:
                    _s.append( f"{_in}{bg.ch}    {c.gr&s.I}{line:<{width}}{c._}" )

            if self.color:
                return str(_s)
            return str(_s).clean

        elif self.mode == 'plaintext':
            return string

        elif self.mode == 'html':
            return f'    <pre style="margin-left: 7%;" white-space="pre-wrap"><code class="hljs">{string}</code></pre>'

    def format(self, record):
        log_fmt = self.FORMAT.get(record.levelno)
        msg = Ansi( record.getMessage() )
        if self.color:
            record.funcName = record.funcName.replace( '.', c.W +'.'+ self.colors[ record.levelname ])
        msgcol = self.colors[record.levelname]

        if self.mode in ( 'basic', 'debug' ):
            try:
                width = os.get_terminal_size().columns
            except:
                width = 200

            if self.color:
                tmcol = c._ & c.gr & s.B
                if record.levelno == logging.CRITICAL:
                    msgcol = c._ & c.dR & s.I   # critical message text #990000 + Italic
                elif record.levelno == logging.ERROR:
                    msgcol = c._ & c.nO & s.I   # error message text    #eaa938 + Italic
                else:
                    msgcol = c._ & c.dl & s.I   # msg text              #9eb0a0 + Italic
            else:
                msgcol = ''

            indent = len(record.levelname) + 5
            if self.mode == 'basic':
                _in = indent + len(str(record.lineno)) + 4
            else:
                _in = len(record.filename) + len(record.funcName) + len(record.levelname) + len(str(record.lineno)) + 10

            space = width - _in - len( msg ) - 16
            if space < 0:
                msg = TextTools.blockTxt( f"{msgcol}{msg}",
                                          indent = indent,
                                          width = -4,
                                          start_column = _in )

                space = width - len( Ansi( msg.split('\n')[-1] )) - 16

                if space < 0:
                    msg = Ansi( f"{msg}\n{'':<{indent}}" )

                space = width - len( Ansi( msg.split('\n')[-1] )) - 16

            if space == 0:
                log_fmt = Ansi(f"{log_fmt}{tmcol}  - %(asctime)s{c._}")
            else:
                log_fmt = Ansi(f"{log_fmt} {' ':.<{space}}{tmcol} - %(asctime)s{c._}")

            record.msg = Ansi(f"{msgcol}{msg}")
            formatter = logging.Formatter(log_fmt, '[%R:%S]')

        elif self.mode == 'html':
            # while any( msg.clean.startswith(i) for i in ( ' ', '.' )):
            #     msg = msg[1:]
            record.msg = msg.html()
            formatter = logging.Formatter(log_fmt, '%a, %m/%d/%y [%R:%S]:')

        if record.exc_info:
            record.exc_text = self.formatException(record.exc_info)

        return formatter.format(record)

class ConsoleOut( logging.StreamHandler ):
    def __init__( self, level, *, mode, colored, out = sys.stderr, formatter = None, name = '' ):
        super().__init__(out)
        self.name = str(name)
        self.logging_mode = mode
        self.logging_color = colored
        self.setLevel(level)
        self.setFormatter( formatter )

    def setFormatter(self, fmt = None, **options):
        if fmt in ( None, BBFormatter ):
            opts = { 'mode'   : self.logging_mode,
                     'colored': self.logging_color,
                     **options }
            super().setFormatter( BBFormatter( **opts ))
        else:
            super().setFormatter( fmt )

    def setLoggingMode(self, mode: str):
        assert mode in ( 'basic', 'debug', None )
        if not mode:
            if self.level == logging.DEBUG:
                mode = 'debug'
            else:
                mode = 'basic'

    def color(self, B: bool):
        """ Set logging color to True/False """
        if not isinstance( self.formatter, BBFormatter ):
            return
        self.logging_color = bool(B)
        return self.setFormatter()

class BBLogger( logging.getLoggerClass() ):
    """
    Console and file logging, formatted with BBFormatter
        - options are set through logger.getLogger() with initial call
        - subsequent loggers should be called with python's logging
          module: logging.getLogger()
    """

    def __init__(self, name, level = VERBOSITY ):
        global APPNAME, ROOTLEVEL, COLORED_OUTPUT, CONSOLE_FORMAT, OUTPUT, TO_CONSOLE, VERBOSITY, AVOID_OVERWRITE, FILE_FORMAT, FILE_ROTATE_TIME, FILEPATH, FILE_VERBOSITY, MAX_FILESIZE, WRITE_MODE
        super().__init__( name, level = level )
        self.propagate = False

        owt = 0
        if TO_CONSOLE:
            self.console_stream = ConsoleOut( self.level,
                                              mode = CONSOLE_FORMAT,
                                              colored = COLORED_OUTPUT,
                                              out = OUTPUT,
                                              name = self.name+"_stream" )
            self.addHandler( self.console_stream )

        if FILEPATH:
            errors = []
            if FILE_FORMAT == 'html':
                FILEPATH = f"{Path.splitext(FILEPATH)[0]}.html"

            if FILE_ROTATE_TIME > 0:
                if FILE_ROTATE_TIME > 1000:
                    owt = Date( seconds = FILE_ROTATE_TIME )
                else:
                    owt = Date( days = FILE_ROTATE_TIME )
            elif AVOID_OVERWRITE:
                owt = 0
            else:
                owt = -1

            try:
                if path == Path.bn( path ):
                    path = Path.join( Path.home(), path )

                if Path.isfile(FILEPATH) and ( owt < 0 or Date() - Path.info( FILEPATH ).ctime < owt ):
                    assert os.access( FILEPATH, os.W_OK ) and os.access( FILEPATH, os.R_OK )

                    if FILE_FORMAT == 'html':
                        with FileLock( FILEPATH, 'r+', encoding = 'utf-8' ) as f:
                            filedata = f.read()

                            if filedata.endswith('\n</body></html>'):
                                f.seek(0)
                                filedata = filedata[:-7]
                                f.write( filedata )

                else:
                    if Path.isfile( FILEPATH ):
                        assert os.access( FILEPATH, os.W_OK ) and os.access( FILEPATH, os.R_OK )
                        if AVOID_OVERWRITE or WRITE_MODE == 'b' \
                            or ( FILE_FORMAT == 'html' and not FILEPATH.endswith('.html') ):
                                moveto = Path.jn( Path.dn( FILEPATH ), f"LOG-{int(Date.ts())}_{Path.bn( FILEPATH )}" )
                                Path.mv( FILEPATH, moveto )

                    elif not Path.isfile( FILEPATH ):
                        assert os.access( Path.dn( FILEPATH ), os.W_OK ) and os.access( Path.dn( FILEPATH ), os.R_OK )

                    if FILE_FORMAT == 'html':
                        src_dir = _src( _data )
                        with open( src_dir.joinpath( 'new_html' ), 'r', encoding = 'utf-8' ) as f:
                            newfiledata = f.read().replace( '__URL__', src_dir.as_posix() )
                    else:
                        newfiledata = "\n# BBLogger logging module\n\n"

                    mode = 'w' if WRITE_MODE == 'w' else 'a'
                    with open( FILEPATH, mode ) as f:
                        f.write( newfiledata )

            except AssertionError:
                raise PermissionError( f"User doesn't have read/write access to '{FILEPATH}'" )

            fhdlr = logging.FileHandler( FILEPATH, mode = 'a', encoding = 'utf-8' )
            fhdlr.setFormatter( BBFormatter( mode = FILE_FORMAT ))
            fhdlr.setLevel( FILE_VERBOSITY )

            atexit.register( self._endHtml_ )
            self.addHandler( fhdlr )

        self.setLevel( level )

    def setLevel(self, level = None, *opts, set_global = False):
        """
        Set logging level for individual log object
            'set_global': set global verbosity level
                           - optionally use 'opts'
                'opts':
                    'file_level': include setting file log level
                    'ignore_console': don't set level of already initiated
                                      console loggers
        """
        if level:
            level = getLoggingLevel( level )
        else:
            level = VERBOSITY

        if set_global:
            return self.__set_global_level__( getLoggingLevel( level ), *opts )

        super().setLevel( getLoggingLevel( level ))

    def __set_global_level__(self, level = None, *opts):
        """
        Set logging level for individual log object
            'set_global': set global verbosity level
                           - optionally use 'opts'
                'opts':
                    'file_level': include setting file log level
                    'ignore_console': don't set level of already initiated
                                      console loggers

            - acceptable modes:
                'debug'    | logging.DEBUG    | 10 | 1 <or> 0
                'info'     | logging.INFO     | 20 | 2
                'warning'  | logging.WARNING  | 30 | 3
                'error'    | logging.ERROR    | 40 | 4
                'critical' | logging.CRITICAL | 50 | 5
        """
        if level:
            global VERBOSITY
            VERBOSITY = level

        logger = self
        while logger:
            for i in logger.handlers:
                if isinstance( i, logging.FileHandler) and 'file_level' in opts:
                    i.setLevel( FILE_VERBOSITY )
                elif isinstance( i, logging.StreamHandler) and 'ignore_console' not in opts:
                    i.setLevel( VERBOSITY )
            logger = logger.parent

    def set_format(self, formatting):
        """
        Change formatting for console logging
            'basic' - simple, nicely formatted messaging
            'debug' - more info pertaining to each message
                      * defaults to log level 1
        """
        if formatting not in ( 'basic', 'debug' ):
            raise SyntaxError(f"Invalid formatting option - '{formatting}'")

        if ConsoleOut not in [ type(i) for i in self.handlers ]:
            self.warning( "Missing StreamHandler - skipping set formatting" )
            return
        for i in self.handlers:
            if not isinstance( i, logging.FileHandler ):
                i.setFormatter( BBFormatter( mode = formatting ))
                if formatting == 'debug':
                    i.setLevel( logging.DEBUG )

    def _endHtml_(self):
        if not Path.isfile( FILEPATH ):
            return
        with FileLock( FILEPATH, 'r' ) as f:
            fd = r.read()

        if not fd.endswith('\n</body></html>'):
            with FileLock( FILEPATH, 'a', encoding = 'utf-8' ) as f:
                f.write( '\n</body></html>' )

    def __repr__(self):
        return f"(< BBLogger {self.name} [ Level: {self.level}, Mode: '{CONSOLE_FORMAT}' ] >)"

@_get_logger_environment_variables_
def getLogger( name, level = None, **opts ):
    """
    Set custom logger class and return logger
      - only use this for initial call to logger. Use logging.getLogger() for
        further logging modules

        'name'    = Name of returned logger
        'level'   = Log level for the returned logger. Defaults to 1.

        **opts:
              More options for logger. To print the log to a file, 'filepath'
            must be present in the opts.

            'appname'          : [ DEFAULT 'BB-Logger' ] Application name
            'console'          : [ DEFAULT = True ] Print logging to console
            'consoleformat'    : [ DEFAULT = 'basic' ] Console formatting. Options are
                                    'basic' or 'debug'.
            'color'            : [ DEFAULT = True ] colorized console logging
            'filepath'         : [ DEFAULT None ] The path for a file to be written to. The
                                    directory for the file must exist.
            'filelevel'        : [ DEFAULT = 1 ] Set log level for file. Default is 1, DEBUGGING
                                    - must be set with initial call to logger.getLogger()
            'rootlevel'        : [ DEFAULT = 1 ] Set the root logger level
                                    - usually best to keep this default
            'fileformat'       : [ DEFAULT = 'html' ] Text formatting for file - 'plaintext'
                                    or 'html'
            'file_write_mode'  : [ DEFAULT = 'a' ] write mode for file stream
                                    - 'a': append, 'b': backup old logfile, 'w': overwrite old logfile
            'overwrite_time'   : [ DEFAULT = -1 ] Ignored if < 0. Amount of seconds before logfile
                                    is overwritten
            'avoid_overwrite'  : [ DEFAULT = True ] Don't overwrite the logfile if existing


              A new file will be created if not existing as long as the directory
            already exists. If only a filename is given for 'path', the file will
            be written in the user's HOME folder. Extra options should only need
            applied for the first time initiating a logger in your app/script.

        NOTE: Shell environment variables will override programatic calls to BBLogger
    """
    if logging.getLoggerClass() != BBLogger and SET_BBLOGGER_CLASS:
        logging.setLoggerClass( BBLogger )

    global APPNAME, ROOTLEVEL, COLORED_OUTPUT, CONSOLE_FORMAT, OUTPUT, TO_CONSOLE, VERBOSITY, AVOID_OVERWRITE, FILE_FORMAT, FILE_ROTATE_TIME, FILEPATH, FILE_VERBOSITY, MAX_FILESIZE, WRITE_MODE

    for opt, arg in opts.items():
        try:
            if opt == 'appname':
                APPNAME = str( arg )

            elif opt == 'avoid_overwrite':
                try:
                    arg = getBoolFromString( arg )
                    AVOID_OVERWRITE = arg
                except:
                    raise ValueError("Invalid value for 'avoid_overwrite' - expected a boolean ( default = True )")

            elif opt == 'color':
                try:
                    arg = getBoolFromString( arg )
                    COLORED_OUTPUT = arg
                except:
                    raise TypeError("Expected boolean for 'color' option")

            elif opt == 'consoleformat':
                arg = str(arg).lower()
                if arg not in ( 'basic', 'debug', 'plaintext', 'html' ):
                    raise TypeError(f"Invalid console format - '{arg}'")
                CONSOLE_FORMAT = arg

            elif opt == 'output_stream':
                arg = str(arg).lower()
                if arg not in ( 'stdout', 'stderr' ):
                    raise ValueError(f"Invalid output stream '{opts['output_stream']}' - expected 'stdout' or 'stderr'")
                OUTPUT = arg

            elif opt == 'filepath':
                if not Path.isdir( Path.dn( Path.abs( arg ))):
                    raise FileNotFoundError(f"Directory doesn't exist - '{DN(arg)}'")
                FILEPATH = arg

            elif opt == 'fileformat':
                if str(arg).lower() not in ( 'plaintext', 'html' ):
                    raise ValueError(f"Invalid file format - '{arg}'")
                FILE_FORMAT = str(arg).lower()

            elif opt == 'file_write_mode':
                try:
                    assert str(arg).lower() in ('a', 'b', 'w')
                    WRITE_MODE = arg.lower()
                except:
                    raise ValueError(f"Invalid argument for '{opt}' - expected 'a', 'b', or 'w'")
            elif opt == 'overwrite_time':
                try:
                    arg = int(arg)
                    FILE_ROTATE_TIME = arg
                except:
                    raise ValueError("Invalid file overwrite_time - expected an integer (-1 = no overwrite [default])")

            elif opt == 'filelevel':
                arg = getLoggingLevel( arg )
                FILE_VERBOSITY = arg

            elif opt == 'console':
                try:
                    arg = getBoolFromString( arg )
                    TO_CONSOLE = arg
                except:
                    raise TypeError("Expected boolean for 'console' option")

            elif opt == 'max_file_size':
                try:
                    arg = int( arg )
                    MAX_FILESIZE = arg
                except:
                    raise ValueError("Invalid file size value - expected an integer (size in bytes)")

            elif opt == 'global_level':
                arg = getLoggingLevel( arg )
                VERBOSITY = arg

            elif opt == 'rootlevel':
                arg = getLoggingLevel( arg )
                ROOTLEVEL = arg

        except Exception as E:
            _out_(f"{c.r&s.B} [{E.__class__.__name__}]{c.Gr&s.I} {' '.join([ str(i) for i in E.args ])}{c._}")
            continue

    if level:
        level = getLoggingLevel( level )
    else:
        level = VERBOSITY

    logger = BBLogger( __name__, level = level )

    root = logger.root
    root.name = APPNAME
    root.setLevel( ROOTLEVEL )

    return logger

def getLoggingLevel(L):
    """
    Translate verbosity from level argument
    """
    verbosity = { '0': logging.DEBUG   ,
                  '1': logging.DEBUG   , 'debug'   : logging.DEBUG   , logging.DEBUG   : logging.DEBUG   ,
                  '2': logging.INFO    , 'info'    : logging.INFO    , logging.INFO    : logging.INFO    ,
                  '3': logging.WARNING , 'warning' : logging.WARNING , logging.WARNING : logging.WARNING ,
                  '4': logging.ERROR   , 'error'   : logging.ERROR   , logging.ERROR   : logging.ERROR   ,
                  '5': logging.CRITICAL, 'critical': logging.CRITICAL, logging.CRITICAL: logging.CRITICAL    }

    try:
        try:
            lvl = verbosity[ L ]
        except:
            L = str(L).replace('0','').lower()
            lvl = verbosity[ L ]
        return lvl

    except Exception as E:
        raise ValueError(f"Invalid log level value '{L}'")

__all__ = [ 'getLoggingLevel',
            'BBFormatter',
            'BBLogger',
            'ConsoleOut',
            'getLogger' ]
