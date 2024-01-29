#!/usr/bin/python3

import sys, os, re, builtins, operator
try:
    from bblogger import getLogger
    log = getLogger(__name__)

    from texttools import FG as c, Styles as S, Ansi, AnsiList
    from apputils import Path

except ImportError:
    print("Please install 'bb_apputils' >= v0.5.0 to use this script")
    if __name__ == "__main__":
        sys.exit(1)

except Exception as E:
    print(str(E))
    if __name__ == "__main__":
        sys.exit(1)

from importlib import import_module as imp
from .syntax_highlighter import SyntaxHighlighter

ALL_ATTRIBS = { **globals(),
                **dict([( i, getattr( builtins, i )) for i in filter( lambda x: not x.startswith('_'), dir(builtins) )]),
                **dict([( i, getattr( operator, i )) for i in filter( lambda x: not x.startswith('_'), dir(operator) )])}

def printHelp():
    from texttools import FG as c, Styles as S, Ansi, AnsiList
    opts = [('-c', '--comments', 'Show comments in output'),
            ('', '', "- default = False"),
            ('-f', '--function', "Function name - same as adding ':function' after module name"),
            ('-h', '--help', 'Print help message'),
            ('-m', '--module', 'View code from a module'),
            ('', '', "- will attempt to automagically parse this without the option given"),
            ('-n', '--no-highlighting', 'Disable syntax highlighting in output'),
            ('', '', '- only effects output - string data is still processed'),
            ('', '', "- default = False"),
            ('-p', '--filepath', 'View file contents'),
            ('', '', "- path can also be provided without this option"),
            ('-s', '--string', 'Code view from a provided string')]

    R = [ '', f"    {c.gr&S.U}code-view{c._}{c.Gr&S.I} - view highlighted python code{c._}", '' ]
    l_len = max( [ len(i[1]) for i in filter( lambda x: bool( x[1] ), opts ) ])
    od = [ f"{c._&c.dGr&S.B}{i}{c._}" for i in ( '(', '|', ')' ) ]

    for opt in opts:
        if not ( opt[0] or opt[1] ):
            for i in opt[2:]:
                R.append( f"{'':<{l_len+17}}{c.Gr&S.I}{i}{c._}" )
        else:
            s, L, D = opt
            R.append( f"    {od[0]} {c.Gd&S.I}{s} {od[1]} {c.Gd&S.I}{L:^{l_len}} {od[2]}{c.dl&S.B}: {c._}{c.Gr&S.I} {D}{c._}" )
    R.append('')
    print( '\n'.join(R) )
    return 0

def highlight_string( string: str, **kwargs ):
    log.debug("Highlighting string")
    SH = SyntaxHighlighter( **kwargs )
    txt = SH.highlight( string )
    return txt

def highlight_module( obj: object, **kwargs ):
    def get_indent(L):
        n = 0
        if not L.strip():
            return 999
        while L[n] == ' ':
            n += 1
        return n

    lines = []
    try:
        if hasattr( obj, '__code__' ):
            code = obj.__code__
            file = code.co_filename
            with open( file, 'r' ) as f:
                lines = f.read().split('\n')

            lineno = code.co_firstlineno - 1
            _indent = get_indent( lines[lineno] )

            end_line = lineno +1
            indent = get_indent( lines[end_line] )

            while end_line < len(lines) and ( not lines[end_line].strip() or lines[end_line].startswith(f"{'':<{indent}}")):
                end_line += 1

        elif hasattr( obj, '__module__' ):
            mod = imp( obj.__module__ )
            if hasattr( mod, '__file__' ):
                return highlight_file( mod.__file__ )
            else:
                raise ValueError(f"No code available for '{obj}'")

        elif hasattr( obj, '__file__' ):
            return highlight_file( obj.__file__ )

        else:
            raise ValueError(f"No code available for '{obj}'")

        data = '\n'.join([ i[_indent:] for i in lines[ lineno : end_line ] ])

    except Exception as E:
        log.exception(E)
        return ''

    if data:
        return highlight_string( data, **kwargs )
    else:
        return ''

def highlight_file( path: str, **kwargs ):
    data = ''
    try:
        assert os.path.isfile(path)
        with open( path, 'r' ) as f:
            data = f.read()

    except AssertionError as E:
        log.exception(E)
        log.error(f"Invalid filepath - '{path}'")
    except Exception as E:
        log.exception(E)

    if not data:
        log.error(f"No data found in '{path}'")
        return ''

    return highlight_string( data, **kwargs )

