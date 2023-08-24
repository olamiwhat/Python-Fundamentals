# Working through examples

my_string = "This is MY string"

# Get all the characters before "M"

# chars_before_m = my_string[0:8]
# chars_before_m = my_string[:8]
# print(chars_before_m)

# Get all the characters starting from "M"
# chars_starting_from_m = my_string[8:]
# print(chars_starting_from_m)

# get all characters  in a string
# all_chars = my_string[:]
# print(all_chars)

# get all chars in reverse
# all_chars_reverse = my_string[::-2]
# print(all_chars_reverse)

# take a step back each time

# step_back_by_1 = my_string[13:2:-1]
# print(step_back_by_1)

# checkmate = "staging"
# print(checkmate[-2:-5:-1])



# slice the word until the first "a"
wrd = "Toscana" # Tosc
# chars_until_first_a = wrd[:4]
# print(chars_until_first_a)

# slice the word so that we "cana"
get_cana = wrd[3:]
# print(get_cana)

#slice the word with steps of 2, excluding the first and last characters
# new_wrd = wrd[1:6:2] # "ocn"
# print(new_wrd)

some_str = "Welcome to my blog"

print(some_str[3:18]) # come to my blog
print(some_str[2:14:2]) #loet y
print(some_str[:7]) # Welcome
print(some_str[8:-1:1]) # to my blo
print(some_str[-9:-15:-1]) # ot emo
print(some_str[0:9:3]) # Wce
print(some_str[-6:-9:-3]) # y
print(some_str[-9:-9:-1]) # No output
print(some_str[8:25:3]) # tmbg