# My finished Collatz Conjecture program. 
# Information on what the Collatz Conjecture is can be found at https://www.youtube.com/watch?v=5mFpVDpKX70

import matplotlib.pyplot as plt

while True:
    print()
    print("Welcome to Bruce's Collatz Conjecture Program.")
    print()
    print("What is the Collatz Conjecture?")
    print(""" The Collatz Conjecture states that if you take any positive number and perform the following operations on it:
    * If the number is even, divide it by two.
    * If the number is odd, triple it and add one.
That process will eventually reach the number 1, regardless of which positive number was chosen initially""")
    print()
    print("** Close the chart made to run the program again **")
    print()

    plt.title('Here is your Collatz Conjecture chart')
    x = int(input("Enter a number to run the Collatz Conjecture Program on and see if it goes to one: ", ))
    print()
    seq = ([x])
    while x > 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        seq.append(x)
        plt.plot(seq)
    print("It took", len(seq),"steps to make it to one from your number.") 
    print()
    print("Here are the steps it took: ",seq)
    plt.show()
    print()
    

    
    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print('Goodbye')
        break
                
                
            
            
        
        
        
            
        
    
        
    
        
     

