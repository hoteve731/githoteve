mylist = []

while True:
    listname = input ('Enter anything: ')
    if (listname == 'q'):
        print (mylist)
        break
    else:   
        mylist.append(listname)

