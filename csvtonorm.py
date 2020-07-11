import csv

with open('syllabus.csv') as syllabus:
	a=csv.reader(syllabus,delimiter=';')
	b=list(a)



	row1=[]
	for row in b:
		row1=row1+row
	print(row1)
	
	for c in row1:
		if ',' in c: 
			d=c.split(',')
			for e in d:
				print(e)
		else:
			print(c)

	