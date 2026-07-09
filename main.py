# a = []

# total_input = int(input("How many inputs do you want to enter? "))

# for i in range(total_input):
#     aInput = input("Enter anything: ")
#     a.append(aInput)

# print(a)

my_dogs = ["Bulldog", "Beagle", "Poodle", "Labrador"]
your_dogs = my_dogs[:]

for dog in your_dogs:
    print("your dogs: " + dog)

my_dogs.append("Golden")
for dog in my_dogs:
    print("my dogs: \n")
    
print(list(my_dogs))