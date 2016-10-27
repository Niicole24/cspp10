nam = input("Enter a number to start with: ")
end = input("Enter a number to end with: ")
end = int(end)
nam = int(nam)

for n in range(nam -1, end):
    n = n+ 1
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3  == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz") 
    else:
        print(n)