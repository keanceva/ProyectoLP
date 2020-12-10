import ply.yacc as yacc
#from past.builtins import raw_input
import lexicoLP


from lexicoLP import tokens

resultado_gramatica = []

def p_programa(p):
    '''programa : OPEN  declaracion CLOSE
                    | OPEN declaracion
                    | declaracion CLOSE
                    | declaracion
                    | CLOSE
                    | OPEN'''

#KEVIN CEVALLOS
def p_declaracion(p):
    '''declaracion :  expression
                        | expif
                        | expelse
                        | expresionlogica
                        | declararvariable
                        | creacionfunciones
                        | returnvalores
                        | operador_object
                        | print
                        | arreglos
                        | while
                        | foreach
                        | clase
                        | declaracion'''

#JOFFRE RAMIREZ

def p_creacionfunciones(p):
    '''creacionfunciones : FUNCTION FNOMBRE LPAREN RPAREN LCORCHET declaracion RCORCHET
                            | FUNCTION FNOMBRE LPAREN RPAREN LCORCHET
                            | declaracion RCORCHET
                            | declaracion
                            | RCORCHET'''

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
    'expression : ID EQUALS operacion_matematica END'

def p_operacion_matematica(p):
    '''operacion_matematica :  termino operadores operacion_matematica
                                | termino operadores termino
    '''
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
    '''expif : funcion_condicion LPAREN comparacion RPAREN LCORCHET declaracion RCORCHET
                | funcion_condicion LPAREN comparacion RPAREN LCORCHET
                | declaracion RCORCHET
                | declaracion
                | RCORCHET'''

def p_expelse(p):
    '''expelse : expif ELSE LCORCHET declaracion RCORCHET
                | expif ELSE LCORCHET declaracion
                | expif ELSE LCORCHET
                | declaracion
                | declaracion RCORCHET
                | RCORCHET'''

def p_funcion_condicion(p):
    '''funcion_condicion : IF
                          | ELSEIF'''

def p_control_bucle(p):
    '''control_bucle : declaracion
                        | BREAK
                        | CONTINUE
                        '''

def p_while(p):
    '''while : WHILE LPAREN comparacion RPAREN LCORCHET control_bucle RCORCHET
                | WHILE LPAREN comparacion RPAREN LCORCHET
                | control_bucle RCORCHET
                | control_bucle
                | RCORCHET'''

def p_foreach(p):
    '''foreach : FOREACH LPAREN ID AS ID RPAREN LCORCHET declaracion RCORCHET
                | FOREACH LPAREN ID AS ID RPAREN LCORCHET
                | control_bucle RCORCHET
                | control_bucle
                | RCORCHET '''

#MARIA CAMILA NAVARRO
def p_comparacion(p):
    '''comparacion : valor_comparado operadorcomparacion valor_comparado
                    | boolean'''

def p_valor_comparado(p):
    '''valor_comparado : NUMBER
                        | boolean
                        | operacion_matematica
                        | ID'''

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
                            | MENORQUE'''

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
    'declararvariable : ID EQUALS tipo END '


def p_tipo(p):
    '''tipo : boolean
            | NUMBER
            | TEXT
            | NULL
            | archivos
            | array
            | new '''
#JOFFRE RAMIREZ
def p_boolean(p):
    '''boolean : TRUE
                | FALSE
                | expresionlogica'''

def p_operador_object(p):
    'operador_object : ID EQUALS OBJECT_OPERATOR FNOMBRE LPAREN argumentos RPAREN END'

def p_array(p):
    'array : ARRAY LPAREN valores_array RPAREN '

def p_valores_array(p):
      '''valores_array : elementos_array COMA valores_array
                          | elementos_array
                          | empty
      '''

def p_flecha_array(p):
    'flecha_array : elementos_array FLECHA elementos_array'

def p_elementos_array(p):
    '''elementos_array : NUMBER
                          | TEXT
                          | empty
                          | boolean
                          | array
                          | flecha_array
    '''

def p_new(p):
    'new : NEW FNOMBRE '

'''
#JOFFRE RAMIREZ
def p_pp(p):
    'pp : ID EQUALS ARRAY LPAREN TEXT RPAREN END'


