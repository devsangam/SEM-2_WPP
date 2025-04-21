s=input().lower()
letters=set()
for c in s:
	if (ord(c)>=97 and ord(c)<=122):
		letters.add(c)
if len(letters)==26:
	print("pangram")
else:
	print("not pangram")