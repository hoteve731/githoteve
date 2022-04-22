fooddic = {}

while True:
    foodname = input ('Enter a fruit type (q to quit): ')
    if foodname == 'q':
        print (fooddic)
        break
    foodweight = input ('Enter the weight in kg:')
    fooddic [foodname] = foodweight
    if foodname == 'q':
        print (fooddic)
        break


