import math
n = int(input('Enter the number of people: '))
print ('Probability: '+ str(100*((1 - (math.factorial(365)) / ((365**n)*(math.factorial(365-n)))))))