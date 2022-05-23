# With only one line of code, assign the variables water, fire, electric, and grass to the values “Squirtle”, “Charmander”, “Pikachu”, and “Bulbasaur”

water, fire, electric, grass = "Squirtle","Charmander","Pikachu","Bulbasaur"


# If you remember, the .items() dictionary method produces a sequence of tuples. Keeping this in mind, we have provided you a dictionary called pokemon. 
# For every key value pair, append the key to the list p_names, and append the value to the list p_number. Do not use the .keys() or .values() methods.

pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = []
p_number = []
for key, value in pokemon.items():
    p_names.append(key)
    p_number.append(value)

# The .items() method produces a sequence of key-value pair tuples. With this in mind, write code to create a list of keys from the dictionary track_medal_counts 
# and assign the list to the variable name track_events. Do NOT use the .keys() method.

track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}
track_events = []
for key, value in track_medal_counts.items():
    track_events.append(key)
