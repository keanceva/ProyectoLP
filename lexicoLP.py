#Grupo PHP
#Kevin Cevallos
#María Camila Navarro
#Joffre Ramírez

import ply.lex as lex
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    #'boolean': 'BOOLEAN',
    #'float': 'FLOAT',
    #'string': 'STRING',
    'null': 'NULL',
    'array': 'ARRAY',
    #'object': 'OBJECT',
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
    'new':'NEW',
    'class':'CLASS',
    'count': 'COUNT',
    'sizeof': 'SIZEOF',
    'array_push': 'ARRAY_PUSH',
    'sort': 'SORT',
    'asort': 'ASORT',
    'ksort': 'KSORT',
    'unset': 'UNSET',
    'var_export': 'VAR_EXPORT',
    'shuffle': 'SHUFFLE',
    'array_merge': 'ARRAY_MERGE',
    'array_search': 'ARRAY_SEARCH',
    'array_rand': 'ARRAY_RAND',
    'array_chunk': 'ARRAY_CHUNK',
    'str_split': 'STR_SPLIT',
    'preg_split': 'PREG_SPLIT',
    'array_unique': 'ARRAY_UNIQUE',
    'function' : 'FUNCTION',
    'while' : 'WHILE',
    'as' : 'AS'
}


tokens =(
    [

    #Operadores Matemáticos
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'MODULO',

    #Operadores Lógicos
    'AND',
    'OR',
    'XOR',
    'NOT',

    #Símbolos
    'LPAREN',
    'RPAREN',
    #'PEIROT',
    'RCORCHET',
    'LCORCHET',
    'OBJECT_OPERATOR',
    'COMA',
    'OPEN',
    'CLOSE',
    'END',
    'FLECHA',

    #Variable
    'ID',

    #Número
    'NUMBER',
    'DECIMAL',

    #Valor Boolean
    'TRUE',
    'FALSE',

    #Cadena de texto
    'TEXT',


     #Operadores Comparación
     'MAYORQUE',
     'MENORQUE',
     'IS_EQUAL',
     'IS_IDENTICAL',
     'IS_NOT_EQUAL',
     'IS_NOT_IDENTICAL',
     'IS_GREATER_OR_EQUAL',
     'IS_SMALLER_OR_EQUAL',
     'SPACESHIP',

     #Nombre de Funciones
     'FNOMBRE'
        ] + list(reserved.values()))

#Operadores Matemáticos
t_MODULO=r'%'
t_PLUS=r'\+'
t_MINUS=r'-'
t_TIMES=r'\*'
t_DIVIDE=r'/'
t_EQUALS = r'='

#Operadores Lógicos
t_AND = r'and'
t_OR = r'or'
t_XOR = r'xor'
t_NOT = r'!'

#Símbolos
t_OBJECT_OPERATOR=r'->'
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_END = r';'
t_TEXT = r'".*"'
t_FLECHA = r'=>'


#t_PEIROT = r'\.'
t_OPEN = r'<\?php'
t_CLOSE = r'\?>'
t_RCORCHET=r'\}'
t_LCORCHET=r'\{'
t_COMA=r','

#Variable
t_ID = r'(\$([a-z]|[A-Z]))([a-zA-Z0-9]+)?'


#Valor Boolean
#t_TRUE = r'true'
#t_FALSE = r'false'

#Operadores Comparación
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_IS_EQUAL = r'=='
t_IS_IDENTICAL = r'==='
t_IS_NOT_EQUAL= r'!='
t_IS_NOT_IDENTICAL= r'!=='
t_IS_GREATER_OR_EQUAL=r'>='
t_IS_SMALLER_OR_EQUAL=r'<='
t_SPACESHIP = r'<=>'

t_ignore = ' \t'

#Número
def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


#Cadena de texto


#Palabras reservadas
def t_CLASS(t):
    r'class'
    return t
def t_ECHO(t):
    r'echo'
    return t
def t_NEW(t):
    r'new'
    return t
'''
def t_BOOLEAN(t):
    r'boolean'
    return t
def t_STRING(t):
    r'string'
    return t
'''
def t_TRUE(t):
    r'true'
    return t
def t_FALSE(t):
    r'false'
    return t
def t_NULL(t):
    r'null'
    return t
'''
def t_OBJECT(t):
    r'object'
    return t
'''
def t_BREAK(t):
    r'break'
    return t
def t_CONTINUE(t):
    r'continue'
    return t
def t_RETURN(t):
    r'return'
    return t
def t_FUNCTION(t):
    r'function'
    return t
def t_AS(t):
    r'as'
    return t
#Sentencia if
def t_IF(t):
    r'if'
    return t
def t_ELSE(t):
    r'else'
    return t
def t_ELSEIF(t):
    r'elseif'
    return t

#Lazo
def t_FOREACH(t):
    r'foreach'
    return t

def t_WHILE(t):
    r'while'
    return t

#Funciones print
def t_PRINT(t):
    r'print'
    return t
def t_PRINT_R(t):
    r'print_r'
    return t
def t_VAR_DUMP(t):
    r'var_dump'
    return t

#Funciones
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
def t_ARRAY(t):
    r'array'
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
def t_UNSET(t):
    r'unset'
    return t
def t_VAR_EXPORT(t):
    r'var_export'
    return t
def t_SHUFFLE(t):
    r'shuffle'
    return t
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

#Nombre de funciones
def t_FNOMBRE(t):
    r'(?!or|and|xor)([a-z]|[A-Z])([a-zA-Z0-9_]+)?'
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

archivo= open("archivo.txt")
for linea in archivo:
    #print(">>"+linea)
    #analizar(linea)
    if len(linea)==0:
        break
def ImprimirAnalizar(dato):
    texto= dato.split("\n")
    cadena=""
    for i in texto:
        cadena+= "-> "+i
        lexer.input(i)
        while True:
            tok = lexer.token()
            if not tok:
                break
            cadena+="\n"
            cadena+=str(tok)
        cadena+="\n"
    return cadena
