import sys

print("This is the name of the script:", sys.argv[0])
print("Number of arguments:", len(sys.argv))
print("The arguments are:", str(sys.argv))

def copy_list(lista):
     return lista.copy()

my_list=[1,2]
print(copy_list(my_list))