
#keypad phone problem.


#here we assigned alphabets present in each number similar to keypad keyboard.

'''keyboard = {"1":"@","2":"a b c","3":"d e f","4":"g h i",
"5":"j k l","6":"m n o","7":"p q r s ","8":"t u v","9":"w x y z","0":"0"}

want_to_continue=True   
while want_to_continue:     #because if it is true the following code will be executed.

    print("available numbers are:\n",keyboard.keys())
    desired_value = input("enter the number: \n")
    print("your alphabets for the given number are: \n",keyboard.get(desired_value))
    
    want_to_stop = int(input("enter 0 to stop or press any number to continue \n"))
    
    if want_to_stop==0:         #if it is 0 then the program will stop.
        print("Thank You")
        want_to_continue=False
        
    
    
    
    
    
    
    


