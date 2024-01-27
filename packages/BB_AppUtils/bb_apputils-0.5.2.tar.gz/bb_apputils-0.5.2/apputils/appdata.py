import sys, re
from os import environ as ENV

from ._constants import FILE_DATE_FORMAT, PROJECT_APP_NAME, getLogger, _AU_TMP_DIR_
from ._import import Path, Date
from .tools import uniqueName, getBoolFromString

class AppData:
    __test__ = False

    def __init__(self, appname = PROJECT_APP_NAME, *, test_mode = False):
        """
          'appname': set application name for base directory of app files
        """
        self.name = appname
        if 'APPUTILS_TEST_MODE' in ENV:
            self.__test__ = getBoolFromString( ENV['APPUTILS_TEST_MODE'] )
        else:
            self.__test__ = test_mode

    def appdir(self, d, *folders, file = '', datefile = '', create_dir = True, unique = False, move_existing = False):
        """
        *args
          'd': system directory type
                - varies on different operating systems - see sysdata
                - 'cache' : users cache directory
                - 'config': users config directory
                - 'data'  : main app directory
                - 'launch': directory where app launchers are placed
          '*folders': path names to append to returned path

        **kwargs
          'create_dir': create directories before they're returned
          'datefile': strftime format to add to filename if file != None
                       - adds date data before extension or at end of filename
                       - if set to 'timestamp', the standard timestamp (without
                         nanoseconds) is used
                       - if set to True, the default dating format is used
                       - default date format: '_%Y-%m-%d_%H-%M-%S'
          'file': add a filename to the end of the returned path
          'move_existing': if file is set and exists, will move the old file to
                           '~filename'. If that already exists, then '~filename (n)',
                           'n' being the first number to make a unique pathname
                             - only applies if 'file' is set

          'unique': avoid overwriting a file by setting unique to True
                     - renames file by adding an integer to the end
                     - does nothing if 'file' is not set
        """
        log = getLogger(__name__)
        if d.lower() not in ('data', 'cache', 'config', 'launch', 'home', 'userhome'):
            raise SyntaxError(f"Invalid directory - '{d}'")

        _dir = Path.jn( self.sysdata(d), *folders )

        if Path.isdir( _dir ):
            log.debug(f"Directory '{_dir}' exists")
        elif create_dir:
            log.info(f"Creating directory '{_dir}'")
            Path.mkdir(_dir)
        else:
            log.warning(f"Directory '{_dir}' doesn't exist")

        if file:
            date = ''
            file_path = Path.jn( _dir, file )
            if Path.isfile( file_path ):
                if unique:
                    log.debug(f"File '{file_path}' exists - renaming provided file")
                    file_path = uniqueName( file_path )
                elif move_existing:
                    moveTo = uniqueName( Path.jn( _dir, f"~{file}" ))
                    log.warning(f"Moving existing file to '{moveTo}'")
                    Path.mv( file_path, moveTo )
                else:
                    log.debug(f"File '{file_path}' exists and could be overwritten")
            if datefile:
                _dt = Date()
                if datefile == 'timestamp':
                    date = f"_{int(_dt.timestamp())}"
                elif isinstance( datefile, str ):
                    try:
                        date = _dt.strftime( datefile )
                    except exception as E:
                        log.error(str(E))
                        date = _dt.strftime( FILE_DATE_FORMAT )
                else:
                    date = _dt.strftime( FILE_DATE_FORMAT )
                try:
                    fn, ext = Path.splitext( file_path )
                except:
                    fn, ext = file_path, ''

                file_path = f"{fn}{date}{ext}"

            _dir = file_path
        return _dir

    def sysdata(self, *args, as_tuple = False):
        """
        Return systeminfo
          *args:
            'cache'||'data'||'config'||'launch' - app directories
            'home'||'userhome'                  - user's home folder
            'user'||'username'                  - user login name
            'os'||'system'                      - operating system

          **kwargs:
            'as_tuple': if getting a directory and True, return as a tuple instead
                        of using os.path.join
        """
        if not self.name:
            raise NameError("Cannot return a path without an app name")
        R = []
        OS = sys.platform.lower()

        if self.__test__:
            USER_HOME = _AU_TMP_DIR_
        else:
            USER_HOME = Path.home()

        USER = Path.user()
        APP_DATA = { '_TMP_'  : { 'config': Path.jn( _AU_TMP_DIR_, '.config', self.name ),
                                  'data'  : Path.jn( _AU_TMP_DIR_, '.local', 'share', self.name ),
                                  'launch': Path.jn( _AU_TMP_DIR_, '.local', 'share', 'applications' ),
                                  'cache' : Path.jn( _AU_TMP_DIR_, '.cache', self.name )},
                     'darwin' : { 'config': Path.jn( USER_HOME, 'Library', 'Preferences', self.name ),
                                  'data'  : Path.jn( USER_HOME, 'Library', self.name ),
                                  'launch': Path.jn( USER_HOME, 'Applications' ),
                                  'cache' : Path.jn( USER_HOME, 'Library', self.name, '.cache' )},
                     'linux'  : { 'config': Path.jn( USER_HOME, '.config', self.name ),
                                  'data'  : Path.jn( USER_HOME, '.local', 'share', self.name ),
                                  'launch': Path.jn( USER_HOME, '.local', 'share', 'applications' ),
                                  'cache' : Path.jn( USER_HOME, '.cache', self.name )},
                     'windows': { 'config': Path.jn( 'Users', USER, 'AppData', 'Local', self.name ),
                                  'data'  : Path.jn( 'Users', USER, self.name ),
                                  'launch': Path.jn( 'Users', USER, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs' ),
                                  'cache' : Path.jn( 'Users', USER, 'AppData', 'Local', self.name, 'cache' )}}

        for arg in args:
            if arg in ( 'cache', 'data', 'config', 'launch' ):
                if self.__test__:
                    if as_tuple:
                        R.append( tuple( Path.split( APP_DATA['_TMP_'][arg] )))
                    else:
                        R.append( APP_DATA['_TMP_'][arg] )
                else:
                    if as_tuple:
                        R.append( tuple( Path.split( APP_DATA[OS][arg] )))
                    else:
                        R.append( APP_DATA[OS][arg] )
            elif arg in ( 'home', 'userhome' ):
                if self.__test__:
                    if as_tuple:
                        R.append( tuple( Path.split( _AU_TMP_DIR_ )))
                    else:
                        R.append( _AU_TMP_DIR_ )
                else:
                    if as_tuple:
                        R.append( tuple( Path.split( USER_HOME )))
                    else:
                        R.append( USER_HOME )
            elif arg in ( 'username', 'user' ):
                R.append( USER )
            elif arg in ( 'os', 'system' ):
                R.append( OS )
            else:
                raise ValueError(f"Invalid argument - '{arg}'")

        if len(R) == 0:
            raise ValueError("No arguments provided for AppData.sysdata")
        elif len(R) == 1:
            return R[0]
        else:
            return tuple(R)