#KEVIN CEVALLOS
def p_funprint(p):
    'funprint : PRINT LPAREN TEXT RPAREN END'

'''

def p_print(p):
    '''print : funcion_print LPAREN argument RPAREN END
                | funcion_print argument END
                | ECHO LPAREN valores_echo RPAREN END
                | ECHO valores_echo END'''

def p_argument(p):
    '''argument : ID
                    | TEXT
                    | operacion_matematica
                    | comparacion'''

def p_valores_echo(p):
    ''' valores_echo : argument COMA valores_echo
                        | argument
                        '''

def p_funcion_print(p):
    '''funcion_print : VAR_EXPORT
                       | ECHO
                        |  PRINT
                        | PRINT_R
                        | VAR_DUMP'''

def p_arreglos(p):
    'arreglos : funcion_arreglo LPAREN ID RPAREN'

def p_argumento_doble(p):
    '''argumento_doble : LPAREN ID COMA ID RPAREN'''

def p_funcion_argumento_doble(p):
    '''funcion_argumento_doble :   ARRAY_MERGE
                                    | ARRAY_SEARCH
                                    | ARRAY_RAND
                                    | ARRAY_CHUNK
                                    | STR_SPLIT
                                    | PREG_SPLIT
                                     | COUNT
                                     | ARRAY_PUSH
                                     | SORT
                                     | ASORT
                                     | KSORT
                                     | UNSET
                                     | IMPLODE
                                    | EXPLODE '''

def p_funcion_arreglo(p):
    '''funcion_arreglo :  SUFFLE
                        | ARRAY_UNIQUE
                         | SIZEOF '''

def p_archivos(p):
    '''archivos : funcion_corta
                    | estructura_funcion'''

def p_funcion_corta(p):
    'funcion_corta : FGETS LPAREN ID COMA NUMBER RPAREN'

def p_estructura_funcion(p):
    'estructura_funcion : funcion_archivo LPAREN opcion RPAREN'

def p_opcion(p):
    '''opcion : ID
                | TEXT'''

def p_funcion_archivo(p):
    '''funcion_archivo :  FREAD
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
    '''clase : CLASS FNOMBRE LCORCHET declaracion RCORCHET
                | CLASS FNOMBRE LCORCHET
                | declaracion RCORCHET
                | declaracion
                | RCORCHET '''


def p_error(p):
    global resultado_gramatica
    if p:
        resultado = "Error sintactico de tipo {} en el valor {}".format(str(p.type), str(p.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(p)
        print(resultado)
    resultado_gramatica.append(resultado)

# Build the parser
parser = yacc.yacc()
'''
while True:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
'''
def ImprimirSintactico(dato):
    while True:
        try:
            s = dato
        except EOFError:
            break
        if not s: continue
        result = str(parser.parse(s))
        return(result)

def prueba_sintactica(data):
    #global resultado_gramatica
    resultado_gramatica.clear()
    linea=1
    contador=len(resultado_gramatica)
    #gram = parser.parse(data)

    for item in data.split("\n"):

        if item:
            gram = parser.parse(item)
            if (contador<len(resultado_gramatica)):
                resultado_gramatica[-1]= str(linea)+"--> "+resultado_gramatica[-1]
                contador=len(resultado_gramatica)

            #if gram:
                #print("entra")
                #print(linea)
                #resultado_gramatica.append(linea)
                #str(gram))

        else: print("Dato vacío")

        linea+=1

    print("Resultado: ", resultado_gramatica)
    return resultado_gramatica

#<?php $var = 1+3; ?>
#<?php $var = new foo; ?>
#<?php echo("Hello wordl"); ?>
#<?php echo($var); ?>
#<?php $a = array(1);?>
#<?php function holamundo(){ echo ("Hola mundo");}?>
#<?php if ($x > $y) { echo ("$x es mayor que $y"); } ?>
#<?php if ($x > $y) { echo ("$x es mayor que $y");} else {echo ("$y es mayor que $x");} ?>
#<?php foreach ($array as $valor) { $valor = $valor * 2;} ?>
#<?php while ($array == $valor) { $valor = $valor * 2;} ?>
#<?php $a = array(class);?>
#<?php class Foo { $aMemberVar = "aMemberVar Member Variable";} ?>
#<?php $a= array("metodo"); ?>

