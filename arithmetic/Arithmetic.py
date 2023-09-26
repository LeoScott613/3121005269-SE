import argparse #读取参数用

def read():
    parser = argparse.ArgumentParser(prog='Arithmetic',description="本程序用于生成指定数量的四则运算题目",epilog="帮助文本") # 函数的参数是输入-h时显示的内容，分为三个部分
    parser.add_argument('-n','--number')
    parser.add_argument('-r','--range') # 添加自定义的参数首选项
    args = parser.parse_args()
    pass

def calc():
    pass

def output():
    pass

read()