# Date and Path imports
from .._constants import getLogger

class __DateImports__:
    from datetime import ( datetime as _dt,
                           timedelta as _td )

    def __init__(self):
        self.parse = self.__parser__()

    def __call__(self, *args, **kwargs):
        """
        Use date functions
          kwargs:
            'date'    : assign date otherwise date is set to now
                         - must be a datetime object
            'strftime': datetime.strftime()
            'strptime': datetime.strptime()
            'parse'   : parse a date with dateutil.parser
                         - ignored if 'date' is in kwargs
        """
        log = getLogger(__name__)
        date = self._dt.now()
        try:
            if not ( kwargs or args ):
                return date

            elif not kwargs:
                _arg = list(filter( lambda x: x != 'timestamp', args ))
                if _arg:
                    date = self.parse( _arg[0] )

            elif 'date' in kwargs:
                if isinstance( kwargs['date'], self._dt ):
                    date = kwargs['date']
                else:
                    date = self.parser( kwargs['date'] )

            elif 'strptime' in kwargs:
                assert isinstance( kwwargs['strptime']. tuple ) and len( kwargs['strptime'] ) == 2
                date = self._dt.strptime( *kwargs['strptime'] )

            elif any( i in kwargs for i in ( 'days', 'seconds' )):
                _opts = dict([( k, v ) for k, v in filter( lambda x: x[0] in ( 'days', 'seconds' ), kwargs.items() )])
                return self._td( **_opts )

            if 'strftime' in kwargs:
                return date.strftime( kwargs['strftime'] )

            elif 'timestamp' in args:
                self.ts( date )

            return date

        except Exception as E:
            log.exception(E)
            raise

    def ts(self, date = None):
        log = getLogger(__name__)
        try:
            if date and isinstance( date, self._dt ):
                return date.timestamp()
            elif isinstance( date, list|tuple ):
                date = self._dt( *date )
            elif isinstance( date, str ):
                date = self.parse( date )
            elif not date:
                date = self._dt.now()
            else:
                raise ValueError(f"Invalid argument for 'date' - '{date}'")

            return date.timestamp()

        except Exception as E:
            log.exception(E)
            raise

    def fromts(self, ts):
        assert isinstance( ts, float|int )
        return self._dt.fromtimestamp(ts)

    class __parser__:
        """
        Date.parse( timestr, parserinfo = None, **kwargs )
        ------------------------------------------------------------------------
        """
        __name__ = 'DateParser'

        def __init__(self):
            from dateutil.parser import parse
            setattr( self, '__doc__', self.__doc__ + parse.__doc__ )
        def __call__(self, *args, **kwargs):
            from dateutil.parser import parse
            return self.__parser__(parse, *args, **kwargs)
        def __repr__(self):
            return "dateutil.parser.parse"

        @staticmethod
        def __parser__(parser, *args, **kwargs):
            return parser(*args, **kwargs)

Date = __DateImports__()

