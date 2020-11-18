
fhand=open(r"C:\Users\kiran\Desktop\coursera assign\mail.txt",'r')
#text=fh.read()
#print(text)

counts=dict()
lst=list()

newlst=list()
for line in fhand:
    #print(line)
    line=line.rstrip()
    lnlist=line.split(':')
    #print(lnlist)
    try:
       if lnlist[0].startswith("From"):
            #print(lnlist[0])
            if lnlist[0] == "From":
                continue
            else:
              time=(lnlist[0][-2:])
              lst.append(time)            
    except:
        continue

#print(lst)

for name in lst :
    counts[name] = counts.get(name,0) +1
#print(counts)

most=None
mostnam=None
finlist=list()
for kee ,val in counts.items():
    finlist.append((kee,val))
finlist= sorted(finlist)
for val ,kee in finlist:
    print(val, kee)

        


