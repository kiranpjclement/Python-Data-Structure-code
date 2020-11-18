
fhand=open(r"C:\Users\kiran\Desktop\coursera assign\mail.txt",'r')
#text=fh.read()
#print(text)

counts=dict()
lst=list()

newlst=list()
for line in fhand:
    #print(line)
    line=line.rstrip()
    lnlist=line.split()
    #print(lnlist)
    try:
       if lnlist[0] == "From":
          #print(lnlist[0])
        
          lst.append(lnlist[1])
          #print(lst)
    except:
        continue
for name in lst :
    counts[name] = counts.get(name,0) +1
#print(counts)

most=None
mostnam=None

for kee ,val in counts.items():
    if most is None or val > most :
        most =val
        mostnam= kee
    else:
        continue
print(mostnam,most)
        



