from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener


class MyListener(ExprListener):
    def __init__(self):
        self.stack = []
        self.output = []

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
            self.output.append(ctx.INT().getText())
        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                pass
            else:
                # 这里的顺序是反的
                right = self.output.pop()
                left = self.output.pop()
                op = ctx.getChild(1).getText()
                self.output.append(left + " " + right + " " + op)

    def getReversePolishNotation(self):
        return self.output[-1]

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

# 获取逆波兰表达式
rpn = listener.getReversePolishNotation()
print("Reverse Polish Notation:", rpn)
