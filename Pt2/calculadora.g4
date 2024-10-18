grammar calculadora;

prog:   stat+ ;

stat:   expr                        # printExpr
    ;

expr:  'MAP(' FUNCTION ',' ITER ')' #SimpleMap                    
    |  'MAP(' LAMBDA ',' ITER ')' #SimpleMap                    
    ;
          
ID        :  ;
LAMBDA    : 'lambda' ;
ITER      : ;
FUNCTION  : ;
WS        : [ \t]+ -> skip ;
