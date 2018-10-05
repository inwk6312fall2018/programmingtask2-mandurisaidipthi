import csv
name="Crime.csv"
def crimelist(s):
    with open("crime.csv") as csvfile:
        readCSV=csv.reader(csvfile,"r")
    mydicta=dict()
    mydictb=dict()
    list1=[]
    list2=[]
    for i in readCSV:
        i.strip()
	i.split()
	list1.append(i[-1])
	list2.append(i[-2])
    for p in list1:
        if p not in line:
	    mydicta[p]=1
	else:
	    mydicta[mydictb]+=1
	    print(prettytable(headers=['crimetype','CrimeId','CrimeCount']))
    def reverse_lookup(g,h):
         for k in mydicta:
              if g[k] == h:
                  print(prettytable(k))
crimelist(name)
