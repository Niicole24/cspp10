num = input("Enter a number:")
word = input ("Enter a noun:")
number = num 
original= word



if number == "1":
    print("1 " + original)
else:
    if original[-2:] == "fe":
        print (number + " " + original[:-2] + "ves")
        
    elif original[-2:] == "ay" or original[-2:] == "oy" or original[-2:] == "ey" or original[-2:] == "uy":
        print (number + " " + original + "s")
        
    elif original[-1] == "y":
        print (number + " " + original[:-1] + "ies")
        
    elif original[-2:] == "sh" or original[-2:] == "ch":
        print (number + " " + original[:-2] + "es")
        
    elif original[-2:] == "us":
        print (number+ " " + original[:-2] + "i")
    else:
        print ("Error")