# first name last name 
first_name = "TJ"
last_name = "Sayre"

print( first_name, last_name,)

# two user inputs using input function 
distance = float(input("Enter the distance: "))
time = float(input("Enter the time: "))

# divide time by distance to get the velocity and print
velocity = distance / time
print("Velocity:", velocity)

# add first name and last name together
full_name = first_name + " " + last_name
print(full_name)

# replace Sayre with Gordon
new_full_name = full_name.replace("Sayre", "Gordon")
print(new_full_name)

# print the length of the full name
bool_true = True
bool_false = False

# print the boolean values
print("AND operator:", bool_true and bool_false)
print("OR operator:", bool_true or bool_false)
print("NOT operator:", not bool_true)

num1 = 10
num2 = 20
    
# print the comparison operators
print("num1 < num2:", num1 < num2)
print("num1 > num2:", num1 > num2)
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)