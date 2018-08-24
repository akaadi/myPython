# create a calculator that can compute the area of the shapes like circle or triangle etc.

print("the program to calculate areas is running")

# taking the input from the user
option = input("Please enter C for Circle or T for Triangle: ")

# checking for inputs and returning/printing the corresponding areas

# here first we check input for a circle
if option == 'C' or option == 'c':
    r = input("Enter the radius:")
    area_circle = 3.14 * float(r*r)
    print(area_circle)

# here we check input for a triangle
elif option == 'T' or option == 't':
    b = input("Enter the base:")
    h = input("Enter the height:")
    area_triangle = 0.5 * float(b*h)
    print(area_triangle)

# if user input something else then do this     
else:
    print("Empty")
    
