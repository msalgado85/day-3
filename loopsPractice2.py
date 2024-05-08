# Grocery Shopping Calculator:
# Write a program that takes a list of item prices from a user and calculates the total cost, including a given tax percentage.
# listOfNumbers = range(1, 101)
# print(listOfNumbers)
# for number in listOfNumbers:
#     print(number)

#     if number % 2 == 0:
#         print( str(number) + " is even")
#     else:
#         print( str(number) + " is odd")

listOfNumbers = range(1, 10001)
even_sum = sum(num for num in listOfNumbers if num % 2 == 0)
print("summ of the even numbers from 1 to 10000:" + str(even_sum) )