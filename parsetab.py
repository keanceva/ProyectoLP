
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARRAY ARRAY_CHUNK ARRAY_MERGE ARRAY_PUSH ARRAY_RAND ARRAY_SEARCH ARRAY_UNIQUE AS ASORT BREAK CLASS CLOSE COMA CONTINUE COUNT DECIMAL DIVIDE ECHO ELSE ELSEIF END EQUALS EXPLODE FALSE FGETC FGETCSV FGETS FILE FILE_GET_CONTENTS FLECHA FNOMBRE FOREACH FPASSTHRU FREAD FSCANF FUNCTION ID IF IMPLODE IS_EQUAL IS_GREATER_OR_EQUAL IS_IDENTICAL IS_NOT_EQUAL IS_NOT_IDENTICAL IS_SMALLER_OR_EQUAL KSORT LCORCHET LPAREN MAYORQUE MENORQUE MINUS MODULO NEW NOT NULL NUMBER OBJECT_OPERATOR OPEN OR PARSE_INI_FILE PLUS PREG_SPLIT PRINT PRINT_R RCORCHET READFILE RETURN RPAREN SIZEOF SORT SPACESHIP STR_SPLIT SUFFLE TEXT TIMES TRUE UNSET VAR_DUMP VAR_EXPORT WHILE XORprograma : OPEN  declaracion CLOSE\n                    | OPEN declaracion\n                    | declaracion CLOSE\n                    | declaracion\n                    | CLOSE\n                    | OPENdeclaracion :  expression\n                        | expif\n                        | expelse\n                        | expresionlogica\n                        | declararvariable\n                        | creacionfunciones\n                        | returnvalores\n                        | operador_object\n                        | print\n                        | arreglos\n                        | while\n                        | foreach\n                        | clase\n                        | declaracioncreacionfunciones : FUNCTION FNOMBRE LPAREN RPAREN LCORCHET declaracion RCORCHET\n                            | FUNCTION FNOMBRE LPAREN RPAREN LCORCHET\n                            | declaracion RCORCHET\n                            | declaracion\n                            | RCORCHETempty : argumentos :   ID\n                    | emptyreturnvalores :  RETURN termino END\n                      | RETURN creacionfunciones\n                      | empty expression : ID EQUALS operacion_matematica ENDoperacion_matematica :  termino operadores operacion_matematica\n                                | termino operadores termino\n    operadores : PLUS\n                    | MINUS\n                    | DIVIDE\n                    | TIMES\n                    | MODULOtermino : NUMBER\n                    | ID\n                    | DECIMALexpif : funcion_condicion LPAREN comparacion RPAREN LCORCHET declaracion RCORCHET\n                | funcion_condicion LPAREN comparacion RPAREN LCORCHET\n                | declaracion RCORCHET\n                | declaracion\n                | RCORCHETexpelse : expif ELSE LCORCHET declaracion RCORCHET\n                | expif ELSE LCORCHET declaracion\n                | expif ELSE LCORCHET\n                | declaracion\n                | declaracion RCORCHET\n                | RCORCHETfuncion_condicion : IF\n                          | ELSEIFcontrol_bucle : declaracion\n                        | BREAK\n                        | CONTINUE\n                        while : WHILE LPAREN comparacion RPAREN LCORCHET control_bucle RCORCHET\n                | WHILE LPAREN comparacion RPAREN LCORCHET\n                | control_bucle RCORCHET\n                | control_bucle\n                | RCORCHETforeach : FOREACH LPAREN ID AS ID RPAREN LCORCHET declaracion RCORCHET\n                | FOREACH LPAREN ID AS ID RPAREN LCORCHET\n                | control_bucle RCORCHET\n                | control_bucle\n                | RCORCHET comparacion : valor_comparado operadorcomparacion valor_comparado\n                    | booleanvalor_comparado : NUMBER\n                        | boolean\n                        | operacion_matematica\n                        | IDoperadorcomparacion : IS_EQUAL\n                            | IS_IDENTICAL\n                            | IS_NOT_EQUAL\n                            | IS_NOT_IDENTICAL\n                            | IS_GREATER_OR_EQUAL\n                            | IS_SMALLER_OR_EQUAL\n                            | SPACESHIP\n                            | MAYORQUE\n                            | MENORQUEexpresionlogica : ID operadorlogico IDoperadorlogico : AND\n                        | OR\n                        | XOR\n                        | NOT declararvariable : ID EQUALS tipo END tipo : boolean\n            | NUMBER\n            | TEXT\n            | NULL\n            | archivos\n            | array\n            | new boolean : TRUE\n                | FALSE\n                | expresionlogicaoperador_object : ID EQUALS OBJECT_OPERATOR FNOMBRE LPAREN argumentos RPAREN ENDarray : ARRAY LPAREN valores_array RPAREN valores_array : elementos_array COMA valores_array\n                          | elementos_array\n                          | empty\n      flecha_array : elementos_array FLECHA elementos_arrayelementos_array : NUMBER\n                          | TEXT\n                          | empty\n                          | boolean\n                          | array\n                          | flecha_array\n    new : NEW FNOMBRE print : funcion_print LPAREN argument RPAREN END\n                | funcion_print argument END\n                | ECHO LPAREN valores_echo RPAREN END\n                | ECHO valores_echo ENDargument : ID\n                    | TEXT\n                    | operacion_matematica\n                    | comparacion valores_echo : argument COMA valores_echo\n                        | argument\n                        funcion_print : VAR_EXPORT\n                       | ECHO\n                        |  PRINT\n                        | PRINT_R\n                        | VAR_DUMParreglos : funcion_arreglo LPAREN ID RPARENargumento_doble : LPAREN ID COMA ID RPARENfuncion_argumento_doble :   ARRAY_MERGE\n                                    | ARRAY_SEARCH\n                                    | ARRAY_RAND\n                                    | ARRAY_CHUNK\n                                    | STR_SPLIT\n                                    | PREG_SPLIT\n                                     | COUNT\n                                     | ARRAY_PUSH\n                                     | SORT\n                                     | ASORT\n                                     | KSORT\n                                     | UNSET\n                                     | IMPLODE\n                                    | EXPLODE funcion_arreglo :  SUFFLE\n                        | ARRAY_UNIQUE\n                         | SIZEOF archivos : funcion_corta\n                    | estructura_funcionfuncion_corta : FGETS LPAREN ID COMA NUMBER RPARENestructura_funcion : funcion_archivo LPAREN opcion RPARENopcion : ID\n                | TEXTfuncion_archivo :  FREAD\n                    | FSCANF\n                    | FPASSTHRU\n                    | FGETCSV\n                    | FGETC\n                    | FILE_GET_CONTENTS\n                    | READFILE\n                    | FILE\n                    | PARSE_INI_FILE\n                    clase : CLASS FNOMBRE LCORCHET declaracion RCORCHET\n                | CLASS FNOMBRE LCORCHET\n                | declaracion RCORCHET\n                | declaracion\n                | RCORCHET '
    
