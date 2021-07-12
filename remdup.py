lits=[5,4,2,6,5,2,1,0]

ring=[]
for number in lits:
    if number not in ring:
        ring.append(number)
print(ring)
