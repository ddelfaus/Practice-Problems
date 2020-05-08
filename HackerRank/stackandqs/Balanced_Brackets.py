
def isBalanced(s):
    stack = []
    closer = {'{': '}', '[': ']', '(': ')'}
    match = "yes"

    for bracket in s:
        if bracket in {'}',']',')'}:
            if not stack or closer[stack.pop()] != bracket:
                match = "NO"
        else:
            stack.append(bracket)
    if stack:
        match = "NO"
    else:
         match = "YES"





#plan some how put 2nd half of the sequence in to a stack

#then compare it wth the first half
#if not the same return no
#else return yes


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = []

    def push(self, value):
        #adding to the top of the stack
        self.storage.append(value)
    def pop(self):
        #removing top of stack
        return self.storage.pop()

    def len(self):
        return self.size


def isBalanced(s):
    stacky = Stack()
    #spliting in half
    first_half = list(s[:len(s)//2])

    print(first_half, "efafeawffwea")
    second_half = s[len(s)//2:]
    match = "yes"
    for item in second_half:
        stacky.push(item)

    
    for item in first_half:
        print(stacky.storage)
        print(item,"compare")

        if item == "[":
            item = "]"

        if item == "(":
            item = ")"
        if item == "{"
            item = "}"

        if item != stacky.pop():
            
            match = "no"
            break

    print(match)
    print(stacky.storage)
isBalanced("[()]")




