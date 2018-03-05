def expr_eval(s):
    values_tok = check_token(s).split()
    if values_tok:
        output_stack = []
        operator_stack = []

        priority_rule = {
            '(': 0,
            '+':1, '-':1,
            '*':2, '/':2,
        }

        for token in values_tok:
            if token.isdigit():
                output_stack.append(int(token))
                continue
            elif token == '(':
                operator_stack.append(token)
                continue
            elif token == ')':
                while operator_stack:
                    operator = operator_stack.pop()
                    try:
                        if operator == '(':
                            break

                        b = output_stack.pop()
                        a = output_stack.pop()
                        if operator == '-': output_stack.append(a - b)
                        elif operator == '+': output_stack.append(a + b)
                        elif operator == '*': output_stack.append(a * b)
                        elif operator == '/': output_stack.append(a // b)
                        else:
                            raise Exception("Unknown operator: {}".format(operator))
                    except:
                        print "Divide by 0 Error."
                continue

            # Not a number - check operator priority_rule
            priority_token = priority_rule[token]
            while operator_stack and priority_token <= priority_rule[operator_stack[-1]]:
                try:
                    operator = operator_stack.pop()
                    b = output_stack.pop()
                    a = output_stack.pop()
                    if operator == '-': output_stack.append(a - b)
                    elif operator == '+': output_stack.append(a + b)
                    elif operator == '*': output_stack.append(a * b)
                    elif operator == '/': output_stack.append(a // b)
                    else:
                        raise Exception("Unknown operator: %s" % operator)
                except:
                    return "Invalid Input Expression string"
            operator_stack.append(token)


        while operator_stack:
            try:
                operator = operator_stack.pop()
                if operator == '(':
                    raise Exception('Mismatched opening parenthesis!')

                b = output_stack.pop()
                a = output_stack.pop()
                if operator == '-':   output_stack.append(a - b)
                elif operator == '+': output_stack.append(a + b)
                elif operator == '*': output_stack.append(a * b)
                elif operator == '/': output_stack.append(a // b)
                else:
                    raise Exception("Unknown operator: %s" % operator)
            except:
                return "Invalid Input Expression string"
        return output_stack.pop()
    else:
        return "Invalid Input Expression string"


def check_token(inp):
    output=""
    for z in inp:
        if z.isalpha():
            return ""

        if z == ' ':
            continue
        elif z == "(":
            output+=z+' '
        elif z in ['+','-','*','/']:
            output+=' '+z+' '
        elif z == ')':
            output+=' '+z
        elif z in str(range(0,9)):
            output+=z

    return output

tests = '((3*(4 + 3)+5) / 2)'
result = expr_eval(tests)
print result