import ply.yacc as yacc
from past.builtins import raw_input

from lexicoLP import tokens

def p_programa(p):
    'programa : OPEN declaracion CLOSE'

#KEVIN CEVALLOS
def p_declaracion(p):
    '''declaracion : expression
                        | expif
                        | expresionlogica
                        | declararvariable
                        | array
                        | creacionfunciones
                        | returnvalores



                       '''

#JOFFRE RAMIREZ
def p_creacionfunciones(p):
    '''creacionfunciones : FUNCTION FNOMBRE LPAREN RPAREN LCORCHET declaracion RCORCHET '''

def p_argumentos(p):
    '''argumentos :   ID
                    | empty

                    '''
#JOFFRE RAMIREZ
def p_returnvalores(p):
    '''returnvalores :  RETURN termino END
                      | RETURN creacionfunciones
                      | empty '''

#KEVIN CEVALLOS
def p_expression_math(p):
    'expression : termino operadores termino'


#KEVIN CEVALLOS
def p_operadores(p):
    '''operadores : PLUS
                    | MINUS
                    | DIVIDE
                    | TIMES
                    | MODULO'''

#JOFFRE RAMIREZ
def p_termino(p):
    '''termino : NUMBER
                    | ID'''
#KEVIN CEVALLOS
def p_expif(p):
    'expif : IF LPAREN comparacion RPAREN LCORCHET expression RCORCHET'

#MARIA CAMILA NAVARRO
def p_comparacion(p):
    'comparacion : termino operadorcomparacion termino'

#MARIA CAMILA NAVARRO
def p_operadorcomparacion(p):
    '''operadorcomparacion : IS_EQUAL
                            | IS_IDENTICAL
                            | IS_NOT_EQUAL
                            | IS_NOT_IDENTICAL
                            | IS_GREATER_OR_EQUAL
                            | IS_SMALLER_OR_EQUAL
                            | SPACESHIP
                            | MAYORQUE
                            | MENORQUE '''
#KEVIN CEVALLOS
def p_funecho(p):
    'funecho : ECHO TEXT END'

#KEVIN CEVALLOS
def p_funprint(p):
    'funprint : PRINT LPAREN TEXT RPAREN END'


def p_fgets(p):
    'fgets : FPASSTHRU LPAREN ID COMA NUMBER RPAREN'

def p_fpassthru(p):
    'fpassthru : FGETS LPAREN ID RPAREN'

def p_expresionlogica(p):
    'expresionlogica : ID operadorlogico ID'

def p_operadorlogico(p):
    '''operadorlogico : AND
                        | OR
                        | XOR
                        | NOT '''


def p_declararvariable(p):
    ''' declararvariable : ID EQUALS NUMBER
                         | ID EQUALS boolean
                         | ID EQUALS TEXT
                         | ID EQUALS NULL
                         '''
#JOFFRE RAMIREZ
def p_boolean(p):
    '''boolean : TRUE
                | FALSE'''


#JOFFRE RAMIREZ
def p_array(p):
    'array : ID EQUALS ARRAY LPAREN TEXT RPAREN END'



def p_error(p):
    print("Syntax error in input!")

def p_empty(p):
  '''empty :
  '''



# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
