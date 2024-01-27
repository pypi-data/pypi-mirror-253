import os, json
from functools import wraps, update_wrapper
from importlib.resources import files as _src
from hashlib import md5


from apputils.tools import uniqueName, isSafeAttribName
from apputils.appdata import AppData
from apputils._import import Path

from ._constants import PROJECT_APP_NAME, getLogger
from . import _data
from .ansitools import Ansi, AnsiList

# Extended Methods  ------------------------------------------------------------
#
#   # Extra color/style tools
#

from .types import FG_Color, BG_Color, Style

@classmethod
def get_file_hash(cls, path):
    # log = getLogger(__name__)
    # try:
    with open( path, 'rb' ) as f:
        H = md5( f.read() ).digest()
    return H
    # except Exception as E:
    #     log.exception(E)
    #     raise

@classmethod
def _hasColorValues_(cls, d):
    vals = (( 'name', str ), ('rgb', list|tuple), ('code', str ))
    return bool( isinstance( d, dict ) and all( i[0] in d and isinstance( d[i[0]], i[1] ) for i in vals ))

@classmethod
def _hasStyleValues_(cls, d):
    vals = (('name', str), ('ansi', list|tuple), ('code', str), ('html', list|tuple))
    return bool( isinstance( d, dict ) and all( i[0] in d and isinstance( d[i[0]], i[1] ) for i in vals ))

@classmethod
def _sort_(cls, D):
    _D = dict(sorted( D.items(), key = lambda x: ( x[0].split()[-1],
                                                   len(x[0].split()),
                                                   x[0] )))
    for k in _D:
        _D[k] = dict(sorted( _D[k].items(), key = lambda x: x[0] ))
    return _D

#
#
#   END Extended Methods
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# UserColors -------------------------------------------------------------------
#   Imported by texttools._escapes.AnsiEscapeDict
#
#

