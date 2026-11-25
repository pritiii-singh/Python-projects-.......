op=(input('Enter your operator='))
a=int(input('Enter your first number='))
b=int(input('Enter your second number='))
if op=='+':
    print('Sum', a+b)
elif op=="-":
    print('Sub',a-b)
elif op=='*':
    print("Mul",a*b)
elif op=="/":
    print("Divide",a/b)
else:
    print("choose an invailed number")