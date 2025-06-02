import sys
from antlr4 import *
from CPP14Lexer import CPP14Lexer
from CPP14Parser import CPP14Parser

def parse_cpp_file(file_path):
    with open(file_path, 'r') as file:
        input_stream = FileStream(file.name)
        lexer = CPP14Lexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = CPP14Parser(token_stream)
        tree = parser.translationunit()

        # 检查语法错误
        if parser._syntaxErrors > 0:
            print(f"语法错误：{parser._syntaxErrors} 个错误")
        else:
            print("语法正确")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("用法：python parse_cpp.py <C++ 文件路径>")
        sys.exit(1)

    parse_cpp_file(sys.argv[1])
