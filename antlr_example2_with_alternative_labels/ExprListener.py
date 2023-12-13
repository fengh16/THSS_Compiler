# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#intExpr.
    def enterIntExpr(self, ctx:ExprParser.IntExprContext):
        pass

    # Exit a parse tree produced by ExprParser#intExpr.
    def exitIntExpr(self, ctx:ExprParser.IntExprContext):
        pass


    # Enter a parse tree produced by ExprParser#addSubExpr.
    def enterAddSubExpr(self, ctx:ExprParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by ExprParser#addSubExpr.
    def exitAddSubExpr(self, ctx:ExprParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by ExprParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:ExprParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by ExprParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:ExprParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by ExprParser#parenExpr.
    def enterParenExpr(self, ctx:ExprParser.ParenExprContext):
        pass

    # Exit a parse tree produced by ExprParser#parenExpr.
    def exitParenExpr(self, ctx:ExprParser.ParenExprContext):
        pass



del ExprParser