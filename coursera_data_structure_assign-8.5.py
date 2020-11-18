#fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"

#fh = open(fname)
#count = 0

fhand=open(r"C:\Users\kiran\Desktop\coursera assign\mail.txt",'r')
#text=fh.read()
#print(text)

count=0
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
          count=count+1
          lst.append(lnlist[1])
          #print(lst)
    except:
        continue

    #if "antranig@caret" in line:
     #break
print(lst)
print("There were",count," lines in the file with From as the first word")

     
"""

    if lnlist[0] == 'From':
       
      count=count+1
      mailid=(lnlist[1])
      lst.append(mailid)
      for word in lst:
          if word not in newlst:
             newlst.append(word)
for elem in newlst:
    print(elem)
    count=count+1
print("There were",count," lines in the file with From as the first word")
"""

