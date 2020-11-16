#Grupo PHP
#Kevin Cevallos
#María Camila Navarro
#Joffre Ramírez

import ply.lex as lex
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'boolean': 'BOOLEAN',
    'float': 'FLOAT',
    'string': 'STRING',
    'null': 'NULL',
    'array': 'ARRAY',
    'object': 'OBJECT',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'for each': 'FOREACH',
    'echo': 'ECHO',
    'print': 'PRINT',
    'print_r': 'PRINT_R',
    'var_dump': 'VAR_DUMP',
    'fgets': 'FGETS',
    'fread': 'FREAD',
    'fscanf': 'FSCANF',
    'fpassthru': 'FPASSTHRU',
    'fgetcsv': 'FGETCSV',
    'fgetc': 'FGETC',
    'file_get_contents': 'FILE_GET_CONTENTS',
    'readfile': 'READFILE',
    'file': 'FILE',
    'parse_ini_file': 'PARSE_INI_FILE',
    'implode': 'IMPLODE',
    'explode': 'EXPLODE',
<<<<<<< HEAD
    'new':'NEW',
    'class':'CLASS',
=======

>>>>>>> fea73e935b1231753e3b9ff857e288bd36b52dea
    'count': 'COUNT',
    'sizeof': 'SIZEOF',
    'array_push': 'ARRAYPUSH',
    'sort': 'SORT',
    'asort': 'ASORT',
    'ksort': 'KSORT',
    'unset': 'UNSET',
    'var_export': 'VAR_EXPORT',
    'shuffle': 'SUFFLE',
    'array_merge': 'ARRAY_MERGE',
    'array_search': 'ARRAY_SEARCH',
    'array_rand': 'ARRAY_RAND',
    'array_chunk': 'ARRAY_CHUNK',
    'str_split': 'STR_SPLIT',
    'preg_split': 'PREG_SPLIT',
    'array_unique': 'ARRAY_UNIQUE',
<<<<<<< HEAD
    'function' : 'FUNCTION'
=======
>>>>>>> fea73e935b1231753e3b9ff857e288bd36b52dea

}


tokens =(
    ['NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MAYORQUE',
    'MENORQUE',
    'EQUALS',
    'AND',
    'OR',
    'XOR',
    'NOT',
    'OPEN',
    'CLOSE',
    'END',
<<<<<<< HEAD
    'ID',
     'TRUE',
     'FALSE',
    'TEXT',
     'PEIROT',
     'RCORCHET',
     'LCORCHET',
     'MODULO',
     'DECIMAL',
     'OBJECT_OPERATOR'] + list(reserved.values()))
=======
    'ID'] + list(reserved.values()))


>>>>>>> fea73e935b1231753e3b9ff857e288bd36b52dea

t_OBJECT_OPERATOR=r'->.*\(\)'
t_DECIMAL=r'[0-9]*\.[0-9]+'
t_MODULO=r'%'
t_PLUS=r'\+'
t_MINUS=r'-'
t_TIMES=r'\*'
t_DIVIDE=r'/'
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_EQUALS = r'='
t_ID = r'(\$([a-z]|[A-Z]))([a-zA-Z0-9]+)?'
<<<<<<< HEAD
t_END = r';'
t_TRUE = r'True'
t_FALSE = r'False'
t_TEXT = r'".*"'
t_PEIROT = r'\.'
=======
t_END=r';'


>>>>>>> fea73e935b1231753e3b9ff857e288bd36b52dea
t_OPEN = r'<\?php'
t_CLOSE = r'\?>'
t_AND = r'and'
t_OR = r'or'
t_XOR = r'xor'
t_NOT = r'!'
t_RCORCHET=r'\}'
t_LCORCHET=r'\{'
T_IS_EQUAL = r'\=='
T_IS_IDENTICAL = r'\==='
T_IS_NOT_EQUAL= r'\!='
T_IS_NOT_IDENTICAL= r'/!=='
T_IS_GREATER_OR_EQUAL=r'\>='
T_IS_SMALLER_OR_EQUAL=r'\<='
T_SPACESHIP = r'\<=>'

