#***** BOOLEANS ********
# print (True)
# print (False)

# is_rainy = True
# print (is_rainy)

# is_rainy = False
# print(is_rainy)

# comparing values
print (10 > 9) #Banke => True
print (10 == 9) #AY => False
print (65 < 66) #Fallon => True
print (True == True) #Banke => True
print (True == False) #AY => False
print (False == False) #Fallon => True
print (False == True) #Banke => False

a  = 3
b = 45

if b > a:
  print("b is greater than a") #AY => True
else:
  print ("b is not greater than a")

print (bool("Hello")) #Fallon => True
print(bool(15)) #Fallon => False

print (bool(False)) # => False
print (bool(0)) # => False
print (bool("")) # => False
print(bool(())) # => False
print(bool([])) # => False
print(bool({})) # => False
print(bool(None)) # => False

num = ""

if num == True:
  print (True)
else:
  print (False)