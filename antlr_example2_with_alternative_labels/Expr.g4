
grammar Expr;
prog:   expr NEWLINE ;
expr:   e=expr ('*'|'/') r=expr   # mulDivExpr
    |   e=expr ('+'|'-') r=expr   # addSubExpr
    |   INT                      # intExpr
    |   '(' expr ')'             # parenExpr
    ;
NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;