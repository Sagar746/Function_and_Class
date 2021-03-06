'''

Write a function to write a comma-separated value (CSV) file. It
should accept a filename and a list of tuples as parameters. The
tuples should have a name, address, and age. The file should create
a header row followed by a row for each tuple. If the following list of
tuples was passed in:
[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',
21)] it should write the following in the file:
name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21

'''


import csv
csvfile=open('file.csv','w', newline='')
name=[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',
21)]
obj=csv.writer(csvfile)

for row in name:
	obj.writerow(row)
	print(row)
	
csvfile.close()