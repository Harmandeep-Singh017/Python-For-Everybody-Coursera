# The print statements at the end of program ac10_5_5 above pick out the specific keys ‘t’ and ‘s’. Generalize that to print out the occurrence 
# counts for all of the characters. To pass the unit tests, your output must use the same format as the original program above.
f = open('scarlet.txt', 'r')
txt = f.read()
letter_counts = {}
for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0

    letter_counts[c] = letter_counts[c] + 1

for c in letter_counts.keys():
    print(c + ": " + str(letter_counts[c]) + " occurrences")
    
    
# Split the string sentence into a list of words, then create a dictionary named word_counts that contains each word and the number of times it occurs.
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
list1 = sentence.split()
word_counts = {}
for i in list1:
    value=0
    for j in list1:
        if i==j:
            value += 1
    word_counts[i] = value

    
# Create a dictionary called char_d. The keys of the dictionary should be each character in stri, and the value for each key should be how many 
# times the character occurs in the string.
stri = "what can I do"
char_d = {} 
for i in stri:
    char_d[i] = char_d.get(i,0) + 1

=========================================================================================================================================================================

# 1. The dictionary travel contains the number of countries within each continent that Jackie has traveled to. Find the total number of countries that Jackie 
# has been to, and save this number to the variable name total. Do not hard code this!
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
list1 = travel.values()
total = 0
for i in list1:
    total += i
    
# 2. schedule is a dictionary where a class name is a key and its value is how many credits it was worth. Go through and accumulate the total number of 
# credits that have been earned so far and assign that to the variable total_credits. Do not hardcode.
schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, 
            "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}
total_credits = 0
for key in schedule.keys():
    total_credits += schedule[key]
    
=====================================Accumulating the Best Key============================================

# Write a program that finds the key in a dictionary that has the maximum value. If two keys have the same maximum value, it’s OK to print out either one. 
# Fill in the skeleton code

# 1. Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. 
# Then, find the key with the lowest value in this dictionary and assign that key to min_value.
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}
for c in placement:
    if c not in d:
        d[c] = 0
    d[c] += 1
list1 = list(d.keys())
min_value = list1[0]
for i in list1:
    if d[min_value] > d[i]:
        min_value = i

# 5. Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. 
# Then, find the key with the highest value in this dictionary and assign that key to max_value.

product = "iphone and android phones"
lett_d ={}
for ch in product:
    if ch not in lett_d:
        lett_d[ch] = 0
    lett_d[ch] += 1
keys = list(lett_d.keys())
max_value = keys[0]
for maxi in keys:
    if lett_d[max_value] < lett_d[maxi]:
        max_value = maxi