class AgeInfo(Date._td):
    def __new__(cls, ctime, _from = None):
        if isinstance( ctime, Date._dt ):
            _1 = ctime.timestamp()
        elif isinstance( _from, Date._td ):
            _1 = ctime.total_seconds()
        else:
            raise TypeError("'ctime' must be a datetime or timedelta object")

        if _from != None:
            if isinstance( _from, Date._dt ):
                _2 = _from.timestamp()
            elif isinstance( _from, Date._td ):
                _2 = _from.total_seconds()
            else:
                raise TypeError("'_from' must be a datetime or timedelta object")
        else:
            _2 = Date._dt.now().timestamp()

        return super().__new__( cls, seconds = _2 - _1 )

    def __init__(self, ctime, _from = None):
        if isinstance( ctime, Date._dt ):
            self.created = ctime.timestamp()
        elif isinstance( _from, Date._td ):
            self.created = ctime.total_seconds()

        if _from != None:
            if isinstance( _from, Date._dt ):
                self._from = _from.timestamp()
            elif isinstance( _from, Date._td ):
                self._from = _from.total_seconds()

        setattr( self, '__doc__', "Age data" )
        super().__init__()

    def __getr__(self):
        if self._from:
            s = self.total_seconds()
            n = None
        else:
            s = ( Date() - self.created ).total_seconds()
            n = s

        yrs = self.years(n)
        # print(f"{yrs = }")

        if yrs >= 3 - ( 1/24 ):
            return f"{int(round(yrs))} years"

        if yrs >= .95:
            s = s - int(yrs) * (( 3600*24 ) * ((( 365*4 ) +1 ) /4 ))
            mts = self.months(s)
            M = int(round( mnts ))
            M = f"1 month" if M == 1 else f"{M} months"
            return f"1 year, {M}" if int(yrs) == 1 else f"{yrs} years, {M}"

        mts = self.months()
        # print(f"{mts = }")
        if mts >= 6 - (1/ ( 4.345*6 )):
            return f"1 month" if int(round(mts)) == 1 else f"{int(round(mts))} months"

        wks = self.weeks()
        # print(f"{wks = }")
        if wks >= 1:
            s = s - ( int(wks) * (( 3600*24 ) * 7 ))
            dys = self.days(s)
            D = f"1 day" if round(dys) == 1 else f"{int(round(dys))} days"
            return f"1 week, {D}" if int(wks) == 1 else f"{int(wks)} weeks, {D}"

        dys = int(self.days())
        # print(f"{dys = }")
        if dys >= 2:
            s = s - ( dys * ( 3600*24 ))
            hrs = self.hours(s)
            hrs = int(round(hrs))
            if not hrs:
                return f"{dys} days"
            return f"{dys} days, 1 hour" if hrs == 1 else f"{dys} days, {hrs} hours"

        hrs = int(self.hours())
        # print(f"{hrs = }")
        if hrs >= 1:
            H = f"1 hour, " if hrs == 1 else f"{H} hours, "
            s = s - ( hrs * 3600 )
            mn = int(self.minutes(s))
        else:
            H = ''
            mn = int(self.minutes())

        # print(f"{mn = }")
        if mn >= 1:
            s = int( s - ( mn * 60 ))
            S = f"1 second" if s == 1 else f"{s} seconds"
            return f"{H}1 minute, {S}" if mn == 1 else f"{H}{mn} minutes, {S}"

        return f"1 second" if int(s) == 1 else f"{int(s)} seconds"

    def years( self, n = None ):
        if not isinstance( n, int|float ):
            n = self.total_seconds()
        return round( n / (( 3600*24 ) * ((( 365*4 ) +1 ) /4 )  ), 12 )

    def months( self, n = None ):
        if not isinstance( n, int|float ):
            n = self.total_seconds()
        return round( n / (( 3600*24 ) * ( 365 / 12 )), 12 )

    def weeks( self, n = None ):
        if not isinstance( n, int|float ):
            n = self.total_seconds()
        return round( n / (( 3600*24 ) * 7 ), 12 )

    def days( self, n = None ):
        if not isinstance( n, int|float ):
            n = self.total_seconds()
        return round( n / ( 3600*24 ), 12 )

    def hours( self, n = None ):
        if not isinstance( n, int|float ):
            n = self.total_seconds()
        return n / 3600

    def minutes( self, n = None ):
        if not isinstance( n, int|float ):
            n = self.total_seconds()
        return n / 60

    def __str__(self):
        return self.__getr__()
    def __float__(self):
        if self._from:
            return self.total_seconds()
        data = dt.now().timestamp() - self
        return data.total_seconds()
    def __int__(self):
        if self._from:
            return int(round(self.total_seconds))
        data = dt.now().timestamp() - self
        return int(round(data.total_seconds))
    def __repr__(self):
        return f"(< AgeInfo: {self.__getr__()} >)"

