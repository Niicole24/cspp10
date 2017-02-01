# worked with jessica
x_list = []
while True:
    user_input = input("What would you like to do? Sum, Clear, Print, Length, or Exit: ")

    
    if user_input == "Print":
        print(x_list)
     
    elif user_input == "Length":
        for index in range(len(x_list)):
        
            print("{} at index {}".format(x_list[index],index))

    elif user_input == "Exit":
        print("End")
        
    elif user_input == "Clear":
        x_list =[]
        print(x_list)
        

    elif user_input == "Sum":
        print(sum(x_list))
    
    else:
        x_list.insert(0, 0int(user_input))
        