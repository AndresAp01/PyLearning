# nested loop = A loop within another loop
#for x in range(3): #repeat this 3 times
  #  for y in range(1, 10):  #With the inner loop we count the lines 1 - 9
  #      print(y, end=' ')
#    print() #after we exit the for loop we will print a new line

rows = int(input('Enter the number of rows: '))
columns = int(input('Enter the number of columns: '))
symbol = input('Enter a symbol to use: ')

for x in range(rows):
    for y in range(columns):
        print(symbol, end='')
    print()