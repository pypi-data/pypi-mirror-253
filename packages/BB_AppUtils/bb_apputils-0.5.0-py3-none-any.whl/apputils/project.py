import re

def findProjectName(cls, project_dir):
    """
      Attempt to find python project's name by searching the current directory's
    sub-folders and files
    """
    from apputils import Path
    pdir = _findProjectRoot()
    if not pdir:
        return ''

    for f in ( 'setup.py', 'pyproject.toml' ):
        path = JN( project_dir, f )
        if Path.isfile(path):
            name = cls._nameFromFile( cls, path )
            if name:
                return name

    return Path.bn( Path.pwd() )

def _findProjectRoot():
    """
    Find root project folder by checking the current directory and the parents of
    """
    from apputils import Path
    cd = Path.pwd()
    HOME = Path.home()
    lf = None

    if cd.find(HOME) == -1:
        return ''

    while True:
        lf = glob( 'pyproject.toml', root_dir = cd )
        if not lf:
            lf = glob( 'setup.py', root_dir = cd )

        if lf:
            return cd
        elif cd == HOME or cd.find(HOME) < 0:
            return ''
        else:
            cd = DN( cd )

def _nameFromFile(path):
    with open( path, 'r' ) as f:
        lines = f.read().split('\n')

    for line in lines:
        if re.match( '^[\'" ]*name[\'" ]*=', line ):
            return line.split('=', 1)[1].replace(' ','').replace('"','').replace("'",'')
    return ''
