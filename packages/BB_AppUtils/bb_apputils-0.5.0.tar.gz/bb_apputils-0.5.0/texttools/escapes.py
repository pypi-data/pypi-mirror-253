import re, json, pickle
from functools import wraps
from importlib.resources import files as _src
from hashlib import md5

from apputils.tools import matchSimilar, listFlatten, isSafeAttribName
from apputils import AppData
from apputils import Path
from ._constants import ( RE_RGB_ESCAPE,
                          RE_16COLOR_ESCAPE,
                          RE_STYLE_ESCAPE,
                          PROJECT_APP_NAME,
                          getLogger     )
from .ansitools import Ansi
from .types import AnsiColor, AnsiStyle, AnsiEscape, BG_Color, FG_Color, Style
from . import _data

class AnsiEscapeDict(dict):
    """ Dictionary for ansi escape codes """

    from ._esc_ext import ( _UserColors_,
                            get_file_hash as _get_file_hash_,
                            _hasColorValues_ as hasColorValues,
                            _hasStyleValues_ as hasStyleValues,
                            _sort_ as sort )

    _cache_ = AppData(PROJECT_APP_NAME).appdir( 'cache', file = "2507fe48-986e-43af-9afb-ee39929bc8a1" )

    __color_path__   = _src(_data).joinpath( 'colors.json' )
    __color16_path__ = _src( _data ).joinpath( '16colors.json' )
    __style_path__   = _src(_data).joinpath( 'styles.json' )
    __user_path__    = _UserColors_._path_
    __hash_path__    = AppData(PROJECT_APP_NAME).appdir( 'cache', file = "b3147e38-ff03-470a-b648-fdd60bfa3d08" )

    def __init__(self, *, rebuild_cache = False):
        log = getLogger(__name__)
        fromCache = False
        dict.__init__(self)
        data = {}
        try:
            with open( self.__hash_path__, 'rb' ) as f:
                saved_hash = f.read()
        except FileNotFoundError:
            saved_hash = 0
        except Exception as E:
            log.exception(E)
            log.warning(f"Failed to get hash from AnsiDict cache files")
            saved_hash = 0

        if not self.hashMatches( saved_hash ):
            log.info(f"Detected changes in configuration files - re-building escape dictionary")
        elif not rebuild_cache:
            try:
                with open( self._cache_, 'rb' ) as f:
                    _data = pickle.load(f)
                data = _data
                log.debug("Loaded escape dictionary from cache")
                fromCache = True
            except FileNotFoundError:
                log.debug("Cache file not found for AnsiEscapeDict")
            except Exception as E:
                log.exception("Error loading escape dictionary from cache")

        if not data:
            data = { 'colors': {},
                     'styles': {},
                     'colors16': {} }

            with open( self.__style_path__, 'r', encoding = 'utf-8' ) as f:
                _styles = self.sort( json.load(f) )
            for k, v in _styles.items():
                v['ansi'] = tuple(v['ansi'])
            data['styles'] = self.sort( _styles )

            with open( self.__color_path__, 'r', encoding = 'utf-8' ) as f:
                _colors = json.load(f)

            _colors = { **_colors, **self._UserColors_() }

            for k, v in _colors.items():
                v['rgb'] = tuple(v['rgb'])
            data['colors'] = self.sort( _colors )


            with open( self.__color16_path__, 'r', encoding = 'utf-8' ) as f:
                data['colors16'] = json.load(f)

            log.debug("Built escape dictionary from config files")

        self.update( **data )

        if not fromCache:
            self._save_hash()
            with open( self._cache_, 'wb' ) as f:
                pickle.dump( self, f )
            log.debug(f"Created escape dictionary cache")

    def hashMatches(self, other):
        try:
            _hash = self._get_hash()
        except:
            return False
        return bool( other == _hash )

    def _get_hash(self):
        return b''.join([ self._get_file_hash_( self.__color_path__ ),
                          self._get_file_hash_( self.__style_path__ ),
                          self._get_file_hash_( self.__user_path__ ),
                          self._get_file_hash_( self.__color16_path__ )])

    def _save_hash(self):
        log = getLogger(__name__)
        with open( self.__hash_path__, 'wb' ) as f:
            f.write( self._get_hash() )
        log.debug("Saved cache hash for system colors")

