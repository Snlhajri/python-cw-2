my_name= input("What is your name?")
my_age= int(input("How old are you?"))
print(f"My name is {my_name}an I am {my_age} years old")



first_number=int(input("first_number"))
secound_number=int(input("secound_number"))
operation=input("the opreation")
if operation == ("+"):
    print(first_number+secound_number)
elif operation == ("-"):
    print(first_number-secound_number)
elif operation == ("*"):
    print(first_number*secound_number)
elif operation ==("/"):   
    print(first_number/secound_number)
else:
    print("the opreation is not vaild")


bus_capacity= 30
people_inbus= int(input("how many people inside the bus"))
people_outbus= int(input("how many people want to enter the bus"))
empty_seats = bus_capacity - people_inbus
if empty_seats > people_inbus :
    print("the empty seats is"+ empty_seats)
elif empty_seats <= people_outbus :
    print("the bus is full ")

