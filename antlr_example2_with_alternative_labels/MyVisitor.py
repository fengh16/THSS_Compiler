from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class EvalVisitor(ExprVisitor):
    def visitProg(self, ctx):
        return self.visit(ctx.expr())
    
    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.e)
        right = self.visit(ctx.r)
        op = ctx.getChild(1).getText()
        if op == '*':
            return left * right
        elif op == '/':
            return left / right

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.e)
        right = self.visit(ctx.r)
        op = ctx.getChild(1).getText()
        if op == '+':
            return left + right
        elif op == '-':
            return left - right

    def visitIntExpr(self, ctx):
        return int(ctx.INT().getText())

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

# 创建词法和语法分析器
input_stream = InputStream("(5+2)*3\n")
lexer = ExprLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ExprParser(stream)

# 创建自定义Visitor
visitor = EvalVisitor()

# 开始解析并获取计算结果
result = visitor.visit(parser.prog())
print("Result:", result)