class _Escapes_(dict):
    def __init__(self, data, prefix = ()):
        d = {}
        if not prefix:
            func = AnsiStyle
            prefix = {}
        else:
            func = AnsiColor
            prefix = { 'prefix': prefix }

        for k, v in data.items():
            d[ v['name'] ] = func( **v, **prefix )
            setattr( d[ v['name'] ], '_dict_', v )

        dict.__init__(self)
        self.update( **d )

class _FG_Colors_( _Escapes_ ):
    """
    Foreground colors with added attributes
    """
    _data_   = AnsiEscapeDict()['colors']
    _prefix_ = (38,2)
    from ._esc_ext import _color_help

    def __init__(self):
        super().__init__( self._data_, self._prefix_ )

    def help(self, *colors, get_list = False, attributes_only = False):
        return self._color_help( *colors,
                                 get_list = get_list,
                                 attributes_only = attributes_only,
                                 __ALL__ = self )

class _BG_Colors_( _Escapes_ ):
    """
    Background colors with added attributes
    """
    _prefix_ = (48,2)
    from ._esc_ext import _color_help

    def __init__(self):
        _data = AnsiEscapeDict()['colors']
        data = {}
        for k, v in _data.items():
            data[f"BG {k}"] = { 'code': v['code'],
                                'comment': v['comment'].replace(k, f"BG {k}"),
                                'name': f"bg_{v['name']}",
                                'rgb': v['rgb'] }

        super().__init__( data, self._prefix_ )

    def help(self, *colors, get_list = False, attributes_only = False):
        return self._color_help( *colors,
                                 get_list = get_list,
                                 attributes_only = attributes_only,
                                 __ALL__ = self )

class _Styles_( _Escapes_ ):
    _data_ = AnsiEscapeDict()['styles']
    from ._esc_ext import _style_help

    def __init__(self):
        super().__init__( self._data_ )

    def help( self, *, get_list = False ):
        return self._style_help( get_list = get_list,
                                 __ALL__ = self )

class EscapeGroup:
    __pre__ = ()
    _data_ = {}

    def __init__(self, D, *, prefix= ()):
        log = getLogger(__name__)
        if hasattr( D, 'help' ):
            setattr( self, 'help', D.help )

        data = {}
        self.__pre__ = prefix
        for k, v in D.items():
            if not isinstance( v, AnsiEscape ):
                log.debug(f"Skipping non escape __dict__ item '{v}'")
                continue

            data[k] = v
            setattr( self, k.replace('bg_',''), v )
            setattr( self, v.__code__, v )

        self._data_ = tuple(data.items())

    def _allnames_(self):
        names = dict([( i, dict(self._data_)['reset'] ) for i in [ 'reset', 'Reset', 'RESET', '' ]])
        for k, v in self.items():
            if self.__pre__ == (38,2) and isinstance( v, FG_Color ):
                for i in ( k, f"FG {v.name[:-5]}", k.replace('_',' ').title(), k.replace('_',' ') ):
                    names[i] = v
            elif self.__pre__ == (48,2) and isinstance( v, BG_Color ):
                for i in ( k, f"BG {v.name[:-5]}", k.replace('_',' ').title(), k.replace('_',' ') ):
                    names[i] = v
            elif not self.__pre__ and isinstance( v, Style ):
                for i in ( k, k.replace('remove','rm'), k.replace('_',' ').title(), k.replace('remove','rm').replace('_',' ').title() ):
                    names[i] = v

        return names

    def items(self):
        D = {}
        for k, v in self._data_:
            if self.__pre__ == (38,2) and isinstance( v, FG_Color ):
                D[k] = v
            elif self.__pre__ == (48,2) and isinstance( v, BG_Color ):
                D[k] = v
            elif not self.__pre__ and isinstance( v, Style ):
                D[k] = v
        return D.items()

    def values(self):
        return [ i[1] for i in self.items() ]

    def names(self):
        return [ i[0] for i in self.items() ]

    def codes(self):
        return [ i[1].__code__ for i in self.items() ]

class Escapes:
    __dict__ = {}

    def __init__(self):
        _fg = _FG_Colors_()
        _bg = _BG_Colors_()
        _s  = _Styles_()

        _d = AnsiEscapeDict()
        self.StyleDict = _d['styles']
        self.ColorDict = _d['colors']
        self.ColorDict16 = _d['colors16']

        _fg['reset'] = _bg['reset'] = _s['reset']
        self.FG_Colors = EscapeGroup( _fg, prefix = (38,2) )
        self.BG_Colors = EscapeGroup( _bg, prefix = (48,2) )
        self.Styles = EscapeGroup( _s )