_lr_action_items = {'OPEN':([0,],[2,]),'CLOSE':([0,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,20,22,23,28,40,41,42,44,55,59,60,79,83,110,116,117,119,137,142,143,144,145,161,165,180,181,182,183,184,186,205,206,207,208,209,212,],[4,-26,43,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-25,-26,-31,-62,-57,-58,82,-23,-12,-20,-25,-61,-26,-84,-29,-23,-114,-116,-163,-20,-32,-89,-128,-23,-44,-22,-113,-115,-60,-162,-43,-21,-59,-65,-100,-64,]),'ID':([0,2,22,24,25,33,34,35,36,46,47,48,49,50,51,52,61,74,77,78,80,83,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,138,142,147,149,150,163,166,180,181,184,191,192,208,],[18,18,57,63,63,-123,-125,-126,-127,84,110,-85,-86,-87,-88,114,63,63,139,114,141,18,156,-35,-36,-37,-38,-39,114,-75,-76,-77,-78,-79,-80,-81,-82,-83,63,18,175,176,178,185,187,18,18,18,175,175,18,]),'RCORCHET':([0,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,20,22,23,28,40,41,42,44,55,59,60,79,83,110,116,117,119,137,142,143,144,145,161,164,165,180,181,182,183,184,186,195,196,197,198,205,206,207,208,209,211,212,],[20,20,44,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-25,60,-31,79,-57,-58,44,-23,-12,117,-25,-61,20,-84,-29,-23,-114,-116,20,165,-32,-89,-128,186,-23,20,20,-113,-115,20,-23,205,206,207,44,-23,-21,-59,20,-100,212,-23,]),'FUNCTION':([0,2,22,83,142,180,181,184,208,],[21,21,21,21,21,21,21,21,21,]),'RETURN':([0,2,22,83,142,180,181,184,208,],[22,22,22,22,22,22,22,22,22,]),'ECHO':([0,2,22,83,142,180,181,184,208,],[25,25,25,25,25,25,25,25,25,]),'WHILE':([0,2,22,83,142,180,181,184,208,],[27,27,27,27,27,27,27,27,27,]),'FOREACH':([0,2,22,83,142,180,181,184,208,],[29,29,29,29,29,29,29,29,29,]),'CLASS':([0,2,22,83,142,180,181,184,208,],[30,30,30,30,30,30,30,30,30,]),'IF':([0,2,22,83,142,180,181,184,208,],[31,31,31,31,31,31,31,31,31,]),'ELSEIF':([0,2,22,83,142,180,181,184,208,],[32,32,32,32,32,32,32,32,32,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,22,23,28,40,41,42,43,44,55,59,60,79,82,83,110,116,117,119,137,142,143,144,145,161,165,180,181,182,183,184,186,205,206,207,208,209,212,],[-26,0,-6,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-25,-26,-31,-62,-57,-58,-2,-3,-23,-12,-20,-25,-61,-1,-26,-84,-29,-23,-114,-116,-163,-20,-32,-89,-128,-23,-44,-22,-113,-115,-60,-162,-43,-21,-59,-65,-100,-64,]),'ELSE':([0,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,20,22,23,28,40,41,42,44,55,59,60,79,83,110,116,117,119,137,142,143,144,145,161,164,165,180,181,182,183,184,186,195,196,197,198,205,206,207,208,209,211,212,],[-26,-26,-20,-7,45,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-25,-26,-31,-62,-57,-58,-20,-23,-12,-20,-25,-61,-26,-84,-29,-23,-114,-116,-26,-20,-32,-89,-128,-20,-23,-26,-22,-113,-115,-26,-23,-20,-20,-62,-20,-23,-21,-59,-26,-100,-20,-23,]),'VAR_EXPORT':([0,2,22,83,142,180,181,184,208,],[33,33,33,33,33,33,33,33,33,]),'PRINT':([0,2,22,83,142,180,181,184,208,],[34,34,34,34,34,34,34,34,34,]),'PRINT_R':([0,2,22,83,142,180,181,184,208,],[35,35,35,35,35,35,35,35,35,]),'VAR_DUMP':([0,2,22,83,142,180,181,184,208,],[36,36,36,36,36,36,36,36,36,]),'SUFFLE':([0,2,22,83,142,180,181,184,208,],[37,37,37,37,37,37,37,37,37,]),'ARRAY_UNIQUE':([0,2,22,83,142,180,181,184,208,],[38,38,38,38,38,38,38,38,38,]),'SIZEOF':([0,2,22,83,142,180,181,184,208,],[39,39,39,39,39,39,39,39,39,]),'BREAK':([0,2,22,83,142,180,181,184,208,],[40,40,40,40,40,40,40,40,40,]),'CONTINUE':([0,2,22,83,142,180,181,184,208,],[41,41,41,41,41,41,41,41,41,]),'EQUALS':([18,57,],[46,46,]),'AND':([18,57,63,84,114,175,],[48,48,48,48,48,48,]),'OR':([18,57,63,84,114,175,],[49,49,49,49,49,49,]),'XOR':([18,57,63,84,114,175,],[50,50,50,50,50,50,]),'NOT':([18,57,63,84,114,175,],[51,51,51,51,51,51,]),'LPAREN':([19,24,25,26,27,29,31,32,33,34,35,36,37,38,39,53,97,99,100,101,102,103,104,105,106,107,108,109,146,],[52,61,74,77,78,80,-54,-55,-123,-125,-126,-127,-144,-145,-146,115,147,149,150,-153,-154,-155,-156,-157,-158,-159,-160,-161,166,]),'FNOMBRE':([21,30,87,98,],[53,81,146,148,]),'NUMBER':([22,24,25,33,34,35,36,46,52,61,74,78,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,138,147,191,192,193,],[56,70,70,-123,-125,-126,-127,89,112,70,70,112,56,-35,-36,-37,-38,-39,112,-75,-76,-77,-78,-79,-80,-81,-82,-83,70,170,170,170,204,]),'DECIMAL':([22,24,25,33,34,35,36,46,52,61,74,78,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,138,],[58,58,58,-123,-125,-126,-127,58,58,58,58,58,58,-35,-36,-37,-38,-39,58,-75,-76,-77,-78,-79,-80,-81,-82,-83,58,]),'TEXT':([24,25,33,34,35,36,46,61,74,138,147,150,191,192,],[64,64,-123,-125,-126,-127,90,64,64,64,171,179,171,171,]),'TRUE':([24,25,33,34,35,36,46,52,61,74,78,126,127,128,129,130,131,132,133,134,135,138,147,191,192,],[71,71,-123,-125,-126,-127,71,71,71,71,71,71,-75,-76,-77,-78,-79,-80,-81,-82,-83,71,71,71,71,]),'FALSE':([24,25,33,34,35,36,46,52,61,74,78,126,127,128,129,130,131,132,133,134,135,138,147,191,192,],[72,72,-123,-125,-126,-127,72,72,72,72,72,72,-75,-76,-77,-78,-79,-80,-81,-82,-83,72,72,72,72,]),'LCORCHET':([45,81,151,152,162,199,],[83,142,180,181,184,208,]),'OBJECT_OPERATOR':([46,],[87,]),'NULL':([46,],[91,]),'ARRAY':([46,147,191,192,],[97,97,97,97,]),'NEW':([46,],[98,]),'FGETS':([46,],[99,]),'FREAD':([46,],[101,]),'FSCANF':([46,],[102,]),'FPASSTHRU':([46,],[103,]),'FGETCSV':([46,],[104,]),'FGETC':([46,],[105,]),'FILE_GET_CONTENTS':([46,],[106,]),'READFILE':([46,],[107,]),'FILE':([46,],[108,]),'PARSE_INI_FILE':([46,],[109,]),'END':([54,56,57,58,62,63,64,65,66,69,71,72,73,75,76,85,86,88,89,90,91,92,93,94,95,96,110,112,113,114,148,153,154,155,156,157,158,159,160,190,194,200,210,],[116,-40,-41,-42,119,-117,-118,-119,-120,-70,-97,-98,-99,137,-122,144,145,-90,-91,-92,-93,-94,-95,-96,-147,-148,-84,-71,-73,-74,-112,182,-34,-33,-41,-69,-72,183,-121,-101,-150,209,-149,]),'PLUS':([56,58,63,67,70,84,89,112,114,154,156,],[-40,-42,-41,121,-40,-41,-40,-40,-41,121,-41,]),'MINUS':([56,58,63,67,70,84,89,112,114,154,156,],[-40,-42,-41,122,-40,-41,-40,-40,-41,122,-41,]),'DIVIDE':([56,58,63,67,70,84,89,112,114,154,156,],[-40,-42,-41,123,-40,-41,-40,-40,-41,123,-41,]),'TIMES':([56,58,63,67,70,84,89,112,114,154,156,],[-40,-42,-41,124,-40,-41,-40,-40,-41,124,-41,]),'MODULO':([56,58,63,67,70,84,89,112,114,154,156,],[-40,-42,-41,125,-40,-41,-40,-40,-41,125,-41,]),'IS_EQUAL':([56,58,63,65,68,69,70,71,72,73,110,112,113,114,154,155,156,],[-40,-42,-74,-73,127,-72,-71,-97,-98,-99,-84,-71,-73,-74,-34,-33,-41,]),'IS_IDENTICAL':([56,58,63,65,68,69,70,71,72,73,110,112,113,114,154,155,156,],[-40,-42,-74,-73,128,-72,-71,-97,-98,-99,-84,-71,-73,-74,-34,-33,-41,]),'IS_NOT_EQUAL':([56,58,63,65,68,69,70,71,72,73,110,112,113,114,154,155,156,],[-40,-42,-74,-73,129,-72,-71,-97,-98,-99,-84,-71,-73,-74,-34,-33,-41,]),'IS_NOT_IDENTICAL':([56,58,63,65,68,69,70,71,72,73,110,112,113,114,154,155,156,],[-40,-42,-74,-73,130,-72,-71,-97,-98,-99,-84,-71,-73,-74,-34,-33,-41,]),'IS_GREATER_OR_EQUAL':([56,58,63,65,68,69,70,71,72,73,110,112,113,114,154,155,156,],[-40,-42,-74,-73,131,-72,-71,-97,-98,-99,-84,-71,-73,-74,-34,-33,-41,]),'IS_SMALLER_OR_EQUAL':([56,58,63,65,68,69,70,71,72,73,110,112,113,114,154,155,156,],[-40,-42,-74,-73,132,-72,-71,-97,-98,-99,-84,-71,-73,-74,-34,-33,-41,]),'SPACESHIP':([56,58,63,65,68,69,70,71,72,73,110,112,113,114,154,155,156,],[-40,-42,-74,-73,133,-72,-71,-97,-98,-99,-84,-71,-73,-74,-34,-33,-41,]),'MAYORQUE':([56,58,63,65,68,69,70,71,72,73,110,112,113,114,154,155,156,],[-40,-42,-74,-73,134,-72,-71,-97,-98,-99,-84,-71,-73,-74,-34,-33,-41,]),'MENORQUE':([56,58,63,65,68,69,70,71,72,73,110,112,113,114,154,155,156,],[-40,-42,-74,-73,135,-72,-71,-97,-98,-99,-84,-71,-73,-74,-34,-33,-41,]),'COMA':([56,58,63,64,65,66,69,71,72,73,76,110,112,113,114,147,154,155,156,157,158,168,169,170,171,172,173,174,176,190,191,192,202,203,],[-40,-42,-117,-118,-119,-120,-70,-97,-98,-99,138,-84,-71,-73,-74,-26,-34,-33,-41,-69,-72,191,-108,-106,-107,-109,-110,-111,193,-101,-26,-26,-105,-108,]),'RPAREN':([56,58,63,64,65,66,69,71,72,73,76,110,111,112,113,114,115,118,136,139,140,147,154,155,156,157,158,160,166,167,168,169,170,171,172,173,174,177,178,179,185,187,188,189,190,191,192,201,202,203,204,],[-40,-42,-117,-118,-119,-120,-70,-97,-98,-99,-122,-84,151,-71,-73,-74,152,153,159,161,162,-26,-34,-33,-41,-69,-72,-121,-26,190,-103,-104,-106,-107,-109,-110,-111,194,-151,-152,199,-27,200,-28,-101,-26,-26,-102,-105,-108,210,]),'FLECHA':([71,72,73,110,147,168,169,170,171,172,173,174,190,191,192,202,203,],[-97,-98,-99,-84,-26,192,-108,-106,-107,-109,-110,-111,-101,-26,-26,192,-108,]),'AS':([141,],[163,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'declaracion':([0,2,22,83,142,180,181,184,208,],[3,42,59,143,164,195,196,198,211,]),'expression':([0,2,22,83,142,180,181,184,208,],[5,5,5,5,5,5,5,5,5,]),'expif':([0,2,22,83,142,180,181,184,208,],[6,6,6,6,6,6,6,6,6,]),'expelse':([0,2,22,83,142,180,181,184,208,],[7,7,7,7,7,7,7,7,7,]),'expresionlogica':([0,2,22,24,25,46,52,61,74,78,83,126,138,142,147,180,181,184,191,192,208,],[8,8,8,73,73,73,73,73,73,73,8,73,73,8,73,8,8,8,73,73,8,]),'declararvariable':([0,2,22,83,142,180,181,184,208,],[9,9,9,9,9,9,9,9,9,]),'creacionfunciones':([0,2,22,83,142,180,181,184,208,],[10,10,55,10,10,10,10,10,10,]),'returnvalores':([0,2,22,83,142,180,181,184,208,],[11,11,11,11,11,11,11,11,11,]),'operador_object':([0,2,22,83,142,180,181,184,208,],[12,12,12,12,12,12,12,12,12,]),'print':([0,2,22,83,142,180,181,184,208,],[13,13,13,13,13,13,13,13,13,]),'arreglos':([0,2,22,83,142,180,181,184,208,],[14,14,14,14,14,14,14,14,14,]),'while':([0,2,22,83,142,180,181,184,208,],[15,15,15,15,15,15,15,15,15,]),'foreach':([0,2,22,83,142,180,181,184,208,],[16,16,16,16,16,16,16,16,16,]),'clase':([0,2,22,83,142,180,181,184,208,],[17,17,17,17,17,17,17,17,17,]),'funcion_condicion':([0,2,22,83,142,180,181,184,208,],[19,19,19,19,19,19,19,19,19,]),'empty':([0,2,22,83,142,147,166,180,181,184,191,192,208,],[23,23,23,23,23,169,189,23,23,23,169,203,23,]),'funcion_print':([0,2,22,83,142,180,181,184,208,],[24,24,24,24,24,24,24,24,24,]),'funcion_arreglo':([0,2,22,83,142,180,181,184,208,],[26,26,26,26,26,26,26,26,26,]),'control_bucle':([0,2,22,83,142,180,181,184,208,],[28,28,28,28,28,28,28,197,28,]),'operadorlogico':([18,57,63,84,114,175,],[47,47,47,47,47,47,]),'termino':([22,24,25,46,52,61,74,78,120,126,138,],[54,67,67,67,67,67,67,67,154,67,67,]),'argument':([24,25,61,74,138,],[62,76,118,76,76,]),'operacion_matematica':([24,25,46,52,61,74,78,120,126,138,],[65,65,85,113,65,65,113,155,113,65,]),'comparacion':([24,25,52,61,74,78,138,],[66,66,111,66,66,140,66,]),'valor_comparado':([24,25,52,61,74,78,126,138,],[68,68,68,68,68,68,157,68,]),'boolean':([24,25,46,52,61,74,78,126,138,147,191,192,],[69,69,88,69,69,69,69,158,69,172,172,172,]),'valores_echo':([25,74,138,],[75,136,160,]),'tipo':([46,],[86,]),'archivos':([46,],[92,]),'array':([46,147,191,192,],[93,173,173,173,]),'new':([46,],[94,]),'funcion_corta':([46,],[95,]),'estructura_funcion':([46,],[96,]),'funcion_archivo':([46,],[100,]),'operadores':([67,154,],[120,120,]),'operadorcomparacion':([68,],[126,]),'valores_array':([147,191,],[167,201,]),'elementos_array':([147,191,192,],[168,168,202,]),'flecha_array':([147,191,192,],[174,174,174,]),'opcion':([150,],[177,]),'argumentos':([166,],[188,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> OPEN declaracion CLOSE','programa',3,'p_programa','sintactico.py',11),
  ('programa -> OPEN declaracion','programa',2,'p_programa','sintactico.py',12),
  ('programa -> declaracion CLOSE','programa',2,'p_programa','sintactico.py',13),
  ('programa -> declaracion','programa',1,'p_programa','sintactico.py',14),
  ('programa -> CLOSE','programa',1,'p_programa','sintactico.py',15),
  ('programa -> OPEN','programa',1,'p_programa','sintactico.py',16),
  ('declaracion -> expression','declaracion',1,'p_declaracion','sintactico.py',20),
  ('declaracion -> expif','declaracion',1,'p_declaracion','sintactico.py',21),
  ('declaracion -> expelse','declaracion',1,'p_declaracion','sintactico.py',22),
  ('declaracion -> expresionlogica','declaracion',1,'p_declaracion','sintactico.py',23),
  ('declaracion -> declararvariable','declaracion',1,'p_declaracion','sintactico.py',24),
  ('declaracion -> creacionfunciones','declaracion',1,'p_declaracion','sintactico.py',25),
  ('declaracion -> returnvalores','declaracion',1,'p_declaracion','sintactico.py',26),
  ('declaracion -> operador_object','declaracion',1,'p_declaracion','sintactico.py',27),
  ('declaracion -> print','declaracion',1,'p_declaracion','sintactico.py',28),
  ('declaracion -> arreglos','declaracion',1,'p_declaracion','sintactico.py',29),
  ('declaracion -> while','declaracion',1,'p_declaracion','sintactico.py',30),
  ('declaracion -> foreach','declaracion',1,'p_declaracion','sintactico.py',31),
  ('declaracion -> clase','declaracion',1,'p_declaracion','sintactico.py',32),
  ('declaracion -> declaracion','declaracion',1,'p_declaracion','sintactico.py',33),
  ('creacionfunciones -> FUNCTION FNOMBRE LPAREN RPAREN LCORCHET declaracion RCORCHET','creacionfunciones',7,'p_creacionfunciones','sintactico.py',38),
  ('creacionfunciones -> FUNCTION FNOMBRE LPAREN RPAREN LCORCHET','creacionfunciones',5,'p_creacionfunciones','sintactico.py',39),
  ('creacionfunciones -> declaracion RCORCHET','creacionfunciones',2,'p_creacionfunciones','sintactico.py',40),
  ('creacionfunciones -> declaracion','creacionfunciones',1,'p_creacionfunciones','sintactico.py',41),
  ('creacionfunciones -> RCORCHET','creacionfunciones',1,'p_creacionfunciones','sintactico.py',42),
  ('empty -> <empty>','empty',0,'p_empty','sintactico.py',45),
  ('argumentos -> ID','argumentos',1,'p_argumentos','sintactico.py',48),
  ('argumentos -> empty','argumentos',1,'p_argumentos','sintactico.py',49),
  ('returnvalores -> RETURN termino END','returnvalores',3,'p_returnvalores','sintactico.py',53),
  ('returnvalores -> RETURN creacionfunciones','returnvalores',2,'p_returnvalores','sintactico.py',54),
  ('returnvalores -> empty','returnvalores',1,'p_returnvalores','sintactico.py',55),
  ('expression -> ID EQUALS operacion_matematica END','expression',4,'p_expression_math','sintactico.py',59),
  ('operacion_matematica -> termino operadores operacion_matematica','operacion_matematica',3,'p_operacion_matematica','sintactico.py',62),
  ('operacion_matematica -> termino operadores termino','operacion_matematica',3,'p_operacion_matematica','sintactico.py',63),
  ('operadores -> PLUS','operadores',1,'p_operadores','sintactico.py',67),
  ('operadores -> MINUS','operadores',1,'p_operadores','sintactico.py',68),
  ('operadores -> DIVIDE','operadores',1,'p_operadores','sintactico.py',69),
  ('operadores -> TIMES','operadores',1,'p_operadores','sintactico.py',70),
  ('operadores -> MODULO','operadores',1,'p_operadores','sintactico.py',71),
  ('termino -> NUMBER','termino',1,'p_termino','sintactico.py',75),
  ('termino -> ID','termino',1,'p_termino','sintactico.py',76),
  ('termino -> DECIMAL','termino',1,'p_termino','sintactico.py',77),
  ('expif -> funcion_condicion LPAREN comparacion RPAREN LCORCHET declaracion RCORCHET','expif',7,'p_expif','sintactico.py',81),
  ('expif -> funcion_condicion LPAREN comparacion RPAREN LCORCHET','expif',5,'p_expif','sintactico.py',82),
  ('expif -> declaracion RCORCHET','expif',2,'p_expif','sintactico.py',83),
  ('expif -> declaracion','expif',1,'p_expif','sintactico.py',84),
  ('expif -> RCORCHET','expif',1,'p_expif','sintactico.py',85),
  ('expelse -> expif ELSE LCORCHET declaracion RCORCHET','expelse',5,'p_expelse','sintactico.py',88),
  ('expelse -> expif ELSE LCORCHET declaracion','expelse',4,'p_expelse','sintactico.py',89),
  ('expelse -> expif ELSE LCORCHET','expelse',3,'p_expelse','sintactico.py',90),
  ('expelse -> declaracion','expelse',1,'p_expelse','sintactico.py',91),
  ('expelse -> declaracion RCORCHET','expelse',2,'p_expelse','sintactico.py',92),
  ('expelse -> RCORCHET','expelse',1,'p_expelse','sintactico.py',93),
  ('funcion_condicion -> IF','funcion_condicion',1,'p_funcion_condicion','sintactico.py',96),
  ('funcion_condicion -> ELSEIF','funcion_condicion',1,'p_funcion_condicion','sintactico.py',97),
  ('control_bucle -> declaracion','control_bucle',1,'p_control_bucle','sintactico.py',100),
  ('control_bucle -> BREAK','control_bucle',1,'p_control_bucle','sintactico.py',101),
  ('control_bucle -> CONTINUE','control_bucle',1,'p_control_bucle','sintactico.py',102),
  ('while -> WHILE LPAREN comparacion RPAREN LCORCHET control_bucle RCORCHET','while',7,'p_while','sintactico.py',106),
  ('while -> WHILE LPAREN comparacion RPAREN LCORCHET','while',5,'p_while','sintactico.py',107),
  ('while -> control_bucle RCORCHET','while',2,'p_while','sintactico.py',108),
  ('while -> control_bucle','while',1,'p_while','sintactico.py',109),
  ('while -> RCORCHET','while',1,'p_while','sintactico.py',110),
  ('foreach -> FOREACH LPAREN ID AS ID RPAREN LCORCHET declaracion RCORCHET','foreach',9,'p_foreach','sintactico.py',113),
  ('foreach -> FOREACH LPAREN ID AS ID RPAREN LCORCHET','foreach',7,'p_foreach','sintactico.py',114),
  ('foreach -> control_bucle RCORCHET','foreach',2,'p_foreach','sintactico.py',115),
  ('foreach -> control_bucle','foreach',1,'p_foreach','sintactico.py',116),
  ('foreach -> RCORCHET','foreach',1,'p_foreach','sintactico.py',117),
  ('comparacion -> valor_comparado operadorcomparacion valor_comparado','comparacion',3,'p_comparacion','sintactico.py',121),
  ('comparacion -> boolean','comparacion',1,'p_comparacion','sintactico.py',122),
  ('valor_comparado -> NUMBER','valor_comparado',1,'p_valor_comparado','sintactico.py',125),
  ('valor_comparado -> boolean','valor_comparado',1,'p_valor_comparado','sintactico.py',126),
  ('valor_comparado -> operacion_matematica','valor_comparado',1,'p_valor_comparado','sintactico.py',127),
  ('valor_comparado -> ID','valor_comparado',1,'p_valor_comparado','sintactico.py',128),
  ('operadorcomparacion -> IS_EQUAL','operadorcomparacion',1,'p_operadorcomparacion','sintactico.py',132),
  ('operadorcomparacion -> IS_IDENTICAL','operadorcomparacion',1,'p_operadorcomparacion','sintactico.py',133),
  ('operadorcomparacion -> IS_NOT_EQUAL','operadorcomparacion',1,'p_operadorcomparacion','sintactico.py',134),
  ('operadorcomparacion -> IS_NOT_IDENTICAL','operadorcomparacion',1,'p_operadorcomparacion','sintactico.py',135),
  ('operadorcomparacion -> IS_GREATER_OR_EQUAL','operadorcomparacion',1,'p_operadorcomparacion','sintactico.py',136),
  ('operadorcomparacion -> IS_SMALLER_OR_EQUAL','operadorcomparacion',1,'p_operadorcomparacion','sintactico.py',137),
  ('operadorcomparacion -> SPACESHIP','operadorcomparacion',1,'p_operadorcomparacion','sintactico.py',138),
  ('operadorcomparacion -> MAYORQUE','operadorcomparacion',1,'p_operadorcomparacion','sintactico.py',139),
  ('operadorcomparacion -> MENORQUE','operadorcomparacion',1,'p_operadorcomparacion','sintactico.py',140),
  ('expresionlogica -> ID operadorlogico ID','expresionlogica',3,'p_expresionlogica','sintactico.py',149),
  ('operadorlogico -> AND','operadorlogico',1,'p_operadorlogico','sintactico.py',152),
  ('operadorlogico -> OR','operadorlogico',1,'p_operadorlogico','sintactico.py',153),
  ('operadorlogico -> XOR','operadorlogico',1,'p_operadorlogico','sintactico.py',154),
  ('operadorlogico -> NOT','operadorlogico',1,'p_operadorlogico','sintactico.py',155),
  ('declararvariable -> ID EQUALS tipo END','declararvariable',4,'p_declararvariable','sintactico.py',159),
  ('tipo -> boolean','tipo',1,'p_tipo','sintactico.py',163),
  ('tipo -> NUMBER','tipo',1,'p_tipo','sintactico.py',164),
  ('tipo -> TEXT','tipo',1,'p_tipo','sintactico.py',165),
  ('tipo -> NULL','tipo',1,'p_tipo','sintactico.py',166),
  ('tipo -> archivos','tipo',1,'p_tipo','sintactico.py',167),
  ('tipo -> array','tipo',1,'p_tipo','sintactico.py',168),
  ('tipo -> new','tipo',1,'p_tipo','sintactico.py',169),
  ('boolean -> TRUE','boolean',1,'p_boolean','sintactico.py',172),
  ('boolean -> FALSE','boolean',1,'p_boolean','sintactico.py',173),
  ('boolean -> expresionlogica','boolean',1,'p_boolean','sintactico.py',174),
  ('operador_object -> ID EQUALS OBJECT_OPERATOR FNOMBRE LPAREN argumentos RPAREN END','operador_object',8,'p_operador_object','sintactico.py',177),
  ('array -> ARRAY LPAREN valores_array RPAREN','array',4,'p_array','sintactico.py',180),
  ('valores_array -> elementos_array COMA valores_array','valores_array',3,'p_valores_array','sintactico.py',183),
  ('valores_array -> elementos_array','valores_array',1,'p_valores_array','sintactico.py',184),
  ('valores_array -> empty','valores_array',1,'p_valores_array','sintactico.py',185),
  ('flecha_array -> elementos_array FLECHA elementos_array','flecha_array',3,'p_flecha_array','sintactico.py',189),
  ('elementos_array -> NUMBER','elementos_array',1,'p_elementos_array','sintactico.py',192),
  ('elementos_array -> TEXT','elementos_array',1,'p_elementos_array','sintactico.py',193),
  ('elementos_array -> empty','elementos_array',1,'p_elementos_array','sintactico.py',194),
  ('elementos_array -> boolean','elementos_array',1,'p_elementos_array','sintactico.py',195),
  ('elementos_array -> array','elementos_array',1,'p_elementos_array','sintactico.py',196),
  ('elementos_array -> flecha_array','elementos_array',1,'p_elementos_array','sintactico.py',197),
  ('new -> NEW FNOMBRE','new',2,'p_new','sintactico.py',201),
  ('print -> funcion_print LPAREN argument RPAREN END','print',5,'p_print','sintactico.py',216),
  ('print -> funcion_print argument END','print',3,'p_print','sintactico.py',217),
  ('print -> ECHO LPAREN valores_echo RPAREN END','print',5,'p_print','sintactico.py',218),
  ('print -> ECHO valores_echo END','print',3,'p_print','sintactico.py',219),
  ('argument -> ID','argument',1,'p_argument','sintactico.py',222),
  ('argument -> TEXT','argument',1,'p_argument','sintactico.py',223),
  ('argument -> operacion_matematica','argument',1,'p_argument','sintactico.py',224),
  ('argument -> comparacion','argument',1,'p_argument','sintactico.py',225),
  ('valores_echo -> argument COMA valores_echo','valores_echo',3,'p_valores_echo','sintactico.py',228),
  ('valores_echo -> argument','valores_echo',1,'p_valores_echo','sintactico.py',229),
  ('funcion_print -> VAR_EXPORT','funcion_print',1,'p_funcion_print','sintactico.py',233),
  ('funcion_print -> ECHO','funcion_print',1,'p_funcion_print','sintactico.py',234),
  ('funcion_print -> PRINT','funcion_print',1,'p_funcion_print','sintactico.py',235),
  ('funcion_print -> PRINT_R','funcion_print',1,'p_funcion_print','sintactico.py',236),
  ('funcion_print -> VAR_DUMP','funcion_print',1,'p_funcion_print','sintactico.py',237),
  ('arreglos -> funcion_arreglo LPAREN ID RPAREN','arreglos',4,'p_arreglos','sintactico.py',240),
  ('argumento_doble -> LPAREN ID COMA ID RPAREN','argumento_doble',5,'p_argumento_doble','sintactico.py',243),
  ('funcion_argumento_doble -> ARRAY_MERGE','funcion_argumento_doble',1,'p_funcion_argumento_doble','sintactico.py',246),
  ('funcion_argumento_doble -> ARRAY_SEARCH','funcion_argumento_doble',1,'p_funcion_argumento_doble','sintactico.py',247),
  ('funcion_argumento_doble -> ARRAY_RAND','funcion_argumento_doble',1,'p_funcion_argumento_doble','sintactico.py',248),
  ('funcion_argumento_doble -> ARRAY_CHUNK','funcion_argumento_doble',1,'p_funcion_argumento_doble','sintactico.py',249),
  ('funcion_argumento_doble -> STR_SPLIT','funcion_argumento_doble',1,'p_funcion_argumento_doble','sintactico.py',250),
  ('funcion_argumento_doble -> PREG_SPLIT','funcion_argumento_doble',1,'p_funcion_argumento_doble','sintactico.py',251),
  ('funcion_argumento_doble -> COUNT','funcion_argumento_doble',1,'p_funcion_argumento_doble','sintactico.py',252),
  ('funcion_argumento_doble -> ARRAY_PUSH','funcion_argumento_doble',1,'p_funcion_argumento_doble','sintactico.py',253),
  ('funcion_argumento_doble -> SORT','funcion_argumento_doble',1,'p_funcion_argumento_doble','sintactico.py',254),
  ('funcion_argumento_doble -> ASORT','funcion_argumento_doble',1,'p_funcion_argumento_doble','sintactico.py',255),
  ('funcion_argumento_doble -> KSORT','funcion_argumento_doble',1,'p_funcion_argumento_doble','sintactico.py',256),
  ('funcion_argumento_doble -> UNSET','funcion_argumento_doble',1,'p_funcion_argumento_doble','sintactico.py',257),
  ('funcion_argumento_doble -> IMPLODE','funcion_argumento_doble',1,'p_funcion_argumento_doble','sintactico.py',258),
  ('funcion_argumento_doble -> EXPLODE','funcion_argumento_doble',1,'p_funcion_argumento_doble','sintactico.py',259),
  ('funcion_arreglo -> SUFFLE','funcion_arreglo',1,'p_funcion_arreglo','sintactico.py',262),
  ('funcion_arreglo -> ARRAY_UNIQUE','funcion_arreglo',1,'p_funcion_arreglo','sintactico.py',263),
  ('funcion_arreglo -> SIZEOF','funcion_arreglo',1,'p_funcion_arreglo','sintactico.py',264),
  ('archivos -> funcion_corta','archivos',1,'p_archivos','sintactico.py',267),
  ('archivos -> estructura_funcion','archivos',1,'p_archivos','sintactico.py',268),
  ('funcion_corta -> FGETS LPAREN ID COMA NUMBER RPAREN','funcion_corta',6,'p_funcion_corta','sintactico.py',271),
  ('estructura_funcion -> funcion_archivo LPAREN opcion RPAREN','estructura_funcion',4,'p_estructura_funcion','sintactico.py',274),
  ('opcion -> ID','opcion',1,'p_opcion','sintactico.py',277),
  ('opcion -> TEXT','opcion',1,'p_opcion','sintactico.py',278),
  ('funcion_archivo -> FREAD','funcion_archivo',1,'p_funcion_archivo','sintactico.py',281),
  ('funcion_archivo -> FSCANF','funcion_archivo',1,'p_funcion_archivo','sintactico.py',282),
  ('funcion_archivo -> FPASSTHRU','funcion_archivo',1,'p_funcion_archivo','sintactico.py',283),
  ('funcion_archivo -> FGETCSV','funcion_archivo',1,'p_funcion_archivo','sintactico.py',284),
  ('funcion_archivo -> FGETC','funcion_archivo',1,'p_funcion_archivo','sintactico.py',285),
  ('funcion_archivo -> FILE_GET_CONTENTS','funcion_archivo',1,'p_funcion_archivo','sintactico.py',286),
  ('funcion_archivo -> READFILE','funcion_archivo',1,'p_funcion_archivo','sintactico.py',287),
  ('funcion_archivo -> FILE','funcion_archivo',1,'p_funcion_archivo','sintactico.py',288),
  ('funcion_archivo -> PARSE_INI_FILE','funcion_archivo',1,'p_funcion_archivo','sintactico.py',289),
  ('clase -> CLASS FNOMBRE LCORCHET declaracion RCORCHET','clase',5,'p_clase','sintactico.py',293),
  ('clase -> CLASS FNOMBRE LCORCHET','clase',3,'p_clase','sintactico.py',294),
  ('clase -> declaracion RCORCHET','clase',2,'p_clase','sintactico.py',295),
  ('clase -> declaracion','clase',1,'p_clase','sintactico.py',296),
  ('clase -> RCORCHET','clase',1,'p_clase','sintactico.py',297),
]
