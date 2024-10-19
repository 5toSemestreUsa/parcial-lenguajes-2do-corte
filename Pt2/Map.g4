grammar Map;

prog:   stat+ EOF;

stat:   mapFunction 
    |   filterFunction 
    |   NEWLINE
    ;


mapFunction: 
      'map' '(' lambdaExpr ',' iterable ')' 
    | 'map' '(' function ',' iterable ')' ;

filterFunction: 
      'filter' '(' lambdaExpr ',' iterable ')' 
    | 'filter' '(' function ',' iterable ')' ;

lambdaExpr: 
    |   'lambda' ID   ':' function;

function:
    expr
    | expr op
    | expr op expr (op expr)*
    | functionCall
    | expr'['expr']' (op lambdaExpr)?;

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
    | '.'ID
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
set : '{' elements* '}';
key: STRING;

elements: expr (',' expr)* ','?;


expr: INT | FLOAT | STRING | dict | list | ID ;

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
WS  :   [ \t]+ -> skip ;