#dict declaration
productDict = {'Computer':40000,'Mobile':20000,'Calculator':1000,'Headphone':500}

#create dict using dict method
productDict = dict(Computer=40000,Mobile=20000,Calculator=1000,Headphone=500)
print(productDict)

#create dict from tuples
tupleList = [('BCA',100),('BCOM',150),('BSc',100)]
studentDict = dict(tupleList)
print(studentDict)

#create dict form two lists
degree = ['BCA','BCOM','BSc']
count = [100,150,100]
studentDict = dict(zip(degree, count))
print(studentDict)

#acccess dictionary values
print(productDict['Computer'])
print(productDict.get('Mobile'))

#update dictionary value
productDict['Computer'] = 600000
print(productDict)

#add new value
productDict['Television'] = 25000
print(productDict)

#remove value from dictionary
productDict.pop('Computer')
print(productDict)

#check if key exist
print('Mobile' in productDict)
