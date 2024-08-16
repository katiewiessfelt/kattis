'''
You also notice that when the calculator is turned on the previous operation’s result is set to 1
your calculator will never have to compute numbers larger than one quintillion (10^8) on your upcoming homework assignments.
'''
'''
The input will begin with an integer n (1<=n<=1000),
The operator will be one of +, -, *, or /.
The operands will be in the range 0<=a,b<=100,000
'''
import sys

count = None
output = None
output = 1

def calculate(line):
    global output
    a, op, b = line.split()
    # cast to int
    a = int(a)
    b = int(b)
    if op == '+':
        # adds the two numbers entered
        # then subtracts the result from the previous operation
        output = (a + b) - output
    elif op == '-':
        # subtracts the two numbers entered
        # then multiplies the result by the previous operation’s result
        output = (a-b)*output
    elif op == '*':
        # it squares its answer after multiplying the two numbers entered
        output = (a*b)**2
    elif op == '/':
        # it divides the first number by 2 if it is even,
        # otherwise it adds 1 to the first number and divides it by 2
        
        # have to cast output as int again to not get decimals
        if a%2 == 0:
            output = int(a/2)
        else:
            output = int((a + 1)/2)
    print(output)

# with open('input.txt', 'r') as fi:
#     lines = fi.readlines()
# for line in lines:
for line in sys.stdin:
    if count is not None:
        calculate(line)
    else:
        # first line is count of operations
        count = int(line)
        