class _UserColors_(dict):
    """ User color data """

    _get_file_hash_ = get_file_hash
    _path_ = AppData(PROJECT_APP_NAME).appdir( 'data', 'configuration', file = 'user_colors.json' )
    with open( _src(_data).joinpath( 'user_color_template.json' ), 'r' ) as f:
        _t = json.load(f)
    template = type( '_usr_temp_', (), { 'sample': dict([ _t[0] ]),
                                         'sort'  : dict([ _t[1] ]) })()
    del _t
    sort = _sort_
    _sort_keys_ = False
    hasColorValues = _hasColorValues_
    __hash_path__ = AppData(PROJECT_APP_NAME).appdir( 'cache', file = '699ce156-710a-46fc-b496-34f6019ad6df' )
    _cache_ = AppData(PROJECT_APP_NAME).appdir( 'cache', file = '0fc4e511-90b5-4a65-8d84-23ee9ec34251' )

    def __init__(self):
        log = getLogger(__name__)
        fromCache = False
        data = {}
        dict.__init__(self)

        try:
            with open( self.__hash_path__, 'rb' ) as f:
                saved_hash = f.read()
        except FileNotFoundError:
            log.warning("Cache hash file for user colors not found")
            saved_hash = 0
        except Exception as E:
            log.exception(E)
            log.warning(f"Failed to get hash from AnsiDict cache files")
            saved_hash = 0

        if self.hashMatches( saved_hash ):
            try:
                with open( self._cache_, 'rb' ) as f:
                    _data = pickle.load(f)
                data = _data
                fromCache = True
                log.debug("Loaded user color configuration from cache")
            except FileNotFoundError:
                log.warning("Cache file for user colors not found")
                pass
            except Exception as E:
                log.exception("Error loading data from cache")
        else:
            log.info("Detected changes to user color configuration file - reloading")

        if not data:
            try:
                data = self.load()
            except json.JSONDecodeError:
                log.error("Corrupted user color json file - backing up and creating a new template")
                moveto = Path.jn( Path.dn( self._path_ ), f"colors_CORRUPTED.json" )
                Path.mv( self._path_, moveto )
                data = {}
            except FileNotFoundError:
                log.info(f"User color list not found - installing template")
                data = {}
            except Exception as E:
                log.exception(E)
                raise

        self.update( **data )
        if not fromCache:
            self.save()

    def load(self):
        log = getLogger(__name__)
        data = {}
        bad_data = {}
        def templateKeys(_dict):
            sample = list(filter( lambda x: x[0].startswith('__SAMPLE__'),
                                  [ k for k, v in _dict.items() ]))
            sort = list(filter( lambda x: x[0].startswith('__SORT_KEYS__'),
                                [ k for k, v in _dict.items() ]))
            sample = None if not sample else sample[0]
            sort = None if not sort else sort[0]
            return sample, sort

        with open( self._path_, 'r', encoding = 'utf-8' ) as f:
            _d = json.load(f)

        sample, sort = templateKeys(_d)
        if sample:
            _d.pop( sample )
        if sort:
            if sort['__SORT_KEYS__']['value']:
                self._sort_keys_ = True
                self.template.sort['value'] = True
            _d.pop( sort )

        for k, v in _d.items():
            if any( k.startswith(i) for i in ( '__SORT_KEYS__', '__SAMPLE__' )):
                continue

            R = self._color_check_( **{ k: v })
            data = { **data, **R['data'] }
            bad_data = { **bad_data, **R['bad_data'] }

        if bad_data:
            path = Path.jn( Path.dn( self._path_ ), 'bad-colors.json' )
            if Path.isfile( path ):
                try:
                    with open( path, 'r' ) as f:
                        bad_data = { **json.load(f), **bad_data }
                except:
                    log.error(f"Error reading existing 'bad_data' color config file")
                    fn, ext = Path.splitext( path )
                    moveto = uniqueName( f"{fn}_CORRUPT.json" )
                    Path.mv( path, moveto )
                    log.warning(f"Backed up corrupted user color file to '{moveto}'")

            with open( path, 'w' ) as f:
                json.dump( bad_data, f, indent = '  ' )

            log.warning(f"Saved json of bad colors to '{path}'")

        return data

    def _color_check_(self, **d):
        log = getLogger(__name__)
        bad_data, data = {}, {}
        for k, v in d.items():
            if not self.hasColorValues(v):
                log.error(f"User color '{k}' is missing needed color values")
                bad_data[k] == v
            if not isSafeAttribName( v['code'] ):
                log.error(f"User color '{k}' has an invalid value 'code': '{v['code']}' - must be a valid attribute name")
                bad_data[k] == v
            if not isSafeAttribName( v['name'] ):
                log.error(f"User color '{k}' has an invalid value 'name': '{v['name']}' - must be a valid attribute name")
                bad_data[k] == v
            if len(v['rgb']) != 3 or any( i > 255 or i < 0 for i in v['rgb'] ):
                log.error(f"Invalid RGB value for color '{k}' - must be 3 values and all >= 0 and <= 255")
                bad_data[k] == v

            if k not in bad_data:
                data[k] = v
                log.info(f"Added user color '{k}' - ( 'name': {repr(v['name'])}, 'code': {repr(v['code'])}, 'rgb': {v['rgb']} )")

        log.debug(f"Valid color(s): {tuple(data)}")
        if bad_data:
            log.warning(f"Invalid color(s): {tuple(bad_data)}")
        return { 'data': data, 'bad_data': bad_data }

    def addColor(self, name, data):
        log = getLogger(__name__)
        if name in self:
            log.error(f"Color '{name}' already exists!")
            return

        R = self._color_check_( name = data )
        if R['data']:
            self.update( name = data )
            self.save()
        else:
            log.warning(f"Could not add color '{name}'")

    def addColors(self, **data):
        log = getLogger(__name__)
        _data = {}
        for k, v in data.items():
            if k in self:
                log.error(f"Color '{name}' already exists!")
                continue
            _data = { **_data, **self._color_check_( k = v )['data'] }

        if not _data:
            log.error(f"Nothing to add")
        else:
            self.update(**_data)
            self.save()

    def __setitem__(self, name, item):
        return self.addColor( name, item )

    def __delitem__(self, name):
        return self.removeColor(name)

    def pop(self, name):
        return self.removeColor(name)

    def removeColor(self, name):
        log = getLogger(__name__)
        if not name in self:
            log.error(f"Color '{name}' not found in user colors")
            return None
        R = super().pop(name)
        self.save()
        return { name: R }

    def save(self):
        log = getLogger(__name__)
        data = self.copy()
        if self._sort_keys_:
            self.clear()
            self.update( **self.sort( data ))
            self.update( **data )

        data = { **self.template.sample,
                 **self,
                 **self.template.sort }

        try:
            with open( self._path_, 'w', encoding = 'utf-8' ) as f:
                json.dump( data, f, indent = '  ' )
            log.info(f"User colors updated and saved to '{self._path_}'")
            self._save_hash()

        except Exception as E:
            log.exception(E)
            raise

    def hashMatches(self, other):
        log = getLogger(__name__)
        try:
            _hash = self._get_hash()
            log.debug(f"file-hash: {str(_hash):>25}")
            log.debug(f"saved-hash: {str(other):>25}")
        except:
            return False
        return bool( other == _hash )

    def _get_hash(self):
        return self._get_file_hash_( self._path_ )

    def _save_hash(self):
        log = getLogger(__name__)
        _hash = self._get_hash()
        with open( self.__hash_path__, 'wb' ) as f:
            f.write( self._get_hash() )
        log.debug(f"Saved cache hash for user colors")

#   END UserColors
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ------------------------------------------------------------------------------
#

