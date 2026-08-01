try:
    with open('Untitled-1', 'rt') as fh:
     for line in fh :
         print(line.readline())
          
    
except FileNotFoundError:
        print("Error : The file 'sample.txt' was not found.")