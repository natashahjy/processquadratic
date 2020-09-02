# Assignment 1 Question 2
# Done By: Natasha Heng Jeng Yee
# UOW ID Number: 6959684

# Solve equation ax^2 + bx + c = y
# Get user input for a, b, c and max value of x and y
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))
  
while True:
    x = int(input("Enter value of max value of x:"))
    # Check if user input value is negative
    if (x < 0):
        print("Value must be positive")
        continue
    
    y = int(input("Enter value of max value of y:"))
    # Check if user input value is negative
    if (y < 0):
        print("Value must be positive")
        continue
    
    # Find solution
    for i in range(1, x):
        solution = (a*i*i + b*i + c)
    
        # If loop only runs one time and solution is greater than 
        # max of y print no solution
        if ((solution >= y) and (i == 1)):
            print("No solution found")
            break
        
        # Stops finding solution if exceed max value of y    
        elif (solution >= y):
            break
        
        # Print number statement
        print("{0}x{1}\u00b2+{2}x{1}+{3}={4}".format(a,i,b,c,solution))
        i = i + 1
        
    # Print output when program stops    
    print("Program ends")
    break 