@classmethod
def _color_help( cls, *colors, get_list = False, attributes_only = False, __ALL__ = {} ):
    grB = '\x1b[0;38;2;210;210;200;1m'
    cI  = '\x1b[0;38;2;0;255;255;3m'
    gdI = '\x1b[0;38;2;0;255;255;3m'
    ppl = '\x1b[0;38;2;102;0;204m'
    gr  = '\x1b[0;38;2;224;224;224m'
    Gr  = '\x1b[0;38;2;160;160;160m'
    g   = '\x1b[0;38;2;102;255;102m'
    cg  = '\x1b[0;38;2;61;255;163m'
    _   = '\x1b[0m'

    R = AnsiList([ '  \x1b[1;38;2;240;240;240;4mColors:\x1b[0m' ], strsep = '\n' )
    colors = [ i.lower().replace('_',' ') for i in colors ]

    if colors and attributes_only:
        R += [ '\x1b[0;38;2;210;210;200;1m    Attributes:', '\x1b[0m' ]

    elif attributes_only:
        R += [ '\x1b[0;38;2;210;210;200;1m    Attributes:', '\x1b[0m' ]

    elif colors:
        R += [ '' ]

    else:
        R += [ '',
               f"{cI}    Attributes can be 'stacked' using the BITAND '&' to create an AnsiCombo",
               f'      Example:',
               f'{Gr}        FG{gr}.{Gr}white{g} &{Gr} BG{gr}.{Gr}charcoal{g} &{Gr} S{gr}.{Gr}Bold{_}',
               '', f'{cI}      You can only have a Reset object at the beginning of an AnsiCombo',
               f'{Gr}        S{gr}.{Gr}_{g} &{Gr} FG{gr}.{Gr}red',
               '', f"{cI}      Only one of each color type or Style type is accepted when combining. If 2",
               f"    or more objects of the same type are detected, a ValueError will be raised. If a Reset",
               f"    object is added anywhere except the beginning of the combo, a TypeError is raised",
               '', f"{cg}      NOTE:{cI} all color groups share a Reset ('\\x1b[0m') object{_}",
               '', f'\x1b[0;38;2;210;210;200;1m  Colors in class:', f"{_}" ]

    for k, v in __ALL__.items():
        if k == 'reset' or ( colors and k.lower() not in colors ):
            continue

        rgb = tuple(v.__esc__[-3:])
        T = f"{k.title().replace('_',' '):<18}█▅▀█▅▀█▅▀█▅▀█"

        if any( k.startswith(i) for i in ( 'fg_black', 'bg_black', 'fg_white', 'bg_white', 'black', 'white' )):
            col = f""
            R += [ f"\x1b[38;2;255;255;0;1m>      \x1b[48;2;80;80;80;38;2;{';'.join([ str(i) for i in rgb ])};1m{T}\x1b[3m      \x1b[0m" ]
        else:
            R += [ f"\x1b[38;2;255;255;0;1m>      \x1b[38;2;{';'.join([ str(i) for i in rgb ])};1m{T} " ]

        if attributes_only:
            R[-1] += f"...\x1b[0;38;2;160;160;160;1m {v['code']}\x1b[0m"

        else:
            R += [ f"\x1b[0;38;2;204;204;0m        {'Attribute Name:':<18}\x1b[38;2;160;160;160;1m{v.__code__}\x1b[0;38;2;204;204;0;1m|\x1b[38;2;160;160;160;1m{k}\x1b[0m",
                   f"\x1b[0;38;2;204;204;0m        {'RGB:':<18}\x1b[38;2;160;160;160;1m( {', '.join([str(i) for i in rgb ])} )\x1b[0m",
                   f"\x1b[0;38;2;204;204;0m        {'Hexidecimal:':<18}\x1b[38;2;160;160;160;1m{'#%02x%02x%02x'%rgb }\x1b[0m",
                   ""   ]

    if get_list:
        return R
    else:
        print(R)

@classmethod
def _style_help( cls, *, get_list = False, __ALL__ = {} ):
    R = AnsiList([ '  \x1b[1;38;2;240;240;240;4mText Styles:\x1b[0m', '', ], strsep = '\n' )
    for k, v in __ALL__.items():
        doc = '    '+v.__doc__.strip().replace('\n','\n        ')
        R += [ f"\x1b[38;2;255;255;0;1m>\x1b[38;2;121;173;255;1m     {k.title().replace('_',' ')}:\x1b[0m",
               f"    \x1b[38;2;0;255;255;3m{doc}", '\x1b[0m',
               f"\x1b[38;2;204;204;0m        {'Attribute Name:':<18}\x1b[38;2;160;160;160;1m{v.__code__}\x1b[0;38;2;204;204;0;1m|\x1b[38;2;160;160;160m{k}\x1b[0m",
               f"\x1b[38;2;204;204;0m        {'Ansi Code:':<18}\x1b[38;2;160;160;160;1m{repr(v.__esc__)}\x1b[0m",
               ""   ]

    if get_list:
        return R
    else:
        print( '\n'.join(R) )
