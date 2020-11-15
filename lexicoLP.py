#Kevin Antonio Cevallos Pilay PHP-2

import ply.lex as lex
reserved = {
    'if': 'IF',
    'else': 'ElSE',
    'elseif': 'ElSEIF',
    'else if': 'ElSE IF',
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
}


tokens = {
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MAYORQUE',
    'MENORQUE',
    'EQUALS',
    'NAME',
    'AND',
    'OR',
    'XOR',
    'NOT',
    'OPEN',
    'CLOSE'
}

t_PLUS=r'\+'
t_MINUS=r'-'
t_TIMES=r'\*'
t_DIVIDE=r'/'
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_EQUALS = r'='
t_NAME = r'^\$[a-zA-Z_][a-zA-Z0-9_]*'
t_ignore = r' \t'
t_OPEN = r'<?php'
t_CLOSE = r'?>'
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

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'^\$[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t



archivo = open("prueba.txt")
for linea in archivo:
    print(">>"+linea)
    analizar(linea)
    if len(linea)==0:
        break