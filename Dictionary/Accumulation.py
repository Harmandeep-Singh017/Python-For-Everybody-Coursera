# The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of 
# credits taken this semester and assign it to the variable credits. Do not hardcode this – use dictionary accumulation!

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for course in Junior.keys():
    credits += Junior[course]
    
    
# Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.

str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for ch in str1:
    if ch not in freq:
        freq[ch] = 0
    freq[ch] += 1
print(freq)


# Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.

s1 = "hello"
counts = {}
for ch in s1:
    if ch not in counts:
        counts[ch] = 0
    counts[ch] += 1

    
# Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
key = str1.split()
for k in key:
    if k not in freq_words:
        freq_words[k] = 0
    freq_words[k] += 1
    
    
# Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d = {}
key = sent.split()
for word in key:
    if word not in wrd_d:
        wrd_d[word] = 0
    wrd_d[word] += 1
    
    
# Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary.
# Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"
characters = {}
for ch in sally:
    if ch not in characters:
        characters[ch] = 0
    characters[ch] += 1
best_char = list(characters.keys())[0]
for key in characters.keys():
    if characters[key] > characters[best_char]:
        best_char = key
        
        

# Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, 
# find the least frequent letter in the string and assign the letter to the variable worst_char.
sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for ch in sally:
    if ch not in characters:
        characters[ch] = 0
    characters[ch] += 1
worst_char = list(characters.keys())[0]
for key in characters.keys():
    if characters[key] < characters[worst_char]:
        worst_char = key
        
        
# Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. 
# Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
string = string1.lower()
letter_counts = {}
for let in string:
    if let not in letter_counts:
        letter_counts[let] = 0
    letter_counts[let] += 1
    
    
# Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. 
# Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = {}
for ch in p.lower():
    if ch not in low_d:
        low_d[ch] = 0
    low_d[ch] += 1
