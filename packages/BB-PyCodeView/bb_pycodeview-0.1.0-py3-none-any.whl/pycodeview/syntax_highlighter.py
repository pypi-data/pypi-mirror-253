import re, operator, builtins
from bblogger import getLogger
log = getLogger(__name__)

from texttools import ( Ansi,
                        AnsiList,
                        BG as bg,
                        FG as c,
                        Styles as S,
                        )

_clear = c._ & bg.BL.bright(5)
def _process_( cls, string, **kwargs ):
    return f"{cls.color}{cls._fixDB( string )}{_clear}"

def _process_string_( cls, string, **kwargs ):
    str_mod = re.match( '^[frub]+', string )
    if str_mod:
        color = cls.color.blend( c.dO, 40 )
        pre = str_mod.group()
        string = cls._fixDB( string[str_mod.end():] )
    else:
        pre = ''
        color = cls.color
        string = cls._fixDB( string )

    return str(color) + pre + fr"{string}" + str(_clear)

def _process_comment_( cls, string, *, show = False ):
    c_index = string.find('#')
    d = {}
    for i in re.findall( '"""|'+"'''|"+"'|"+'"', string[:c_index] ):
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    if d and any( v % 2 != 0 for v in d.values() ):
        return ''

    if show:
        return ( c_index, f"{cls.color}{cls._fixDB( string[c_index:] )}{_clear}" )
    return ( c_index, '' )

class SyntaxFilter(type):
    def __new__( cls, index, name, re, color, *args, **kwargs ):
        if 'string' in args:
            proc = _process_string_
        elif 'comment' in args:
            proc = _process_comment_
        else:
            proc = _process_

        clsDict = { 'color': color,
                    'end_index': 0,
                    'index': -1,
                    'input': '',
                    'matches': (),
                    'output': '',
                    'process': proc,
                    're': re,
                    'start_index': 0,
                    }

        return super().__new__( cls, name, (), clsDict )

    def __init__(self, *args, **kwargs):
        pass

    def run( self, *args, start_index, string, show_comments = False ):
        self.start_index = start_index
        self.input = string
        M = []
        index_sub = 0
        for i, match in enumerate( self.re.finditer( string ) ):
            span = match.span()
            if span[0] == span[1] or self._skip( string[:span[0]], string[ slice(*span) ], string[span[1]:] ):
                index_sub += 1
                continue

            formatted = self.process( self, string[ slice(*span) ], show = show_comments )
            if not formatted:
                index_sub += 1
                continue
            elif isinstance( formatted, tuple ):
                span = ( span[0] + formatted[0], span[1] )
                formatted = formatted[1]

            try:
                m = type( 'SyntaxMatch', (), { 'formatted': formatted,
                                               'index'    : i + start_index - index_sub,
                                               'original' : string[ slice(*span) ],
                                               'group'    : match.group(),
                                               'span'     : span,
                                               })()

            except Exception as E:
                log.exception(E)
                index_sub += 1

            M.append(m)

        if M:
            log.debug(f"Adding '{len(M)}' matches with '{self.__name__}'")
        else:
            log.debug(f"No matches found with '{self.__name__}'")

        self.matches = tuple( sorted( M, key = lambda x: x.index ))
        self.end_index = start_index + len(M) - 1
        if self.matches and self.matches[-1].index != self.end_index:
            log.error(f"End index '{self.end_index}' doesn't match last item index in matches '{self.matches[-1].index}'")
        self.output = self._fmt_output()
        return self

    def _fixDB( self, string ):
        return string.replace('{{','{').replace('}}','}')

    def _fmt_output(self):
        s = self.input
        for match in reversed( self.matches ):
            start, end = match.span
            s = f"{s[:start]}{{{match.index}}}{s[end:]}"
        return s

    def _skip( self, a, b, c ):
        return bool(( re.match( '[0-9]+', b ) and re.match( '.*{[0-9]*$', a, re.DOTALL ) and re.match( '^[0-9]*}', c )) \
            or (( b == '}' and re.match( '.*{[0-9]+$', a, re.DOTALL )) or ( b == '{' and re.match( '^[0-9]+}', c ))))

    def format_span(self):
        return ( self.start_index, self.end_index )

    def __iter__(self):
        for match in self.matches:
            yield match.formatted

def special_methods():
    def _f(_x):
        if _x.startswith('__') and _x.endswith('__'):
            return True
        return False

    dunders = set(filter( _f, [ *dir(type), *dir(int), *dir(float), *dir(dict), *dir(operator) ]))
    err, bins = [], []
    for attr in dir(builtins):
        if attr in ( 'True', 'False', 'None', '__doc__' ):
            continue
        if attr.startswith('__'):
            dunders.add(attr)
        elif attr.islower():
            bins.append(attr)
        elif re.match( '^[A-Z]{1}[A-Za-z]+$', attr ):
            err.append(attr)
    return ( bins, dunders, err )

