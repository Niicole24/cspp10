#   working with jessica 
x_list = []
x = 1
while x != 0:
    user_input = int(input("Enter any number: "))
    
    if user_input >= 1:
        x_list.insert(0,user_input)
    
    if user_input < 0:
        if (user_input * -1) in x_list:
            x_list.remove(user_input * -1)
    
    if user_input == 0:
        print("End")
        
    print(x_list)
    
    



