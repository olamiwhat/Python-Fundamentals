# print (2 + 3 + 6)
# print (2 + 9)

# ORDER OF PRECEDENCE => ORDER TO BE COMPUTED FIRST
#Addition
# print(10 + 4) # 14

# float1 = 14.76
# float2 = 87.65

# print(float1 + float2)

#Subtraction
# print (1455 - 345)
# float1 = -13.345
# float2 = 6.78

# print(float1 - float2)

#Multplication
# print(23 * 34)

# float1 = 15.6
# float2 = 11

# print(float1 * float2)

#Division and Floor Division
# print(35/7) #5
# print(23.8/2)

# print(35//7) #5
# print(23.8//2) #Floor rounds up to the the nearest smaller integer

# Modulo
# Modulo returns the remainder of a division
# print(10 % 2)
# divide_by_10 = 28 % 10

# print(divide_by_10)
# print(type(divide_by_10))

# print(divide_by_10 * 10)



# def check_even_odd_num(num): # num is called a PARAMETER
#   if num%2 == 0: # Condition (TRUE OR FALSE)
#     print(num, " is an even number") # DO
#   else:
#     print(num, "is not an even number")


# check_even_odd_num(78) # Function Invocation , 78 is called an ARGUEMENT
# check_even_odd_num(35)
# check_even_odd_num(7381)

#EXECUTION CONTEXT
# fn() => check_even_odd_num # LINE 47
# num = 78 #creates a variable
# 78%2 = 0
# 0 == 0 => (TRUE)
# print(num, " is an even number")

# closes the execution context


# PRECEDENCE=> ORDER IN WHICH AN EXPRESSION THAT CONTAINS DIFFERENT OPERATORS WILL BE COMPUTED
#Parenthesis, exponent, modulo, multiplication, division, floor division, addition, subtraction

print(10 - 3 * 2) #multiplication is computed first, followed by subtraction

print(3 * 20 / 5) #multiplication occurs first, followed by division

print((10 - 3) * 2) #subtraction occurs first

print((18 + 2) / (10 % 8))

val1 = 2
val2 = 3

res = ((val1 ** val2) * (val2 % val1))

print(res)


