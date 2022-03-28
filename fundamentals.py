# A light exercise to add to your arsinal of coding weapons to master the fundamentals of python and have continued exposure.


#1 | Iterating through lists with for loops

my_numbers = [1, 2, 3, 4, 5, 6, 7]

for numbers in my_numbers:
    print(numbers)


#2 | Adding to iterations

my_numbers = [1, 2, 3, 4, 5, 6, 7]

for numbers in my_numbers:
    numbers += 1
    print(numbers)

3 | Finding even numbers in a list

my_numbers = [1, 2, 3, 4, 5, 6, 7]

for numbers in my_numbers:
    if numbers % 2 == 0:
        print(numbers)

#4 | listing even and odd numbers

my_numbers = [1, 2, 3, 4, 5, 6, 7]

even_numbers = 0
odd_numbers = 0

for numbers in my_numbers:
    if numbers % 2 == 0:
        even_numbers += 1
    elif numbers % 2 == 1:
        odd_numbers += 1


print('We have {} even numbers'.format(even_numbers))
print('We have {} odd numbers'.format(odd_numbers))

#5 | Using strings in a list

state = ['California',
         
         'Mississippi',
         
         'Florida',
         
         'Arizona',
         
         'Alabama',
         
         ]


for location in state:
    
    print(location)
