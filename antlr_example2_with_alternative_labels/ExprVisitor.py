# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#intExpr.
    def visitIntExpr(self, ctx:ExprParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addSubExpr.
    def visitAddSubExpr(self, ctx:ExprParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:ExprParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parenExpr.
    def visitParenExpr(self, ctx:ExprParser.ParenExprContext):
        return self.visitChildren(ctx)



del ExprParser