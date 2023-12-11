def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

Stack = []
postfix_expr = input().split()
for token in postfix_expr:
    if is_number(token):
        Stack.append(float(token))
    else:
        operand2 = Stack.pop()
        operand1 = Stack.pop()
        
        if token == "+":
            result = operand1 + operand2
        elif token == "-":
            result = operand1 - operand2
        elif token == "*":
            result = operand1 * operand2
        elif token == "/":
            result = operand1 / operand2
        elif token == "^":
            result = operand1 ** operand2
        elif token == "%":
            result = operand1 % operand2
        
        
        Stack.append(result)

if len(Stack) == 1:
    print('%.1f' % Stack[0])
else:
    print("Invalid postfix expression")
