from threading import Lock
from ._constants import getLogger

class _custom_colors_(type):
    def __new__(cls):
        return type.__new__( cls, '_custom_colors_', (object,), { '_new_'  : lambda x = (), y = {}: cls._new_( cls, *x, **y ),
                                                                  '_codes_': {},
                                                                  '_data_' : {},
                                                                  '_dict_' : {},
                                                                  '_cache_': '',
                                                                  'lock'   : Lock(),
                                                                  })
    def __init__(self):
        super().__init__(self)

    def __call__(self, *args, rgb = (), name = '', code = '', prefix = (), comment = '', **kwargs ):
        log = getLogger(__name__)

        if '__SKIP_CACHE__' not in args and not self._cache_:
            self._init_()

        if name:
            try:
                R = getattr( self, name )
                return R
            except AttributeError:
                log.debug(f"Name '{name}' not found in colors = creating new")
                pass

        try:
            if not ( isinstance( rgb, list|tuple ) and len(rgb) == 3 and all( i in range(256) for i in rgb )):
                raise ValueError(f"Invalid rgb data '{rgb}' - must be a list|tuple of 3 integers 0-255")

        except Exception as E:
            log.exception(E)
            raise

        return_bg = False
        try:
            assert name
            _name = name
            name = _fix_name_( name )
        except:
            if name:
                log.warning(f"Invalid name for attribute name - '{name}' - renameing to 'rgb_color_{'_'.join(rgb)}'")
            name = f"rgb_color_{'_'.join([ str(i) for i in rgb ])}"
            _name = f"RGB Color: ({', '.join([ str(i) for i in rgb ])})"

        hasCode = False
        try:
            assert code
            code = self._fix_name_( code ).replace(' ','_').lower()
            hasCode = True
        except:
            if code:
                log.warning(f"Invalid code for attribute name - '{code}' - renaming to '{'c_'+'_'.join(rgb)}'")
            code = 'c_'+'_'.join([ str(i) for i in rgb ])

        if prefix and prefix not in ( (38,2), (48,2) ):
            log.error(f"Invalid value for 'prefix' - '{prefix}'")

        elif prefix == (48,2) or any( name.lower().find(i) >= 0 for i in ('bg_','bg ','_bg',' bg', '(bg)') ):
            log.debug("Returning background color")
            return_bg = True

        if not comment:
            comment = f"Custom color: {name} {rgb}",

        prefix = (38,2)
        data = { 'code': code,
                 'name': name,
                 '_name': _name,
                 'clsName': _name,
                 'prefix': prefix,
                 'rgb': rgb,
                 'comment': comment }

        self._dict_[_name] = data.copy()
        self._save_cache_()

        try:
            import texttools.types
            # _name = name.replace(' ','_').lower()
            self._data_[name] = texttools.types.AnsiColor( **data )
            self._data_['bg_'+name] = texttools.types.AnsiColor( **{ **data, 'prefix': (48,2) } )
            if hasCode:
                if hasCode in self._data_:
                    log.warning(f"Overwriting existing attribute '{data['code']}'!")
                self._data_[code] = self._data_[_name]
                self._data_['bg_'+code] = self._data_['bg_'+_name]

            if '_FG_' in kwargs:
                setattr( kwargs['_FG_'], name, self._data_[name] )
                if hasCode:
                    setattr( kwargs['_FG_'], code, self._data_[name] )
            if '_BG_' in kwargs:
                setattr( kwargs['_BG_'], name, self._data_['bg_'+name] )
                if hasCode:
                    setattr( kwargs['_BG_'], code, self._data_['bg_'+name] )

            if return_bg:
                return self._data_['bg_'+name]
            return self._data_[name]

        except Exception as E:
            log.exception(E)
            raise

    def _init_(self):
        log = __getLogger__(__name__)

        from apputils import AppData, Path
        self._cache_ = AppData('PyDev').appdir('cache', file = '.pydev_customcolors')

        if Path.isfile( self._cache_ ):
            try:
                with self.lock:
                    with open( self._cache_, 'r' ) as f:
                        data = json.load( f.read() )
                    self._dict_ = { **data['_dict_'], **self._dict_ }
            except FileNotFoundError:
                pass
            except Exception as E:
                log.exception
            else:
                with self.lock:
                    with open( self._cache_, 'w' ) as f:
                        f.truncate()

        if self._dict_:
            for name, D in self._dict_.items():
                if name not in self._data_:
                    with self.lock:
                        self._data_[name] = AnsiColor( **D )
                        self._data_['bg_'+name] = AnsiColor( **{ **D, 'prefix': (48,2) })
                        self._data_[D['code']] = self._data_[name]
                        self._data_['bg_'+D['code']] = self._data_['bg_'+name]

        atexit.register( self.__exit )

    def __exit(self):
        from apputils import Path
        with self.lock:
            if Path.isfile( self._cache_ ):
                with open( self._cache_, 'w' ) as f:
                    f.truncate()

    def _save_cache_(self):
        with self.lock:
            with open( self._cache_, 'w' ) as f:
                json.dump( self._dict_, f, separators = (',',':') )

    def _fix_name_(self, name):
        name = ''.join( re.findall( '[A-Za-z0-9_ ]', str( name ) ))
        while name and name[0].isnumeric():
            name = name[1:]
        if not name:
            raise NameError(f"Can't create a valid attribute name from '{data['name']}'")
        return name

    def __getattribute__(self, name):
        try:
            return self._data_[name.replace(' ','_').lower()]
        except:
            return object.__getattribute__( self, name )
