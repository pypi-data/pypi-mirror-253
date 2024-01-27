# BB_AppUtils

> Utilities for developing python applications/scripts

> README is incomplete!

## Contents

- [Shell Script 'apputils'](#shell-script) - terminal commands

- [AppUtils](#apputils)
    - package of handy functions and tools
    - [AppData](#appdata) - tools for using system directories
    - Classes
        - AgeInfo - class to make readable strings from timedelta objects
        - [AppData](#appdata) - application directories tool
        - [Date](#date) - Date imports with added functions
        - [Path](#path) - os.path imports with added functions
    - Functions
        - [appendFile](#appendfile)
        - [attribNameFromString](#attribnamefromstring)
        - [filterList](#filterlist)
        - [filter_dir](#filter_dir)
        - [getBoolFromString](#getboolfromstring)
        - [getIndexed](#getindexed)
        - [isBinary](#isbinary)
        - [isSafeAttribName](#issafeattribname)
        - [listDepth](#listdepth)
        - [listFlatten](#listflatten)
        - [matchSimilar](#matchsimilar)
        - [mkData](#mkdata)
        - [moveListItem](#movelistitem)
        - [parseDate](#parsedate)
        - [readFile](#readfile)
        - [sortDiverseList](#sortdiverselist)
        - [stringFilter](#stringfilter)
        - [timeDeltaString](#timedeltastring)
        - [tupleCalc](#tuplecalc)
        - [uniqueName](#uniquename)
        - [writeFile](#writefile)
    - attributes
        - FileLock - Threading type lock for writing/reading files
        - GlobalLock - Threading lock for global use

- [BBLogger](#bblogger)
    - custom Logger and Formatter class for the built-in python logging module
    - [Shell Options](#environment-variables) - set logging options via shell environment
    - [Get Logger](#getlogger) - initial call to bblogger
    - [BBLogger Class](#logger-class)
    - [BBFormatter Class](#custom-formatter)
    - [Logger Example](#logger-example)

- [TextTools](#texttools)
    - collection of tools for modifying console text
    - [Ansi](#ansi) - work with escaped strings
    - [AnsiList](#ansilist)
    - [TextTools Class](#texttools-class) - collection of classmethods
        - [Attributes](#texttools-attributes)
        - [Functions](#texttools-classmethods)
            - [ansi2rgb](#ansi2rgb)
            - [blockTxt](#blocktxt)
            - [hex2rgb](#hex2rgb)
            - [rgb2ansi](#rgb2ansi)
            - [rgb2hex](#rgb2hex)
            - [rgbString](#rgbString)
            - [money_fmt](#money_fmt)
            - [t2a](#t2a)
            - [from16](#from16)
            - [to16color](#to16color)
            - [help](#texttools-help)
    - [Escape Types](#ansi-escape-types)
    - [Styles](#styles)
    - [Using Ansi Colors](#working-with-color-types)
    - Color Functions
        - [Brightened](#brightened)
        - [Dimmed](#dimmed)
        - [Inverted](#inverted) - needs work
        - [Blended](#blended)
    - [AnsiCombo](#ansicombo)
    - [Cursor Controls](#cursor-controls)

- [ChangeLog](#changelog)

## Shell Script

```sh
apputils --help


```
## AppUtils

    module apputils

> Multiple functions/tools for various tasks in python applications

### AppData
apputils.appdata.AppData

```python
class AppData:
    def __init__(self, appname = PROJECT_APP_NAME):
        """
          'appname': set application name for base directory of app files
        """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### AppData Functions

    AppData.appdir()
        - Locates and creates application directories as needed according to application name

    AppData.sysdata()
        - Retrieve default system folders and info

```python
    def appdir( self, d, *folders, file = '', datefile = '',
                create_dir = True, unique = False, move_existing = False):
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

    def sysdata(self, *args, as_tuple = False):
        """
        Return systeminfo
          *args:
            app      : [ 'cache'||'data'||'config'||'launch' ]
            home     : [ 'home'||'userhome' ]
            user name: [ 'user'||'username' ]
            os type  : [ 'os'||'system' ]

          **kwargs:
            'as_tuple': if getting a directory and True, return as a tuple instead
                        of using os.path.join
        """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

### Date

    Imports for working with datetime objects

```python
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
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

### Path
apputils._import.Path

    Imports for working with system files and directories

```python
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
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

### Tools
    apputils.tools

> MISSING DOCUMENTATION

##### appendFile
    apputils.tools.appendFile

```python
def appendFile( path, data, *, mode = 'a', encoding = 'utf-8', **kwargs ):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### attribNameFromString
    apputils.tools.attribNameFromString

```python
def attribNameFromString( string ):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### filterList
    apputils.tools.filterList

```python
def filterList( _list, match, index = None, *,
                not_in = False, _type = None):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### filter_dir
    apputils.tools.filter_dir

```python
def filter_dir(attr, **kwargs):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### getBoolFromString
    apputils.tools.getBoolFromString

```python
def getBoolFromString(s):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### getIndexed
    apputils.tools.getIndexed

```python
def getIndexed(item, args):
      """
    getIndexed(item, args) >>> ( item, args )
        Get item from list of arguments. Returns ( indexed item, args minus item )
      if found else ( None, original args )
    """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### isBinary
    apputils.tools.isBinary

```python
def isBinary(filename):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### isSafeAttribName
    apputils.tools.isSafeAttribName

```python
def isSafeAttribName(name):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### listDepth
    apputils.tools.listDepth

```python
def listDepth( L: list, *, tuples = False ):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### listFlatten
    apputils.tools.listFlatten

```python
def listFlatten( *L, depth: int = 1, tuples = False ):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### matchSimilar
    apputils.tools.matchSimilar

```python
def matchSimilar( find, _list, *,
                  ratio = STRING_SEQUENCE_MATCH_RATIO,
                  getall = False, getalldata = False ):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### mkData
    apputils.tools.mkData

```python
def mkData(obj):
    """
    Make data dictionary from dataclass, ignoring keys that start with '_'
        - embedded dataclasses are recursively moved to a dict() object as well
    """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### moveListItem
    apputils.tools.moveListItem

```python
def moveListItem( L: list, from_index, to_index, *, items = False ):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### parseDate
    apputils.tools.parseDate

```python
def parseDate(s, fmt = ''):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### readFile
    apputils.tools.readFile

```python
def readFile( path, *, mode = None, encoding = 'utf-8', **kwargs ):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### sortDiverseList
    apputils.tools.sortDiverseList

```python
def sortDiverseList( L: list|tuple, *,
                     reverse = False, unknowns_last = False ):
    """
    Sorts lists|tuples containing both str and int
        - integers are returned before strings
        - always returns a list object

        Types other than int|float|str are sorted by their '__name__'
      attribute if existing. These will come before the unkown types,
      which will be first in the list, unless 'unknowns_last' is set
      to True, and sorted by their __repr__ value.
    """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### stringFilter
    apputils.tools.stringFilter

```python
def stringFilter( obj: Any, *,
                  func = None, start = [], end = [],
                  re_search: re.compile = None, re_match: re.compile = None ):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### timeDeltaString
    apputils.tools.timeDeltaString

```python
def timeDeltaString(t):
    """
    Convert time from timedelta object to xx:xx:xx
    """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### tupleCalc
    apputils.tools.tupleCalc

```python
def tupleCalc( a, b, op, *, diff = False, round_int = False ):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### uniqueName
    apputils.tools.uniqueName

```python
def uniqueName(path, *, move_existing = False):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### writeFile
    apputils.tools.writeFile

```python
def writeFile( path, data, *, mode = 'w', encoding = 'utf-8', **kwargs ):
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

## BBLogger

    module bblogger

> Custom log formatting and file handling

> Subclasses of the python logging module

#### Environment Variables

> Set logging options using shell variables

```python
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
```

- run script in shell `bblogger-shell-settings` to view available environment variables

### getLogger
    bblogger.logger.getLogger

> Use this for initial logger to set the logging class and load environment variables

```python
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
                                    - shell var =
            'filelevel'        : [ DEFAULT = 1 ] Set log level for file. Default is 1, DEBUGGING
                                    - must be set with initial call to logger.getLogger()
                                    - shell var =
            'rootlevel'        : [ DEFAULT = 1 ] Set the root logger level
                                    - usually best to keep this default
            'fileformat'       : [ DEFAULT = 'html' ] Text formatting for file - 'plaintext'
                                    or 'html'
                                    - shell var =
            'file_write_mode'  : [ DEFAULT = 'a' ] write mode for file stream
                                    - 'a': append, 'b': backup old logfile, 'w': overwrite old logfile
            'overwrite_time'   : [ DEFAULT = -1 ] Ignored if < 0. Amount of seconds before logfile
                                    is overwritten
                                    - shell var =
            'avoid_overwrite'  : [ DEFAULT = True ] Don't overwrite the logfile if existing


              A new file will be created if not existing as long as the directory
            already exists. If only a filename is given for 'path', the file will
            be written in the user's HOME folder. Extra options should only need
            applied for the first time initiating a logger in your app/script.

        NOTE: Shell environment variables will override programatic calls to BBLogger
    """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

#### Logger Class
    bblogger.logger.BBLogger

```python

class BBLogger( logging.getLoggerClass() ):
    """
    Console and file logging, formatted with BBFormatter
        - options are set through logger.getLogger() with initial call
        - subsequent loggers should be called with python's logging
          module: logging.getLogger()
    """

  # Added (or overridden) functions

    def setLevel(self, level = None, *opts, set_global = False):
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

    def set_format(self, formatting):
        """
        Change formatting for console logging
            'basic' - simple, nicely formatted messaging
            'debug' - more info pertaining to each message
                      * defaults to log level 1
        """

```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

#### Custom Formatter
    bblogger.logger.BBFormatter

```python
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
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

### Logger Example

```python

# __init__.py

from bblogger import getLogger
log = getLogger( __name__, 3,
                 appname   = "The_Awesomest_Application_Ever",
                 filepath  = "/path/to/logfile",
                 filelevel = 1,
                 consoleformat = 'basic',
                 fileformat = 'html' )

    # NOTE subsequent calls to bblogger.getLogger will return a logger with initial options

# -------------------------------------------------------------

# __main__.py

import logging
log = logging.getLogger(__name__)

```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

## TextTools
    module texttools

- Collection of console text and ansi manipulation tools
- Add/create text colors for console
- Includes limited html formatting
- Adds a custom color template to user app folder that is loaded on import
- Some consoles may not accept all available attributes
- [Ansi](#ansi) and [AnsiList](#ansilist) for working with strings containing ansi escapes

### Ansi
    texttools.ansitools.Ansi

> Work with strings containing ansi escape codes

        - Reports accurate (printed) string length
        - Built in method to convert to an html `<span>` string
            - wrapper for TextTools classmethod `esc2html`
        - Provides a 'clean' (escapes removed) version of the string
        - Will not throw an 'IndexError' with __getitem__, instead will return an empty string
        - Overloaded Constructor
            - If multiple strings are passed to Ansi(), an [AnsiList](#ansilist) is returned
        - Tries to always return an Ansi object when standard strings are inserted/added
            - This won't work when using an Ansi object in an f-string

```python
class Ansi(str):
    """
        Holds a string object with escapes while still reporting an accurate
      length. also provides a cleaned version (no escapes).

        Using f-strings will 're-class' the object to a standard str() object.
      It is recommended to use the '+' operator to join standard string objects
      with Ansi objects so that they remain Ansi types.
    """
    def __init__(self, string = '', **kwargs):
        """
        Create an Ansi string
        ========================================================================
        **kwargs:
            'last_esc_on_slices': add last ansi escape to end of string if
                                    slice leaves it out
                                    - DEFAULT = False
            'reset_on_slice'    : add ansi text reset to end of slices
                                    - overrides 'last_esc_on_slices' if True
                                    - DEFAULT = False
            'strsep'            : passed to AnsiList if split is used

            * Also will look for environment variables 'LAST_ESC_ON_SLICES' and
                'RESET_ON_SLICES' in os.environ. Boolean values are expected.
                Anything other than 'false', '0', or 'no' will set these values
                to True.
        """
```

> Ansi is a subclass of `str`, made to facilitate the formatting and printing of strings containing
> ansi escape codes. Because escape codes, on terminals that accept escapes, don't use any columns
> when printed, it makes it hard to do print formatting and text coloring. This attempts to account
> for that by manipulating the character count. This greatly changes iteration, indexing, and slicing
> of an Ansi object.
>
> It can be confusing to use __getitem__ and __iter__ methods. Iterating through 'string' will separate
> the escapes as single characters. In the case of 'string', the last yielded item is `'\x1b[0m'`, yet
> `string[-1]` returns `'!\x1b[0m'`, prepending the last non escaped character to the ansi escape. This
> is by design because the Ansi and AnsiList classes are specifically made to assist in printing and print
> formatting with strings containing ansi escapes. The attributes `clean` and `string` are provided in
> Ansi() as native `str` objects for more complicated uses. Another attribute `escapes` will list all the
> escapes in the string. This was the best I could come up with for handling iteration, indexing, and
> slicing.
>
> Because of the complications of iteration and slicing, it will never throw an IndexError when using
> __getitem__. Instead, an empty string `''` will be returned.
>
> Here is showing some characteristics of Ansi objects:

```python
>>> from texttools import Ansi
>>> string = Ansi( '\x1b[38;2;51;153;255mHello\x1b[38;2;102;255;102m World!\x1b[0m' )

# Actual length
>>> string.rlen()
53

# Normal reported length
>>> len(string)
12

# Iteration
>>> string_list = list(string)
>>> string_list
['\x1b[38;2;51;153;255m',
 'H',
 'e',
 'l',
 'l',
 'o',
 '\x1b[38;2;102;255;102m',
 ' ',
 'W',
 'o',
 'r',
 'l',
 'd',
 '!',
 '\x1b[0m']
>>> len(string_list)
15

# indexing and slicing
>>> string[-1]
'!\x1b[0m'

>>> string[:5]
'\x1b[38;2;51;153;255mHello'

>>> string[:6]
'\x1b[38;2;51;153;255mHello\x1b[38;2;102;255;102m '
    # notice the space after the escape code

>>> string[:7]
'\x1b[38;2;51;153;255mHello\x1b[38;2;102;255;102m W'
```

> Because of the characteristics of Ansi strings, splitting is also a bit different.
> Ansi.split() with no arguments will split the string using the value in Ansi.strsep
> and return an AnsiList containing the same `strsep` value. This works vice-versa as
> well when using the added list method `join` in AnsiList.

```python
>>> from texttools import Ansi

>>> string = Ansi( '\x1b[38;2;51;153;255mHello\x1b[38;2;102;255;102m World!\x1b[0m' )
>>> string.split()
[ '\x1b[38;2;51;153;255mHello\x1b[38;2;102;255;102m',
  'World!\x1b[0m' ]

# let's try setting the 'strsep' kwarg to 'l'
>>> string = Ansi( '\x1b[38;2;51;153;255mHello\x1b[38;2;102;255;102m World!\x1b[0m', strsep = 'l' )
>>> split_string = string.split()
>>> split_string
[ '\x1b[38;2;51;153;255mHe',
  '',
  'o\x1b[38;2;102;255;102m Wor',
  'd!\x1b[0m' ]

>>> type(split_string)
texttools.ansitools.AnsiList
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

### AnsiList
    texttools.ansitools.AnsiList

- subclass of `list`
- Accepts 0 or more string arguments to form a list of [Ansi](#ansi) strings
- Shares the same keyword arguments as [Ansi](#ansi)
- Returns [Ansi](#ansi) objects with `join` and `__str__`

Added methods:

```python
    def iterclean(self):
        """
        A generator of this list with all ansi escapes removed
        """

    def join(self, s = None, **kwargs):
        """
        Join items in the list with the character in self.strsep
            - returns an Ansi object
        """

    def strip(self, item = None, *, strip_none = False ):
        """
        Removes any list items matching 'item'
            - returns a new AnsiList object
        """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

### TextTools Class
    texttools.TextTools

> Most of the attributes/functions can be imported directly from the texttools package

```python
class TextTools:
    """
    Tools for getting and printing colorized/styled text
    """

      # All functions in this class are classmethods

```

#### TextTools Attributes

- FG - foreground RGB ansi escape types
- BG - background RGB ansi escape types
- Styles - text styles (bold, italic, underline, strikethrough, blink)

#### TextTools Classmethods

##### ansi2rgb
    texttools.TextTools.ansi2rgb

```python
@classmethod
def ansi2rgb(cls, ansi, *, fg_color = True, bg_color = True):
    """
    ansi2rgb( ansi, *, fg_color = True, bg_color = True ) >>> tuple()

        Returns a 5 or 10 part tuple from a string containing ansi escapes
          *args
            'ansi': string containing ansi escape patterns

          **kwargs
            'fg_color': include foreground tuple in results
                         - default = True
            'bg_color': include background color in results
                         - default = True

            Foreground color is always at the beginning of the tuple if both
          'fg_color' and 'bg_color' are True and both values are found
    """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### blockTxt
    texttools.TextTools.blockTxt

```python
    @classmethod
    def blockTxt( cls, txt, *,
                  fill_indent = False,
                  fill_width = False,
                  indent = 0,
                  indent_first = 0,
                  keep_newlines = False,
                  line_break = ' ',
                  push = 0,
                  push_first = False,
                  split_escapes = True,
                  start_column = 0,
                  width = 0,
                  width_includes_indent = True ):
        """
        Indents text for neater printing
          *args:
            'indent'   : amount of indenting to use after 1st line
                          - 'txt' is split by newlines and 'line_break' value
                          - if 'keep_newlines' == True, only 'line_break' value is
                            used to split 'txt'
                          - default = 0
            'push'     : push all indent values (does not include width)
                         to the right [n] amount of columns
                          - default = 0
            'txt'      : full text string
            'width'    : total width of text block
                          - if negative, subtract from the width found
                            using os.get_terminal_size
                          - does not include indent if width_includes_indent == False

          **kwargs:
            'indent_first'         : Amount of columns to indent to first line
                                      - 'indent' to matches the indent value
                                      - a negative value subtracts from indent value
                                        ( minumum value will be 0 )
                                      - default = 0
            'width_includes_indent': If True (default), includes indent in total width,
                                     otherwise total width = width + indent
            'start_column'         : Column that first line starts on
                                      - use 'indent' to match the indent value
                                      - default = 0
            'split_escapes'        : Resets text at end of lines and uses escapes from
                                     the previous line to reset it.
                                      - default = True
            'keep_newlines'        : Doesn't remove newlines from provided text
                                      - might have double newlines in result
            'line_break'           : Provide a string pattern to try to break lines on
                                      - default = ' '
            'push_first'           : Include the first line when using 'push' argument
                                      - default = False
           ** use fill options to make sure background colors, if used, will cover before
                and/or after the text characters

            'fill_width'           : Fill the remaining width in each line with a space
                                      - default = False
            'fill_indent'          : Insert escape code before the indent spaces when using
                                     'split_escapes'
                                      - default = False
        """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### hex2rgb
    texttools.TextTools.hex2rgb

```python
    @classmethod
    def hex2rgb(cls, HEX):
        """
        Returns an RGB tuple from a hexidecimal code
            'HEX': hexidecimal value representing a color
        """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### rgb2ansi
    texttools.TextTools.rgb2ansi

```python
    @classmethod
    def rgb2ansi(cls, R = 0, G = 0, B = 0, *, bg = False):
        """
        Returns an ansi escape string from RGB values
            'R': integer for Red    [0-255]
            'G': integer for Green  [0-255]
            'B': integer for Blue   [0-255]

          * default values are set to Black - (0,0,0)
        """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### rgb2hex
    texttools.TextTools.rgb2hex

```python
    @classmethod
    def rgb2hex(cls, RGB):
        """
        Returns a hexidecimal code from an rgb code
            'RGB': tuple|list of 3 integers
        """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### rgbString
    texttools.TextTools.rgbString

```python
    @classmethod
    def rgbString(cls, value):
        """
        Create an rgb string
            'value': hex, string of integers, list|tuple, or FG_Color|BG_Color
        """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### money_fmt
    texttools.TextTools.money_fmt

```python
    @classmethod
    def money_fmt(cls, n, *, color_type = 'term'):
        """
        Return formatted number to money string
            accepted color_type:
                'term', 'term_reverse', 'html', or 'html_reverse'
        """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### t2a
    texttools.TextTools.t2a

```python
    @classmethod
    def t2a(cls, t: tuple|list, *, end = 'm'):
        """
        Tuple to ansi escape
            - provide a tuple or list of ansi escape integers
            - returns an ansi escape string
        """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### from16
    texttools.TextTools.from16

```python
    @classmethod
    def from16(cls, color, *, return_data = False):
        """
        16 color tuple to rgb tuple
            - if len(tup) == 1, assumes 0 for first value
        """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

##### to16color
    texttools.TextTools.to16color

```python
    @classmethod
    def to16color(cls, rgb, *, bg = False, color_dict = False, diff_key = COLORS_RGB_DIFF_KEY, all_results = False ):
        """
        Rgb to 16 color tuple
            - rgb length can be 3 or 5
            - if rgb doesn't match color, tries to find the closest match
            - if len(rgb) != 5, a fg color is returned by default

            'bg'         : True to force or set to return a bg color
            'data'       : True to return a dict
            'diff_key'   : key to sort matches by
                            [ 'mean'||'median'||'max'||'min'||'min_max_avg' ]
            'all_results': return a list of all result data
                            - assumes 'data' == True
        """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

#### TextTools Help
    texttools.TextTools.help

```python
    @classmethod
    def help(cls, *, return_list = False):
        """
        TextTools help message
            - prints detailed list of available colors

          'return_list': return as a list instead of printing
                          - default = False
        """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

#### Ansi Escape Types

- types of ansi escape objects - subclasses of `str`
    - FG_Color
    - BG_Color
    - Style
    - Reset
    - AnsiCombo

#### Color Modifiers

- functions defined in escape types that have a color attributes
    - Dimmed
    - Brightened
    - Blended
    - Inverted

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

### Styles

>     Blink:
        Ansi style: Blink
          - Set text to blinking

        Attribute Name:   Bl|blink
        Ansi Code:        (5,)

>     Remove Blink:
        Ansi style: Remove Blink
          - Remove the blinking text escape

        Attribute Name:   Bl_|remove_blink
        Ansi Code:        (25,)

>     Bold:
        Ansi style: Bold
          - Set text to bold

        Attribute Name:   B|bold
        Ansi Code:        (1,)

>     Remove Bold:
        Ansi style: Remove Bold
          - Remove the bold text option

        Attribute Name:   B_|remove_bold
        Ansi Code:        (21,)

>     Italic:
        Ansi style: Italic
          - Set text to italic

        Attribute Name:   I|italic
        Ansi Code:        (3,)

>     Remove Italic:
        Ansi style: Remove Italic
          - Remove the italic text option

        Attribute Name:   I_|remove_italic
        Ansi Code:        (23,)

>     Strikethrough:
        Ansi style: Strikethrough
          - Set strikethrough decoration to text

        Attribute Name:   S|strikethrough
        Ansi Code:        (9,)

>     Remove Strikethrough:
        Ansi style: Remove Strikethrough
          - Remove the strike-through text option

        Attribute Name:   S_|remove_strikethrough
        Ansi Code:        (29,)

>     Underline:
        Ansi style: Underline
          - Set underline decoration to text

        Attribute Name:   U|underline
        Ansi Code:        (4,)

>     Remove Underline:
        Ansi style: Remove Underline
          - Remove the underline text option

        Attribute Name:   U_|remove_underline
        Ansi Code:        (24,)

>     Reset:
        Ansi style: Reset
          - Reset all ansi styles and colors

        Attribute Name:   _|reset
        Ansi Code:        (0,)

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

### Working With Color Types

> View a list of all default colors from FG or BG escape group

```python
>>> from texttools import FG
>>> FG.help()
"""
  Colors:

    Attributes can be 'stacked' using the BITAND '&' to create an AnsiCombo
      Example:
        FG.white & BG.charcoal & S.Bold

      You can only have a Reset object at the beginning of an AnsiCombo
        S._ & FG.red

      Only one of each color type or Style type is accepted when combining. If 2
    or more objects of the same type are detected, a ValueError will be raised. If a Reset
    object is added anywhere except the beginning of the combo, a TypeError is raised

      NOTE: all color groups share a Reset ('\x1b[0m') object

  Colors in class:
                    ...
"""
```

```python
# Import colors

>>> from texttools import ( FG as c,
>>>                         BG as bg,
>>>                         Styles as S )

# Get colors by full name or 'code' name

>>> color = c.charcoal
>>> color
AnsiColor(< Charcoal (Fg) >)

>>> color = c.ch
>>> color
AnsiColor(< Charcoal (Fg) >)

>>> str(color)
'\x1b[38;2;26;26;26m'

# AnsiColor attributes

>>> color.rgb       # RGB tuple
(26, 26, 26)
>>> ch.name         # object name
'Charcoal (Fg)'
>>> ch.hex          # hexidecimal value
'#1a1a1a'
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

### Color Functions

> Use functions in color objects to modify RGB values
> - AnsiCombos that have color attributes will also have these functions
> - If an AnsiCombo has both foreground and background colors, both will be affected

#### Brightened
    texttools.types.Brightened

> Lighten AnsiColor with 'bright' function
> - Optionally add a percentage of brightness (default is 15%)

```python
>>> gray = c.dark_gray
>>> gray.rgb
(56, 56, 56)

>>> gray_brightened = color.bright(20)
>>> gray_brightened
'Brightened(< Dark Gray (Fg) - %20 >)'

>>> gray_brightened.rgb
(96, 96, 96)

# You can also use the '+' operator to add the default (15%) bright value
>>> +gray
'Brightened(< Dark Gray (Fg) - %15 >)'

# Doing this more than once will exponentially brighten the object
>>> (+gray).rgb
(86, 86, 86)

>>> (+++gray).rgb
(133, 133, 133)

# NOTE when using operators like this in AnsiCombo creation, the expressions
#   need to be wrapped in parentheses.
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

#### Dimmed
    texttools.types.Dimmed

> Darken AnsiColor with 'dim' function
> - Optionally add a percentage of dimness (default is 15%)

```python
>>> blue = c.light_blue
>>> blue.rgb
(51, 153, 255)

>>> blue_dimmed = blue.dim(20)
>>> blue_dimmed
'Dimmed(< Light Blue (Fg) - %20 >)'

>>> blue_dimmed.rgb
(41, 122, 204)

# You can also use the '-' operator to subtract the default (15%) dim value
>>> (-blue).rgb
(43, 130, 217)

# Doing this more than once will exponentially dim the object
>>> (---blue).rgb
(31, 94, 156)
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

#### Inverted
    texttools.types.Inverted

> Invert AnsiColor with the 'invert' function
> - this function takes no arguments
> - This still needs work and will change in the future, but for now...

```python
>>> blue = c.light_blue
>>> blue.rgb
(51, 153, 255)

>>> blue_inverted = blue.invert()
>>> blue_inverted
'Inverted(< Light Blue (Fg) >)'

>>> blue_inverted.rgb
(204, 102, 0)

# You can also use the '~' operator to invert
>>> (~blue).rgb
(204, 102, 0)

# Doing this more than once or using invert() on the inverted object
# will just revert back to the original AnsiColor

>>> blue_inverted.invert()
AnsiColor(< Light Blue (Fg) >)
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

#### Blended
    texttools.types.Blended

> Blend 2 or more AnsiColors or AnsiCombos with the 'blend' function
> - probably the coolest function :)
> - first argument is the color to blend
> - optional 2nd argument to set the blend percentage
> - default blend value = 15%
>    - usually requires a higher percentage to notice a difference
> I've written a linear gradient string function that will be incorporated in TextTools in a future release

```python
>>> white = c.white
>>> white.rgb
(255, 255, 255)

>>> orange = c.orange
>>> orange.rgb
(255, 128, 0)

>>> white_orange_blend = white.blend( orange, 40 )
>>> white_orange_blend
'Blended(< White||Orange- %40 >)'

>>> white_orange_blend.rgb
(255, 204, 153)

# AnsiColors can also be blended using the BITOR '|' operator
#  - this uses the default 15% blend value

>>> white_orange = white|orange
>>> white_orange
'Blended(< White||Orange- %15 >)'
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

### AnsiCombo
    texttools.types.AnsiCombo

> AnsiColors can be combined using the BITAND operator `&`. Only one of each color type
> ( `FG_Color`, `BG_Color` ) can be combined. Every `Style` object can also be added as
> long as the 'remove' version isn't combined with the non 'removed' version. A `Reset`
> object can be used in the combination but must be the first to the list or else a
> `TypeError` is raised. Multiple objects that conflict will raise a `ValueError`.
>
> Example:

```python
>>> from texttools import FG, BG, Styles as S

>>> combo = FG.yellow & BG.blue
>>> combo
"AnsiCombo(< Yellow (Fg) + Bg Blue (Bg) >)"

    # here, FG._ is actually a Reset object, not an FG_Color
>>> combo = FG._ & FG.gold & BG.dark_gray & S.italic
>>> combo
"AnsiCombo(< Reset + Gold (Fg) + Bg Silver (Bg) + Italic >)"

    # trying to add a Reset in the middle of Combo
>>> combo = FG.gold & FG._ & BG.dark_gray & S.italic
"TypeError: Can't add 'Reset' type to another attribute"

    # adding 2 conflicting objects
>>> combo = FG.gold & S.remove_italic & BG.dark_gray & S.italic
"ValueError: 'AnsiCombo' already contains 'italic' attributes"
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

### Cursor Controls
    texttools.cursorcontrols.CursorControls

```python
>>> from texttools import Cursor

>>> Cursor.Clear.__doc__
        """
        Clear screen or line
          - alias = 'Cursor.clr'
          - clear entire screen (2J)

            Clear.line
              - clear current line (2K)
                L: clear line left of cursor (1K)
                R: clear line right of cursor (0K)

            Clear.screen
              - clear entire screen (2J)
                up: clear screen above cursor (1J)
                dn: clear screen below cursor (0J)
        """

>>> Cursor.L.__doc__
        """
        Cursor Left
          'n': Number of columns
        """

>>> Cursor.R.__doc__
        """
        Cursor Right
          'n': Number of columns
        """

>>> Cursor.col.__doc__
        """
        Cursor To Column
          'n': column number
        """

>>> Cursor.dn.__doc__
        """
        Cursor Down
          'n': Number of lines
        """

>>> Cursor.getpos.__doc__
        """
        Get cursor position
            - returns tuple( [line], [column] )
        """

>>> Cursor.help.__doc__
        """ Help message """

>>> Cursor.hide.__doc__
        """ Cursor Invisible """

>>> Cursor.pos.__doc__
        """
        Set cursor position
            - PositionCursor( [line], [column] )
        """

>>> Cursor.show.__doc__
        """ Cursor Visible """

>>> Cursor.up.__doc__
        """
        Cursor Up
          'n': Number of lines
        """
```

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>

## Changelog

- 0.3.5
    - modified BBLogger and getLogger to hopefully maintain the right level across modules
    - added 'rootlogger' level option

- 0.3.8
    - changed formatter to include filename instead of logger name

- 0.3.9
    - fixed logging error when not in terminal

- 0.3.91
    - fixed typo in basic logging.... maybe

- 0.3.92
    - 2nd attempt at fixing basic logging

- 0.3.95
    - yet another attempt to get basic log formatting right

- 0.4.0
    - re-wrote the basic log formatter

- 0.5.0
    - completely rebuilt bblogger, texttools, and apputils
    - full overhaul of AnsiColors
        - added types:
            - FG_Color
            - BG_Color
            - Style
            - AnsiCombo
            - Brightened
            - Dimmed
            - Inverted
            - Blended
    - added functions to apputils
    - removed bbargparser (working on new version)
    - added user colors and template
    - added a lot to documentation

- 0.5.1
    - fixed a typo in texttools.types

## Thanks To:

<p>Thread at <a href="https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output">Stack Overflow</a> on python log formatting</p>

<p>Adapted from <a href="https://stackoverflow.com/a/56944256/3638629">original code</a> by user at Stack Overflow</p>

> And everyone else on forums across the web for being the sole source of my development learnings :)

<p style="text-align: right;"><a href="#contents"><i>return to contents<i></a></p>
