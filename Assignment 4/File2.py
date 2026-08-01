with open('output.txt','wt') as fh:
     fh.write(input("Enter text to write to the file : ") + "\n")
     print("Data successfully written to 'output.txt'.\n")

with open('output.txt', 'at') as fh:
     fh.write(input("Enter additional text to append : "))
     print("Data successfully appended\n")

print("Final content of 'output.txt':")
with open('output.txt','rt') as fh:
     line1 = fh.readline()
     line2 = fh.readline()
     print(line1.rstrip())
     line1.rstrip()
     print(line2.rstrip())
     
     