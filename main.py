from antlr4 import *
from HelloLexer import HelloLexer
from HelloParser import HelloParser


input_text = input("> ")
lexer = HelloLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = HelloParser(stream)

tree = parser.r()

print(tree.toStringTree(recog=parser))
