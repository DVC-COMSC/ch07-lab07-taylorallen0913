
inputvalues = input('Enter all elements values: ')
numbers1 = inputvalues.split()
evenlist = [] 
for i in range(len(numbers1)):
	numbers1[i] = int(numbers1[i])

counter = 0

while counter < len(numbers1):
	evenlist.append(numbers1.pop(counter))
	print(evenlist)
	counter += 1

print('The list numbers \n', numbers1)
print('The list for even index elements\n', evenlist)