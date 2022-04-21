a = {}

a["이름"] = "류호산"
a["나이"] = "만 24살"
a["학번"] = "2019119025"
a["학과"] = "심리학과"
a["생일"] = "19970731"

print(a)
print(len(a))
print()

del a["이름"]
del a["나이"] 
del a["학번"] 
del a["학과"]
del a["생일"]

print (a)
print(len(a))
print()

a = dict(이름 = '류호산', 나이='만 24살', 학번 = '2019119025', 학과='심리학과', 생일='19970731')

print (a)
print(len(a))
print()

a.clear()
print(a)
print(len(a))