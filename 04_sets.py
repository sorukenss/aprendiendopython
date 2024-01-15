#sets 

my_set = set()  # declarar un set
my_other_set = {}

my_other_set = {"isaac", 'david', 32}
print(type(my_other_set))

print(len(my_other_set))

#un set no es una estructura ordenada al momento de guardar, los guarda donde sea que ella quiera 

print("isaac" in my_other_set)

my_other_set.remove('david')

my_other_set.clear()
