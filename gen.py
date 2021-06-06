import asyncio

fields = {
	1: 
		[[0 for n in range(43)] for j in range(20)]+[[0 for i in range(20)]+[1,1,1]+[0 for i in range(20)]]+[[0 for i in range(20)]+[0,0,0]+[0 for i in range(20)]]+[[0 for i in range(20)]+[1,1,1]+[0 for i in range(20)]]+[[0 for n in range(43)] for j in range(20)],
	2: 
		[[0 for n in range(43)] for j in range(20)]+[[0 for i in range(20)]+[0,1,0]+[0 for i in range(20)]]+[[0 for i in range(20)]+[1,1,1]+[0 for i in range(20)]]+[[0 for i in range(20)]+[0,1,0]+[0 for i in range(20)]]+[[0 for n in range(43)] for j in range(20)],
	3: 
		[[0 for n in range(43)] for j in range(20)]+[[0 for i in range(20)]+[1,1,1]+[0 for i in range(20)]]+[[0 for i in range(20)]+[0,1,0]+[0 for i in range(20)]]+[[0 for i in range(20)]+[1,1,1]+[0 for i in range(20)]]+[[0 for n in range(43)] for j in range(20)],
	4:
		[[0 for n in range(43)] for j in range(20)]+[[0 for i in range(20)]+[1,0,1]+[0 for i in range(20)]]+[[0 for i in range(20)]+[1,0,1]+[0 for i in range(20)]]+[[0 for i in range(20)]+[1,0,1]+[0 for i in range(20)]]+[[0 for n in range(43)] for j in range(20)],	
	5:
		[[0 for n in range(43)] for j in range(20)]+[[0 for i in range(20)]+[1,1,1]+[0 for i in range(20)]]+[[0 for i in range(20)]+[1,0,1]+[0 for i in range(20)]]+[[0 for i in range(20)]+[1,1,1]+[0 for i in range(20)]]+[[0 for n in range(43)] for j in range(20)],
	6: 
		[[0 for n in range(43)] for j in range(20)]+[[0 for i in range(20)]+[1,0,1]+[0 for i in range(20)]]+[[0 for i in range(20)]+[0,0,0]+[0 for i in range(20)]]+[[0 for i in range(20)]+[1,0,1]+[0 for i in range(20)]]+[[0 for n in range(43)] for j in range(20)],
	7:
		[[0 for n in range(43)] for j in range(20)]+[[0 for i in range(20)]+[0,1,0]+[0 for i in range(20)]]+[[0 for i in range(20)]+[0,0,0]+[0 for i in range(20)]]+[[0 for i in range(20)]+[0,1,0]+[0 for i in range(20)]]+[[0 for n in range(43)] for j in range(20)],
}

async def count_neighbours(x: int, y: int, field: list) -> int :
	count = 0
	if x != 0 :
		if field[x-1][y] != 0 : count += 1
	if y != 0 :
		if field[x][y-1] != 0 : count += 1
	if x != 0 and y != 0 : 
		if field[x-1][y-1] != 0 : count += 1
	if x != len(field)-1 :
		if field[x+1][y] != 0 : count += 1
	if y != len(field[x])-1 :
		if field[x][y+1] != 0 : count += 1
	if x != len(field)-1 and y != len(field[x])-1 :
		if field[x+1][y+1] != 0 : count += 1
	if x != 0 and y != len(field[x])-1 :
		if field[x-1][y+1] != 0 : count += 1
	if x != len(field)-1 and y != 0 :
		if field[x+1][y-1] != 0 : count += 1
	return count

async def gen(field: list, count: bool) -> list :
	out = [[0 for i in field[0]] for j in field]
	for i in  range(len(field)) :
		for j in range(len(field[i])) :
			#if count_neighbours(i,j) == 2 :
			if count : # 1 change add if else
				if await count_neighbours(i, j, field) >= 2 :
					out[i][j] = 1
				if field[i][j] :
					if await count_neighbours(i, j, field) in (2,3) :
						out[i][j] = 1
					else :
						out[i][j] = 0
			else : # 1 change add if else
				if await count_neighbours(i, j, field) < 2 : # 2 change changed predicate (dont work for all start forms with (not in (1,2)))
					out[i][j] = 1
				if field[i][j] :
					if await count_neighbours(i, j, field) not in (2,3) : # 3 change added not and changed values
						out[i][j] = 1
					else :
						out[i][j] = 0
	return out

async def invert(field: list) -> list :
	out = [[0 for i in field[0]] for j in field]
	for i in range(len(field)) :
		for j in range(len(field[i])) :
			if field[i][j] :
				out[i][j] = 0
			else :
				out[i][j] = 1
	return out

async def generate(field: list, n: int) -> list:
	count = True
	a = await gen(field, count)
	for i in range(n) :
		a = await gen(a, count)
		count = not count
	return a

async def rule_gen(s: str) -> list :
	if s[28].isalpha() :
		gens = sum(list(map(lambda x : ord(x), s[29:])))
	else :
		gens = sum(list(map(lambda x : ord(x)-47, s[29:])))
	for i in s :
		if i == "9"  :
			start_fig = 1
		if i.isalpha() :
			start_fig = ord(i)-95
	print(start_fig)
	do_invert = s[0].isalpha()
	f = await generate(fields[start_fig], gens)
	if do_invert :
		f = await invert(f)
	return f
