with open('data/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

filename = 'data/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
    
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    
print("Birthday & PI")

filename = 'data/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

# print(pi_string[:80])

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
