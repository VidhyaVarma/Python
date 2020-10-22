# Python
1.Python Dictionary:
  *Python dictionary is an unordered and mutable collection of items.
  *Each item  of dictionary has a key/value pair.
  *Key-Value pairs are seperated by comma(,).
  *A colon(:) separates value from its value.
  *ex: Products with their price as dictionary.
    productDict = {'Computer':40000,'Mobile':20000,'Calculator':1000,'Headphone':500}
	
2.Create Dictionary:
  *Using dict built-in-function, we can create the dictinary.
  *ex:
    productDict = dict(Computer=40000,Mobile=20000,Calculator=1000,Headphone=500)
  *We can create a dictionary form list of tuples.Each tuples should have two objects.The first object of tuple beacomes key and 
second object becomes value of dictionary.
  *ex: Count of students
    tupleList = [('BCA',100),('BCOM',150),('BSc',100)]
	studentDict = dict(tupleList)
  *We can create a dictionary from two different List.
    degree = ['BCA','BCOM','BSc']
	count = [100,150,100]
  *We have to form a iterable of tuples using zip(args) functiion.
    studentDict = dict(zip(degree, count))
	
3.Access values form dictionary:
  *Dictionary uses a keys to access values.
  *Keys can be used either inside the square backets or using the get method.
  *EX: 
    productDict = {'Computer':40000,'Mobile':20000,'Calculator':1000,'Headphone':500}
	productDict['Computer']
	productDict.get('Computer')
  *We can seperate the values from the dictionary using dict.values() method.
  *Also we can seperate the keys from the dictionary using dict.keys() method.
	
4.Add and update values in dictionary:
  *We can add new items or change the value of existing items using an assignment operator.
  *If the key is already present, then the existing value gets updated. In case the key is not present, a new (key: value)
  
pair is added to the dictionary.
  *EX:
    Update => productDict['Computer'] = 600000
	Add    => productDict['Television'] = 25000
	
5.Remove element from dictionary:
  *We can remove a particular item in a dictionary using the pop() method.
  *EX: productDict.pop('Computer').
  *There is another method called clear() is used to remove all items form dictinary.
  *EX: productDict.clear()
  
6.Check key is exist in dictinary:
  *We can check the if key is exist in dictinary by using the membership operator.
  *in => If return true, the key is exist.
  *not in => If returns true, the key is not in dictinary.
  *EX: 'Computer' in productDict ; 'Computer' not in productDict
	


  
