import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

full_arr = names_1 + names_2
name_dict = {}
duplicates = []
for name in full_arr:
    if name not in name_dict:
        name_dict[name] = 0
    name_dict[name] += 1
    if name_dict[name] > 1:
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")