def cal_treats(pet_s):
	treat_size = 1
	treat_tot = 1
	for i in range(1, len(pet_s)):
		if pet_s[i] == pet_s[i-1]:
			treat_tot = treat_tot + treat_size
		else:
			treat_size = treat_size + 1
			treat_tot = treat_tot + treat_size
	return treat_tot

num_cases = int(input())
for case in range(1, num_cases + 1):
	num_pets = int(input())
	size_pets = input().split()
	size_pets = list(map(int, size_pets))
	size_pets.sort()
	result = cal_treats(size_pets)
	#print(size_pets)
	print('Case #{}: {}'.format(case, result))