class PathInfo(type):
    class DateInfo(Date._dt):
        def __new__( cls, name, date, doc ):
            return super().__new__( cls, *tuple(date.timetuple())[:7] )
        def __init__( self, name, date, doc ):
            setattr( self, '__doc__', doc )
            setattr( self, '__name__', name )
            super().__init__()
        def __str__(self):
            return self.strftime('%B, %A %_e, %Y - %I:%M%P')
        def __repr__(self):
            return f"DateInfo{tuple(self.timetuple())}"

    class SizeInfo(int):
        __types__ = (( 'kbit', 'Bit' ), ( 'n', 'Nibble' ), ( 'kb',  'Kilobit'  ), ( 'Kb',  'Kibibit'  ),
                     ( 'kB',  'Kilobyte' ), ( 'KiB', 'Kibibyte' ), ( 'Mb',  'Megabit'  ), ( 'Mib', 'Mebibit'  ),
                     ( 'MB',  'Megabyte' ), ( 'MiB', 'Mebibyte' ), ( 'Gb',  'Gigabit'  ), ( 'Gib', 'Gibibit'  ),
                     ( 'GB',  'Gigabyte' ), ( 'GiB', 'Gibibyte' ), ( 'Tb',  'Terabit'  ), ( 'Tib', 'Tebibit'  ),
                     ( 'TB',  'Terabyte' ), ( 'TiB', 'Tebibyte' ), ( 'Pb',  'Petabit'  ), ( 'Pib', 'Pebibit'  ),
                     ( 'PB',  'Petabyte' ), ( 'PiB', 'Pebibyte' ))

        class SubSize(float):
            def __new__(cls, n, *args):
                return super().__new__(cls, n)
            def __init__(self, n, _short, _long):
                self.abbr = _short
                self.name = _long
                self.__doc__ = f"File size ({self.name}s)"
            def __str__(self):
                return f"{self.real} {self.abbr}"
            def __repr__(self):
                return f"(< SizeInfo: {self.real} {self.name} >)"

        def __new__(cls, n, rounded = 2):
            return super().__new__(cls, n)
        def __init__(self, n, rounded = 2):
            self.rounded = rounded
            setattr( self, '__doc__', f"File size (Bytes)" )
            setattr( self, '__name__', 'Size' )
            setattr( self, '_round_', rounded )
            for attr, s in (('K', 'KiB'), ('M', 'MiB'), ('G', 'GiB'), ('T', 'TiB'), ('P', 'PiB')):
                setattr( self, attr, self.__call__(s) )
            super().__init__()
        def __str__(self):
            return f"{self.real} B"
        def __repr__(self):
            return f"(< SizeInfo: {self.real} Bytes >)"
        def __call__(self, s: str = ''):
            if not s or s in ( 'B', 'Bs', 'byte', 'bytes' ):
                return cls
            import operator as op
            b = self.real * 8
            B = self.real
            types = [ (a, b) for a, b in zip( self.__types__, (( op.mul, b, 1 ), ( op.mul, b, 4 ), ( op.truediv, b, 1000 ),
                                                               ( op.truediv, b, 1024 ), ( op.truediv, B, 1000 ), ( op.truediv, B, 1024 ),
                                                               ( op.truediv, b, 1000**2 ), ( op.truediv, b, 1024**2 ), ( op.truediv, B, 1000**2 ),
                                                               ( op.truediv, B, 1024**2 ),( op.truediv, b, 1000**3 ), ( op.truediv, b, 1024**3 ),
                                                               ( op.truediv, B, 1000**3 ), ( op.truediv, B, 1024**3 ), ( op.truediv, b, 1000**4 ),
                                                               ( op.truediv, b, 1024**4 ), ( op.truediv, B, 1000**4 ), ( op.truediv, B, 1024**4 ),
                                                               ( op.truediv, b, 1000**5 ), ( op.truediv, b, 1024**5 ), ( op.truediv, B, 1000**5 ),
                                                               ( op.truediv, B, 1024**5 )))]
            for matches, ( op, _b, n ) in types:
                if s in [*[ i+'s' for i in matches ], *matches ]:
                    res = op( _b, n )
                    return self.SubSize( round( res, self._round_ ), *matches )
            raise AttributeError(f"Invalid size type")

        def help(self):
            msg = [ '',
                    "\x1b[1;37m  SizeInfo\x1b[2;37;3m - size in Bytes\x1b[0m",
                    "\x1b[3m    Get other size types with the following keywords:\x1b[0m",
                    "\x1b[2;37;3m            (keywords are case sensitive)\x1b[0m",
                    '' ]
            for s, l in self.__types__:
                msg.append( f"\x1b[38;2;204;204;0;1m        {s:>4}:\x1b[0;38;2;160;160;160;3m File size in {l}s\x1b[0m" )
            msg.append('')
            print( '\n'.join(msg) )

    class FilePermissions(type):
        __perm__ = { 1: '--x', 2: '-w-', 4: 'r--', 5: 'r-x', 6: 'rw-', 7: 'rwx' }
        def __new__(cls, path: str, mode: str):
            _int = oct(mode)[-3:]
            s = ''.join([ cls.__perm__[_i] for _i in [ int(i) for i in list(_int) ]])
            doc = '\n'.join([ f"File permission bits - '{path}'",
                              f"Octal: {_int}",
                              f"    User / Group / Other",
                              f"    {s[:3]:5}   {s[3:6]:5}   {s[6:9]}" ])
            return super().__new__( cls, 'FilePermissions', (), { '__s__': s, '__doc__': doc, '__mode__': int(_int) })
        def __init__(self, path: str, mode: str):
            pass
        def __repr__(self):
            return f"(< FilePermissions: '{self}' >)"
        def __str__(self):
            return self.__s__
        def __int__(self):
            return self.__mode__

    def __new__(cls, path: str):
        if not Path.isfile(path) and not Path.isdir(path):
            raise FileNotFoundError(f"File path doesn't exist - '{path}'")

        nm, ext = Path.splitext( Path.bn( path ))
        st = Path.stat(path)

        if Path.islink(path):
            islink = True
            realpath = Path.readlink(path)
        else:
            islink = False
            realpath = ''

        ctime = cls.DateInfo( 'ctime', Date._dt.fromtimestamp( st.st_ctime ), "File creation time" )
        age = AgeInfo( ctime )

        clsDict = { 'ext'          : ext,
                    'name'         : nm,
                    'path'         : Path.abs( path ),
                    'filetype'     : 'directory' if Path.isdir(path) else 'file',
                    'ctime'        : ctime,
                    'atime'        : cls.DateInfo( 'atime', Date._dt.fromtimestamp( st.st_atime ), "Latest file access time" ),
                    'mtime'        : cls.DateInfo( 'mtime', Date._dt.fromtimestamp( st.st_mtime ), "Last modification time" ),
                    'size'         : cls.SizeInfo( st.st_size ),
                    'permissions'  : cls.FilePermissions( path, st.st_mode ),
                    'age'          : age,
                    'islink'       : islink,
                    'realpath'     : realpath,
                    'inode'        : st.st_ino,
                    'device'       : st.st_dev,
                    'links_to_file': st.st_nlink,
                    'uid'          : st.st_uid,
                    'gid'          : st.st_gid     }

        return super().__new__( cls, 'PathInfo', (), clsDict )

    def __init__(self, path: str):
        self.__path__ = path

