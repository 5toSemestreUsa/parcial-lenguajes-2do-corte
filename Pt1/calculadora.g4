grammar calculadora;

prog:   stat+ ;

stat:   expr                        # printExpr
    ;

expr:   '-' expr                    # Negative
    |   expr op=('*'|'/') expr      # MulDiv 
    |   expr op=('+'|'-') expr      # AddSub
    |   ABS expr ABS                # Abs
    |   INT '/' INT                 # Fract
    |   '(' expr ')'                # parens
    ;

MUL     : '*' ;
DIV     : '/' ;
ADD     : '+' ;
SUB     : '-' ;
ABS     : '|' ;
INT     : [0-9]+ ;                         
WS      : [ \t]+ -> skip ;
