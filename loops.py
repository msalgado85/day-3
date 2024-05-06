nums = [1, 2, 3, 4, 5]

# for num in nums:
#     if num == 3:
#         print('Found!')
        # break
    #     continue
    # print(num)
# Should result in 1 2 Found! 4 5 (if continue) if break it stops once its found.

# for num in nums:
#     for letter in 'abc':
#         print(num, letter)
# Should print a b c for every number given:
# 1 a
# 1 b
# 1 c
# 2 a
# 2 b
# 2 c
# 3 a
# 3 b
# 3 c
# 4 a
# 4 b
# 4 c
# 5 a
# 5 b
# 5 c

# for i in range(1, 11):
#     print(i)
# This prints out
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
x = 0
# while x < 10:
# while True:
#     if x == 5:
#         break
#     print(x)
#     x += 1 
    # incraments x += # it goes up by given #

# use control + c to stop a loop if youre stuck in one
    
while True:
        print("Enter your name: ")
        name = input()
    if name == "Manny":
        print("Your name is" + name)
        break
    else:
        print("Thank you!")
