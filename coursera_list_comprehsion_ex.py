list1=[1,3,4,5,8,78,9,90]
list2=list()
y= (2+4)

newlist1=[ n for n in list1]
#newlist2=[ y+n for n in list1]
newlist3=[ n*2 for n in list1 if n%2==0]
x='abc'
newlist4=[(letter,num) for letter in x for num in range(1,4)]
print(newlist4)

for m,n in newlist4:
    print(m,n)

#print(newlist)



"""

for ele in list1:
    #list2.append(ele)

print(list2)
"""


""" 
for letter in x:
    for num in range(1,4):
        print(letter,num)
"""
    
