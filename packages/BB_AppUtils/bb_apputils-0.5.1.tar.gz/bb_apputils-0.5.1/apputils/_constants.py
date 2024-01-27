# Constant variables
import os

# global mutex for multithreaded stuff
from threading import Lock
global GLOBAL_LOCK
GLOBAL_LOCK = Lock()

global _AU_TMP_DIR_
from tempfile import gettempdir
_AU_TMP_DIR_ = os.path.join( gettempdir(), 'apputils_tmp_39287yuh82hdg268' )
os.makedirs( _AU_TMP_DIR_, exist_ok = True )

PROJECT_APP_NAME = 'AppUtils'
if 'PROJECT_APP_NAME' in os.environ and os.environ['PROJECT_APP_NAME']:
    PROJECT_APP_NAME = os.environ['PROJECT_APP_NAME']

FILE_DATE_FORMAT = '_%Y-%m-%d_%H-%M-%S'
if 'FILE_DATE_FORMAT' in os.environ and os.environ['FILE_DATE_FORMAT']:
    PROJECT_APP_NAME = os.environ['FILE_DATE_FORMAT']

STRING_SEQUENCE_MATCH_RATIO = 0.7
if 'STRING_SEQUENCE_MATCH_RATIO' in os.environ and os.environ['STRING_SEQUENCE_MATCH_RATIO']:
    opt = None
    try:
        opt = float( os.environ['STRING_SEQUENCE_MATCH_RATIO'] )
        PROJECT_APP_NAME = opt
    except:
        pass
    finally:
        del opt

def getLogger(name):
    try:
        import bblogger.logger as bbl
        logger = bbl.getLogger( name, consoleformat = 'debug' )
    except Exception as E:
        import logging
        logger = logging.getLogger(__name__)
    return logger
