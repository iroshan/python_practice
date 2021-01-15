def uniq(s):
	from collections import defaultdict
	dic =defaultdict(int)
	for c in s:
		dic[c] +=1
	return len(dic)

print(uniq('hellhjkdo'))

def uniqc(s):
	from collections import Counter
	dic = Counter(s)
	return len(dic)

print(uniqc('hello world'))

def uniqd(s):
	dic ={}
	for c in s:
		dic[c]= dic.get(c,0)+1
	return len(dic)
	
print(uniqd('bye bye'))