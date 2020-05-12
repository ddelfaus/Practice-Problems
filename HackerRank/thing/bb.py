

def balancedBrackets(string):
    stack = []
    brackets = ['{', '}', '[', ']', '(', ')', "|"]
    count = 0
    for bracket in string:

        if bracket == '|' and count == 0:
            stack.append(bracket)
            print("current stack", stack)
            count += 1

        elif bracket == '{' or bracket == "[" or bracket == '(':
            stack.append(bracket)
            print("current stack", stack)

        else:
            if stack == []:
                print(stack)
                print("else stack failed")
                return False

            if bracket in brackets:
                print("bracket2", bracket)
                stack_pop = stack.pop()

                if bracket == ')' and stack_pop != '(':
                    print("failed par")
                    return False

                if bracket == '}' and stack_pop != '{':
                    print("failed bar")
                    return False
                if bracket == ']' and stack_pop != '[':
                    print("failed sqr")
                    return False
                if bracket == '|' and stack_pop == '|' and count != 1:
                    print("failed pip")
                    return False
                if bracket == '|':
                    print(count)
                    count -= 1

    print(stack)
    if stack == []:
        print("test")
        return True

    else:
        print("empty list fail")
        return False


print(balancedBrackets("{efwwaef|eafwawfe|}"))


# def balancedBrackets(string):
#     # Write your code here

#     # Write your code here
#     stack = []

#     brackets = {'{': '}', '[': ']', '(': ')'}
#     match = True
#     count = 0
#     for bracket in string:
#         print(bracket)
#         if bracket == '|':
#             count += 1
#         print(count)
#         if bracket in ['}', ']', ')']:

#             if stack == [] or brackets[stack.pop()] != bracket :
#                 match = False

#             else:
#                 print(stack, "stack")
#                 stack.append(bracket)

#         if stack:
#             match = False

#         else:
#             match = True
#     if count % 2 != 0:
#             match = False
#     return match

# print(balancedBrackets("{{||[]|}|}"))
