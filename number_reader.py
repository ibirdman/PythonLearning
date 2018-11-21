import json

filename = 'data/numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    
print(numbers)
