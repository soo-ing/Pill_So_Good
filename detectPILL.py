import csv

def detect():
	r1=open('pill_list.csv','r',encoding='UTF-8')
	r2=open('pill.csv','r',encoding='UTF-8')

	num1=csv.reader(r1)
	num2=csv.reader(r2)

	num1_data=list(num1)
	num2_data=list(num2)

	for i in range(len(num1_data)):
		if num1_data[i][0]==num2_data[0][0]:
			if num1_data[i][1]==num2_data[0][1]:
				return num1_data[i][2]
