with open('example.txt', 'r') as file:
    content = file.read()
    print(content)


with open('example.txt', 'w') as file:
    text=file.write("I am a developer")


with open('example.txt', 'a') as the_file:
    content = the_file.write("I am anania")

'''
The below is to read the file into a list

'''

with open('example.txt', 'r') as the_file:
    lines = the_file.readlines()
    print(lines)