class Path:
    """
    File path modification tools
        - contains mostly builtins ... mostly (some aliased)
    """
    from os import ( access as __access__,
                     environ as env,
                     getcwd as pwd,
                     getlogin,
                     link as ln,
                     listdir as ls,
                     makedirs as mkdir,
                     readlink,
                     remove as rm,
                     removedirs as rmdir_R,
                     rmdir,
                     stat,
                     walk,
                     R_OK as __R_OK__,
                     W_OK as __W_OK__,
                     X_OK as __X_OK__   )
    from shutil import ( copyfile as cp,
                         copytree as cp_R,
                         move as mv     )
    from os.path import ( abspath as abs,
                          basename as bn,
                          dirname as dn,
                          exists,
                          expanduser,
                          isabs,
                          isfile,
                          isdir,
                          islink,
                          join as jn,
                          sep as pathsep,
                          splitext      )

    @classmethod
    def walklevel(path, depth = -1):
        """
        It works just like os.walk, but you can pass it a level parameter
        that indicates how deep the recursion will go.
        If depth is 1, the current directory is listed.
        If depth is 0, nothing is returned.
        If depth is -1 (or less than 0), the full depth is walked.
        """
          # If depth is negative, just walk
          # Not using yield from for python2 compat
          # and copy dirs to keep consistant behavior for depth = -1 and depth = inf

        if depth < 0:
            for root, dirs, files in cls.walk(path):
                yield root, dirs[:], files
            return
        elif depth == 0:
            return

          # path.count(os.path.sep) is safe because
          # - On Windows "\\" is never allowed in the name of a file or directory
          # - On UNIX "/" is never allowed in the name of a file or directory
          # - On MacOS a literal "/" is quietly translated to a ":" so it is still
          #   safe to count "/".
        base_depth = path.rstrip(os.path.sep).count(os.path.sep)
        for root, dirs, files in cls.walk(path):
            yield root, dirs[:], files
            cur_depth = root.count(os.path.sep)
            if base_depth + depth <= cur_depth:
                del dirs[:]

    @classmethod
    def home(cls):
        """ Return user's home directory """
        return cls.expanduser('~')

    @classmethod
    def user(cls):
        """ Return user's login name """
        return cls.getlogin()

    @classmethod
    def hasRead(cls, path):
        """ Check if path has read permissions """
        if not cls.isfile(path) or cls.isdir(path):
            raise FileNotFoundError(f"'{path}' is not a valid file path")
        return cls.__access__( path, cls.__R_OK__ )

    @classmethod
    def hasWrite(cls, path):
        """ Check if path has write permissions """
        if not cls.isfile(path) or cls.isdir(path):
            raise FileNotFoundError(f"'{path}' is not a valid file path")
        return cls.__access__( path, cls.__W_OK__ )

    @classmethod
    def hasReadWrite(cls, path):
        """ Check if path has read/write permissions """
        return bool( cls.hasWrite(path) and cls.hasRead(path) )

    @classmethod
    def isExec(cls, path):
        """ Check if file is executable """
        if not cls.isfile(path):
            raise FileNotFoundError(f"'{path}' is not a valid file")
        return cls.__access__( path, cls.__X_OK__ )

    @classmethod
    def joinchk( cls, L: list|tuple, *, relpath = False ):
        """
        def joinchk( path: str ) >>> tuple( abspath, os.path.is[dir|file]() )

          Uses os.path.join to join pathnames but includes a boolean
        signifying whether the path exists or not.

            - Returns an absolute path unless 'relpath' is True
        """
        path = cls.abspath( cls.JN( *L )) if relpath else cls.JN( *L )
        B = bool( cls.isdir(path) or cls.isfile(path) )
        return ( path, B )

    @classmethod
    def split( cls, path: str ):
        """
        def split( path: str ) >>> tuple()

            Splits path and returns a tuple of path names. Includes
          the path separator as the first index if the path is an
          absolute path.
        """
        while path.endswith( cls.pathsep ):
            path = path[:-1]

        if cls.isabs(path):
            return [ cls.pathsep ] + path.split( cls.pathsep )[1:]
        else:
            return path.split( cls.pathsep )

    @classmethod
    def info(cls, path: str):
        """
        Returns a type object 'PathInfo' that includes stat data and more
        """
        if not cls.exists( path ):
            raise FileNotFoundError(f"Path doesn't exist - '{path}'")
        return PathInfo(path)

__all__ = [ 'Date',
            'Path' ]
