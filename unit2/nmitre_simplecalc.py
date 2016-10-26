num = input("Enter a problem:") 
op = num[1] 
num1 = int(num[0]) 
num2 = int(num[2]) 
print (op)

if op == "+":
    print ("The result is {}".format(num1 + num2))
elif op == "-":
    print ("The result is {}".format(num1 - num2))
elif op == "*":
    print ("The result is {}".format(num1 * num2))
elif op == "/":
    print ("The result is {}".format(num1 / num2))
elif op == "%":
    print ("The result is {}".format(num1 % num2))