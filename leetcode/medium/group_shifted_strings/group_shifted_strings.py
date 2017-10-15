

def group(words):
	abc_size = 26
	res = {}
	for w in words:
		k = ord(w[0]) - ord('a')
		group = ''.join([chr(ord('a') + (ord(ch) - ord('a') + abc_size - k) % abc_size) for ch in w])
		#print k, group, w

		res.setdefault(group, []).append(w)

	#print res

	return res.values()

print group(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
