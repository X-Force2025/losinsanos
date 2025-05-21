def infix_to_postfix(tokens):
    """Convert infix expression to postfix notation"""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []

    for token in tokens:
        if token.isalnum():  # Operand (numbers or variables)
            output.append(token)
        elif token in precedence:  # Operator
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove the '('

    while stack:
        output.append(stack.pop())

    return output
