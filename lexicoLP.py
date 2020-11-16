#Kevin Antonio Cevallos Pilay PHP-2

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
    'var_dump': 'VAR_DUMP'
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
    'ID'] + list(reserved.values()))



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
t_END=r';'


t_OPEN = r'<\?php'
t_CLOSE = r'\?>'
t_AND = r'and'
t_OR = r'or'
t_XOR = r'xor'
t_NOT = r'!'

T_IS_EQUAL = r'\=='
T_IS_IDENTICAL = r'\==='
T_IS_NOT_EQUAL= r'\!='
T_IS_NOT_IDENTICAL= r'/!=='
T_IS_GREATER_OR_EQUAL=r'\>='
T_IS_SMALLER_OR_EQUAL=r'\<='
T_SPACESHIP = r'\<=>'

t_ignore = ' \t'



def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#def t_ID(t):
    #r'^$[a-zA-Z][a-zA-Z0-9]*;'
    #t.type = reserved.get(t.value, 'ID')
    #return t

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

def t_error(t):
    print("No es reconocido '%s'"%t.value[0])
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


#archivo = open("prueba.txt")
lexer=lex.lex()

data=''' 
<?php
$adfghj123dfghj=1 ; 
$b=2;
echo $a  / $b;
?>
if
else
or
xor
boolean
float
'''
lexer.input(data)

while True:
    tok=lexer.token()
    if not tok:
        break
    print(tok)
#for linea in archivo:
#    print(">>"+linea)


