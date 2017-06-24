#D1 = { key:value, key:value,..}
D1={"Bangkok":30, "Roi-Et":40.1, "Ubon":35.2}
print(D1)

D2={"Monday":"Yellow", "Tuesday":"Pink", "Friday":20.2}
print(D2)

#D1.clear()
#print(D1)
print(D1.keys())
print(D1.values())

print(D1['Bangkok'])
D1['Bangkok'] = 100
print(D1)


D3={"9:00":34.4, "9:05":35.1, "9:10":40}
print(D3['9:05'])