t_ignore = ' \t'

<<<<<<< HEAD
def t_CLASS(t):
    r'class .*'
    return t

def t_NEW(t):
    r'new .*'
    return t
=======

>>>>>>> fea73e935b1231753e3b9ff857e288bd36b52dea

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_IF(t):
    r'if'
    return t
def t_ELSE(t):
    r'else'
    return t
def t_ELSEIF(t):
    r'elseif'
    return t
def t_BOOLEAN(t):
    r'boolean'
    return t
def t_FLOAT(t):
    r'float'
    return t
def t_STRING(t):
    r'string'
    return t
def t_NULL(t):
    r'null'
    return t
def t_ARRAY(t):
    r'array'
    return t
def t_OBJECT(t):
    r'object'
    return t
def t_BREAK(t):
    r'break'
    return t
def t_CONTINUE(t):
    r'continue'
    return t
def t_RETURN(t):
    r'return'
    return t
def t_FOREACH(t):
    r'foreach'
    return t
def t_ECHO(t):
    r'echo'
    return t
def t_PRINT(t):
    r'print'
    return t
def t_PRINT_R(t):
    r'print_r'
    return t
def t_VAR_DUMP(t):
    r'var_dump'
    return t


def t_FGETS(t):
    r'fgets'
    return t
def t_FREAD(t):
    r'fread'
    return t
def t_FSCANF(t):
    r'fscanf'
    return t
def t_FPASSTHRU(t):
    r'fpassthru'
    return t
def t_FGETCSV(t):
    r'fgetcsv'
    return t
def t_FGETC(t):
    r'fgetc'
    return t
def t_FILE_GET_CONTENTS(t):
    r'file_get_contents'
    return t
def t_READFILE(t):
    r'readfile'
    return t
def t_FILE(t):
    r'file'
    return t
def t_PARSE_INI_FILE(t):
    r'parse_ini_file'
    return t

def t_IMPLODE(t):
    r'implode'
    return t
def t_EXPLODE(t):
    r'explode'
    return t
def t_COUNT(t):
    r'count'
    return t
def t_SIZEOF(t):
    r'sizeof'
    return t
def t_ARRAY_PUSH(t):
    r'array_push'
    return t
def t_SORT(t):
    r'sort'
    return t
def t_ASORT(t):
    r'asort'
    return t
def t_KSORT(t):
    r'ksort'
    return t
def t_UNSER(t):
    r'unset'
    return t
def t_VAR_EXPORT(t):
    r'var_export'
    return t
def t_FUNCTION(t):
<<<<<<< HEAD
    r'function .*'
    return t
def t_SHUFFLE(t):
    r'shuffle'
    return t
=======
    r'function'
    return t
def t_SHUFFLE(t):
    r'shuffle'
    return t
>>>>>>> fea73e935b1231753e3b9ff857e288bd36b52dea
def t_ARRAY_MERGE(t):
    r'array_merge'
    return t
def t_ARRAY_SEARCH(t):
    r'array_search'
    return t
def t_ARRAY_RAND(t):
    r'array_rand'
    return t
def t_ARRAY_CHUNK(t):
    r'array_chunk'
    return t
def t_STR_SPLIT(t):
    r'str_split'
    return t
def t_PREG_SPLIT(t):
    r'preg_split'
    return t
def t_ARRAY_UNIQUE(t):
    r'array_unique'
    return t




def t_error(t):
    print("No es reconocido '%s'"%t.value[0])
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


lexer=lex.lex()


def analizar(dato):
    lexer.input(dato)
    while True:
        tok =lexer.token()
        if not tok:
            break
        print(tok)

lexer=lex.lex()
archivo= open("archivo.txt")
for linea in archivo:
    print(">>"+linea)
    analizar(linea)
    if len(linea)==0:
        break