def _view_code_():
    args = sys.argv[1:]
    if not args:
        print(f"{c.r}  [ERROR]{c.Gr&S.I} no arguments given{c._}")
        return 1

    DATA = ''
    DATA_TYPE = ''
    COMMENTS = False
    NO_HIGHLIGHT = False
    txt = ''

    arg = 'None'
    try:
        def chkData():
            if DATA_TYPE:
                raise SyntaxError(f"Data type already specified as '{DATA_TYPE}' - only one data type allowed")

        while args:
            arg = args.pop(0)
            if arg in ( '-c', '--comments' ):
                COMMENTS = True

            elif arg in ( '-f', '--function' ):
                if not ( DATA_TYPE == 'module' and DATA.find(':') < 0 ):
                    chkData()

                DATA = DATA + ':' + args.pop(0)
                DATA_TYPE = 'module'

            elif arg in ( '-m', '--module' ):
                if not ( DATA_TYPE == 'module' and DATA.startswith(':') ):
                    chkData()

                if DATA:
                    DATA = args.pop(0) + DATA
                else:
                    DATA = args.pop(0)
                    DATA_TYPE = 'module'

            elif arg in ( '-h', '--help' ):
                sys.exit( printHelp() )

            elif arg in ( '-p', '--path' ):
                chkData()
                DATA = args.pop(0)
                DATA_TYPE = 'file'

            elif arg in ( '-s', '--string' ):
                chkData()
                DATA = args.pop(0)
                DATA_TYPE = 'string'

            elif not DATA and Path.isfile(arg):
                DATA = Path.abs( arg )
                DATA_TYPE = 'file'

            elif not DATA and ( arg in locals() or \
                re.match( '^[A-Za-z_]{1}[A-Za-z0-9_]*(\.{1}[A-Za-z_]{1}[A-Za-z0-9_]*)*(:[A-Za-z_]{1}[A-Za-z0-9_]*)?$', arg )):
                    DATA = arg
                    DATA_TYPE = 'module'

            elif arg in ( '-n', '--no-highlighting' ):
                NO_HIGHLIGHT = True

            else:
                raise SyntaxError(f"Invalid argument '{arg}'")

        if not DATA:
            raise ValueError("Nothing to highlight")

        log.debug(f"{DATA = }, {DATA_TYPE = }")
        if DATA_TYPE == 'module':
            log.debug(f"Highlighting data from module '{DATA}'")
            title = []
            module = None
            MOD, FUNC = '', ''
            if DATA.find(':') >= 0:
                MOD, FUNC = DATA.rsplit(':', 1)
            else:
                MOD = DATA

            log.debug(f"{MOD = }, {FUNC = }")

            if MOD:
                title += MOD.split('.')
                try:
                    module = imp( MOD )
                except:
                    try:
                        if MOD.find('.') > 0:
                            module = imp( *MOD.rsplit('.', 1))
                        else:
                            raise
                    except:
                        title = []
                        if not FUNC:
                            FUNC = MOD
                        else:
                            raise

            if FUNC:
                if module:
                    title = [ *MOD.split('.'), FUNC ]
                    module = getattr( module, FUNC )
                elif FUNC in ALL_ATTRIBS:
                    title = [ FUNC ]
                    try:
                        module = ALL_ATTRIBS[FUNC]
                    except:
                        raise ValueError(f"Couldn't find a module named '{DATA}'")

            title = f"{c._&c.gr&S.B}.{c._&c.Gr&S.I}".join(title)
            title = f"{c._&c.Gr&S.I}{title}{c._}"

            txt = highlight_module( module, show_comments = COMMENTS, remove_leading_whitespace = True )

        elif DATA_TYPE == 'file':
            log.debug(f"Highlighting data from file '{DATA}'")
            title = f"{c.ce&S.I}{DATA}{c._}"
            txt = highlight_file( DATA, show_comments = COMMENTS )

        elif DATA_TYPE == 'string':
            log.debug(f"Highlighting provided string '{DATA[:25]}'")
            title = f"{c.Gr&S.I}from string{c._}"
            txt = highlight_string( DATA, show_comments = COMMENTS, remove_leading_whitespace = True )

    except Exception as E:
        log.exception(E)
        sys.exit(1)

    # Adding title to output
    if txt:
        txt = str(AnsiList( [ '', f"  {c.S&S.U}Python Code View{c._&c.Gr&S.I} - {c.ce}{title}{c._}",
                              *[ f"    {i}" for i in str(txt).split('\n') ], "" ],
                            strsep = '\n' ))

        if NO_HIGHLIGHT:
            print( txt.clean )
        else:
            print(txt)
        sys.exit(0)

    else:
        print(f"\n{c.r}  [ERROR]{c.Gr&S.I} nothing to print{c._}\n")
        sys.exit(1)

if __name__ == "__main__":
    _view_code_()