class SyntaxHighlighter(type):
    """
    Syntax list order:
        ( index, name, re, color, args )

      Syntax filter objects (order index):
        # Comments (0)
        # Multiline Text (1)
        # Text (2)
        # Decorators (3)
        # Iterator Brackets (4)
        # Method Definitions (5)
        # Integers (6)
        # Special Attributes (7)
        # Conditional Keywords (8)
        # Dunder Methods (9)
        # Import Keywords (10)
        # Builtins (11)
        # Exceptions (12)
        # Special Python Keywords (13)
        # Bool Values (14)
        # Special Variables (15)
        # Operators (16)
    """
    def __new__( cls, *args, **kwargs ):
        bins, dunders, err = special_methods()
        filters = ( SyntaxFilter( 0, 'Comments', re.compile( r'^.*?#.*?$', re.MULTILINE ), _clear&c.c, 'comment' ),
                    SyntaxFilter( 1, 'MultilineText', re.compile( '^( *[frub]*""".*?"""|'+" *[frub]*'''.*?''')$", re.DOTALL|re.MULTILINE ), _clear&c.ce&S.I ),
                    SyntaxFilter( 2, 'Text', re.compile( '[frub]*".*?"|'+"[frub]*'.*?'" ), _clear&c.Gr&S.I, 'string' ),
                    SyntaxFilter( 3, 'Decorators', re.compile( '^ *@[a-zA-Z_]{1}[a-zA-Z0-9_]*(\(.*\))?$', re.MULTILINE ), _clear&c.Gd&S.I ),
                    SyntaxFilter( 4, 'IteratorBrackets', re.compile( '\[|\]|}}|{{' ), _clear&c.gr&S.B ),
                    SyntaxFilter( 5, 'Methods', re.compile( '\[|\(|\]|\):|\)|(?<=def )[A-Za-z_]{1}[A-Za-z0-9_]*|(?<=class )[A-Za-z_]{1}[A-Za-z0-9_]*' ), _clear&c.S&S.B ),
                    SyntaxFilter( 6, 'Integers', re.compile( r'\b(?<!{)-?[0-9]+\.?[0-9]*(?!})\b' ), _clear&c.g&S.I ),
                    SyntaxFilter( 7, 'SpecialAttribs', re.compile( r'\b'+r'\b|\b'.join(['__name__','__file__','__module__','__doc__'])+r'\b' ), _clear&c.T&S.B&S.I ),
                    SyntaxFilter( 8, 'ConditionalKeywords', re.compile( r'\b'+r'\b|\b'.join(['raise', 'assert','if','then','while','break','continue','return','else','elif','try','except'])+r'\b' ), _clear&c.Y&S.B ),
                    SyntaxFilter( 9, 'Dunders', re.compile( r'\b'+r'\b|\b'.join( dunders )+r'\b' ), _clear&c.P&S.B ),
                    SyntaxFilter( 10, 'ImportKeywords', re.compile( r'\b'+r'\b|\b'.join(['import','from','as'])+r'\b' ), _clear&c.B&S.B&S.I ),
                    SyntaxFilter( 11, 'Builtins', re.compile( r'\b'+r'\b|\b'.join( bins )+r'\b' ), _clear&c.ice&S.B&S.I ),
                    SyntaxFilter( 12, 'Exceptions', re.compile( r'\b'+r'\b|\b'.join( err )+r'\b' ), _clear&c.dR&S.B ),
                    SyntaxFilter( 13, 'PythonKeywords', re.compile( r'\b'+r'\b|\b'.join(['def','class','lambda','object'])+r'\b' ), _clear&c.B&S.I&S.B ),
                    SyntaxFilter( 14, 'Bools', re.compile( r'\b'+r'\b|\b'.join(['True','False'])+r'\b' ), _clear&c.T&S.B&S.I ),
                    SyntaxFilter( 15, 'SpecialVars', re.compile( r'\b'+r'\b|\b'.join(['self','cls'])+r'\b' ), _clear&c.dC&S.I ),
                    SyntaxFilter( 16, 'Operators', re.compile( '==|>=|<=|\!=|&|\|=|\||&=|/|\\+|\-|\\*|\^|=' ), _clear&c.g ))

        return super().__new__( cls, 'SyntaxHighlighter', (), { '__filters__': filters,
                                                                '__formatted__': (),
                                                                'input': '',
                                                                'output': '',
                                                                'processed': '',
                                                                'show_comments': False,
                                                                })

    def __init__( self, *, show_comments = False, remove_leading_whitespace = False, **kwargs ):
        self.show_comments = show_comments
        self.rm_indent = remove_leading_whitespace

    def highlight( self, string: str ):
        if self.output:
            self.__formatted__ = ()
            self.input = ''
            self.processed = ''

        string = str(string).replace( '{', '{{' ).replace( '}', '}}' )
        if self.rm_indent:
            lines = string.split('\n')
            indent = self.get_whitespace_indent(lines)
            if indent:
                string = '\n'.join([ i[indent:] for i in lines ])

        self.input = string
        self.processed = self._process_highlighting()
        self.output = self._process_output()
        return self.output

    @classmethod
    def get_whitespace_indent(self, lines):
        indents = []
        for line in lines:
            if not line.strip():
                continue
            n = 0
            while line[n] == ' ':
                n += 1
            indents.append(n)
        return min(indents)

    def _process_output(self):
        s = self.processed.format( *self.__formatted__ )
        s = re.sub( '\n *\n( *\n)++', '\n\n', s )
        while re.match( '^ *\n', s ):
            s = s[1:]
        while re.match( '.*\n *\n$', s ):
            s = s[:-1]
        return Ansi( f"{_clear}\n\n" + s.strip() + f"\n{c._}" )

    def _process_highlighting(self):
        s = self.input
        index = 0
        for _filter in self.__filters__:
            F = _filter.run( start_index = index, string = s, show_comments = self.show_comments )
            index = F.end_index + 1
            s = F.output
            self.__formatted__ = self.__formatted__ + tuple(F)
            log.debug(f"'{F.__name__}': start index = {F.start_index}, end index = {F.end_index}")

        log.debug(f"Number of formatted matches = {len(self.__formatted__)}")
        log.debug(f"Last format index = {F.end_index}")
        return s
