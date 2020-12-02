import ply.yacc as yacc
from past.builtins import raw_input
import lexicoLP

from lexicoLP import tokens

def p_programa(p):
    'programa : OPEN declaracion CLOSE'

#KEVIN CEVALLOS
def p_declaracion(p):
    '''declaracion : expression
                        | expif
                        | expelse
                        | expresionlogica
                        | declararvariable
                        | definir_array
                        | creacionfunciones
                        | returnvalores
                        | operador_object
                        | print
                        | arreglos
                        | while
                        | foreach
                        | clase'''

#JOFFRE RAMIREZ
def p_creacionfunciones(p):
    '''creacionfunciones : FUNCTION FNOMBRE LPAREN RPAREN LCORCHET declaracion RCORCHET '''

def p_empty(p):
    'empty : '

def p_argumentos(p):
    '''argumentos :   ID
                    | empty'''

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
                    | ID
                    | DECIMAL'''

#KEVIN CEVALLOS
def p_expif(p):
    'expif : funcion_condicion LPAREN comparacion RPAREN LCORCHET declaracion RCORCHET'

def p_expelse(p):
    'expelse : expif ELSE LCORCHET declaracion RCORCHET'

def p_funcion_condicion(p):
    '''funcion_condicion : IF
                          | ELSEIF'''

def p_control_bucle(p):
    '''control_bucle : BREAK
                        | CONTINUE
                        | declaracion'''

def p_while(p):
    'while : WHILE LPAREN comparacion RPAREN LCORCHET control_bucle RCORCHET'

def p_foreach(p):
    'foreach : FOREACH LPAREN array AS ID RPAREN LCORCHET control_bucle RCORCHET'

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

'''
#KEVIN CEVALLOS
def p_funecho(p):
    'funecho : ECHO TEXT END'
'''

def p_expresionlogica(p):
    'expresionlogica : ID operadorlogico ID'

def p_operadorlogico(p):
    '''operadorlogico : AND
                        | OR
                        | XOR
                        | NOT '''


def p_declararvariable(p):
    ''' declararvariable : ID EQUALS NUMBER
                                    | boolean
                                    | TEXT
                                    | NULL
                                    | archivos
                                    | array
                                    | new'''
#JOFFRE RAMIREZ
def p_boolean(p):
    '''boolean : TRUE
                | FALSE'''

def p_operador_object(p):
    'operador_object : ID EQUALS OBJECT_OPERATOR FNOMBRE LPAREN argumentos RPAREN END'

def p_definir_array(p):
    'definir_array : array END'

def p_array(p):
    'array : ARRAY LPAREN termino RPAREN'

def p_new(p):
    'new : NEW FNOMBRE END'

'''
#JOFFRE RAMIREZ
def p_pp(p):
    'pp : ID EQUALS ARRAY LPAREN TEXT RPAREN END'


#KEVIN CEVALLOS
def p_funprint(p):
    'funprint : PRINT LPAREN TEXT RPAREN END'

'''

def p_print(p):
    'print : funcion_print LPAREN ID RPAREN END'

def p_funcion_print(p):
    '''funcion_print : VAR_EXPORT
                       | ECHO
                        |  PRINT
                        | PRINT_R
                        | VAR_DUMP'''

def p_arreglos(p):
    'arreglos : funcion_arreglo LPAREN ID RPAREN'

def p_funcion_arreglo(p):
    '''funcion_arreglo :  SUFFLE
                        | ARRAY_MERGE
                        | ARRAY_SEARCH
                        | ARRAY_RAND
                        | ARRAY_CHUNK
                        | STR_SPLIT
                        | PREG_SPLIT
                        | ARRAY_UNIQUE
                         | COUNT
                         | SIZEOF
                         | ARRAY_PUSH
                         | SORT
                         | ASORT
                         | KSORT
                         | UNSET
                         | IMPLODE
                        | EXPLODE '''

def p_archivos(p):
    'archivos : funcion_archivo LPAREN TEXT COMA TEXT RPAREN'

def p_funcion_archivo(p):
    '''funcion_archivo : FGETS
                    | FREAD
                    | FSCANF
                    | FPASSTHRU
                    | FGETCSV
                    | FGETC
                    | FILE_GET_CONTENTS
                    | READFILE
                    | FILE
                    | PARSE_INI_FILE
                    '''

def p_clase(p):
    'clase : CLASS FNOMBRE LCORCHET declaracion RCORCHET'

VERBOSE = 1

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(lexicoLP.lexer.lineno))
	else:
		raise Exception('syntax', 'error')


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

def ImprimirSintactico(texto):
        s = texto
        result = parser.parse(s)
        print(result)