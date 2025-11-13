outfile = open(r"chapter12\numbers.txt", "w")

for i in range(10):
    outfile.write(str(i)+" ")

outfile.close() 