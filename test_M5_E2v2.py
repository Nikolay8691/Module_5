print(' welcome to Module 5 Exercise 2 version 2 homework! ')

l = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']

#l_unique = []
#for i in l:
#	if i not in l_unique:
#		l_unique.append(i)

#print('l_unique by for : ', l_unique)

l_unique = []
l_unique = list(set(l))
print('l_unique by set : ', l_unique)

#l_repeat = []
#for i in l_unique :
#	j = 0
#	for k in l : 
#		if k == i :
#			j += 1
#			if j > 1 :
#				l_repeat.append(i)

#print('repeated elements of the list : ', l_repeat)