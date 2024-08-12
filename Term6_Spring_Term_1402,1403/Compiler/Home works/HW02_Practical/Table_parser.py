from enum import Enum

class Token(Enum):
    Epsilon = ''
    Id = 'id'
    Equal = '='
    Semicolon = ';'
    LeftParen = '('
    RightParen = ')'
    LeftBrace = '{'
    RightBrace = '}'
    Plus = '+'
    Number = 'number'
    If = 'if'
    Else = 'else'
    While = 'while'

def tokenize(s: str):
    return [token.strip() for token in s.replace('\n', '').split()]

Rules = {
    'SL1' : 'StatementList -> Statement StatementList', 
    'SL2' : 'StatementList ->', 
    'S1'  : 'Statement -> Assignment',
    'S2'  : 'Statement -> Conditional',
    'S3'  : 'Statement -> Loop',
    'AS'  : 'Assignment -> id = Expr ;', 
    'CD'  : 'Conditional -> if ( Expr ) { StatementList } else { StatementList }', 
    'LP'  : 'Loop -> while ( Expr ) { StatementList }', 
    'EX'  : 'Expr -> Factor RestExpr', 
    'RE1' : 'RestExpr -> + Factor RestExpr', 
    'RE2' : 'RestExpr ->',
    'FT1' : 'Factor -> id', 
    'FT2' : 'Factor -> number', 
}

i = int()
tokens = list()
stack = list()

def input_to_token():
    tokens = list()
    n = int(input())
    for k in range(n):
        s = input()
        tokens.extend(tokenize(s))
    return tokens

def error():
    print("That was wrong!")

def sl1():
    global stack
    stack.extend(['sl', 'st'])

def s1():
    global stack
    stack.append('as')

def s2():
    global stack
    stack.append('cd')

def s3():
    global stack
    stack.append('lp')

def ass():    
    global stack
    stack.extend(reversed(['id', '=', 'ex', ';']))

def cd():
    global stack
    stack.extend(reversed(['if', '(', 'ex', ')', '{', 'sl', '}', 'else', '{', 'sl', '}']))

def lp():
    global stack
    stack.extend(reversed(['while', '(', 'ex', ')', '{', 'sl', '}']))

def ex():
    global stack
    stack.extend(reversed(['ft', 're']))

def re1():
    global stack
    stack.extend(reversed(['+', 'ft', 're']))

def ft1():
    global stack
    stack.append('id')

def ft2():
    global stack
    stack.append('number')

def main():
    global stack, i, tokens
    stack.append('sl')
    i = 0
    tokens = input_to_token()
    while len(stack) != 0:
        if i < len(tokens):
            if stack[-1] == tokens[i]:
                stack.pop()
                i += 1
                continue
        if stack[-1] == 'sl':
            if i == len(tokens):
                print(Rules['SL2'])
                stack.pop()
            elif tokens[i] == 'id' or tokens[i] == 'if' or tokens[i] == 'while':
                print(Rules['SL1'])
                stack.pop()
                sl1()
            elif tokens[i] == '}':
                print(Rules['SL2'])
                stack.pop()
            else:
                error()
        elif stack[-1] == 'st':
            if tokens[i] == 'id':
                print(Rules['S1'])
                stack.pop()
                s1()
            elif tokens[i] == 'if':
                print(Rules['S2'])
                stack.pop()
                s2()
            elif tokens[i] == 'while':
                print(Rules['S3'])
                stack.pop()
                s3()
            else:
                error()
        elif stack[-1] == 'as':
            if tokens[i] == 'id':
                print(Rules['AS'])
                stack.pop()
                ass()
            else:
                error()
        elif stack[-1] == 'cd':
            if tokens[i] == 'if':
                print(Rules['CD'])
                stack.pop()
                cd()
            else:
                error()
        elif stack[-1] == 'lp':
            if tokens[i] == 'while':
                print(Rules['LP'])
                stack.pop()
                lp()
            else:
                error()
        elif stack[-1] == 'ex':
            if tokens[i] == 'id' or tokens[i] == 'number':
                print(Rules['EX'])
                stack.pop()
                ex()
            else:
                error()
        elif stack[-1] == 're':
            if tokens[i] == ';' or tokens[i] == ')':
                print(Rules['RE2'])
                stack.pop()
            elif tokens[i] == '+':
                print(Rules['RE1'])
                stack.pop()
                re1()
            else:
                error()
        elif stack[-1] == 'ft':
            if tokens[i] == 'id':
                print(Rules['FT1'])
                stack.pop()
                ft1()
            elif tokens[i] == 'number':
                print(Rules['FT2'])
                stack.pop()
                ft2()
            else:
                error()

if __name__ == '__main__':
    main()