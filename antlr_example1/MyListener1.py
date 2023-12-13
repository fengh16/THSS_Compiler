from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener


class MyListener(ExprListener):
    def __init__(self):
        self.stack = []

    def exitExpr(self, ctx):
        """
        This method is called when exiting the 'expr' rule in the grammar.
        It performs the necessary operations based on the parsed expression.

        Parameters:
            ctx (antlr4.tree.ParseTree): The parse tree node for the 'expr' rule.

        Returns:
            None
        """
        if ctx.INT():
            self.stack.append(int(ctx.INT().getText()))
        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                pass
            else:
                left = self.stack.pop()
                right = self.stack.pop()
                op = ctx.getChild(1).getText()
                if op == '+':
                    self.stack.append(left + right)
                elif op == '-':
                    self.stack.append(left - right)
                elif op == '*':
                    self.stack.append(left * right)
                elif op == '/':
                    self.stack.append(left / right)

    def getResult(self):
        return self.stack[-1]

# 创建词法和语法分析器
input_stream = InputStream("(5+2)*3\n")
lexer = ExprLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ExprParser(stream)

# 创建自定义Listener
listener = MyListener()

# 添加Listener到解析器
parser.addParseListener(listener)

# 开始解析
tree = parser.prog()

# 获取计算结果
result = listener.getResult()
print("Result:", result)