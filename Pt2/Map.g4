grammar Map;

prog:   stat+ EOF;

stat:   mapFunction 
    |   filterFunction 
    |   NEWLINE
    ;


mapFunction: 
      'map' '(' lambdaExpr ',' iterable ')' 
    | 'map' '(' ID ',' iterable ')' ;

filterFunction: 
      'filter' '(' lambdaExpr ',' iterable ')' 
    | 'filter' '(' ID ',' iterable ')' ;

lambdaExpr: 
    |   'lambda' ID   ':' function;

function: ID op expr 
    | functionCall
    | ID'['INT']' (op lambdaExpr)?;

functionCall: 
    | ID '(' expr (',' expr )+ ','? ')'
    | ID '(' ')';
op:
    '+' 
    | '-' 
    | '/' 
    | '%' 
    | '*' 
    | '**' 
    | '.'ID'()'
    | '==' 
    | '!=' 
    | '<' 
    | '>' 
    | '<='
    | '>=' ;

iterable: 
      list 
    | dict
    | set
    | ID'(' expr (',' expr )* ','? ')' 
    | ID'(' expr ')' 
    | ID ;

list: 
    '[' elements? ']' 
    | '(' elements? ')' ;


dict : '{' ( key ':' expr )* '}';
set : '{' expr* '}';
key: 
        '"'  *  '"' 
    |   '\'' * '\'';

elements: expr (',' expr)* ','?;


expr: INT | FLOAT | STRING | dict | list | ID;

INT: [0-9]+;
ID: [a-zA-Z]+;
FLOAT: [0-9]+'.'[0-9]+;
STRING: '"' (~["\r\n])* '"'  // comillas dobles
      | '\'' (~['\r\n])* '\''; // comillas simples
MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
NEWLINE:'\r'? '\n' ;
WS  :   [\t]+ -> skip ;