#List:collection of data simply know as list.Lists are used to store multiple items in a single variable.
#List items are ordered, changeable, and allow duplicate values.

ayesha=[1,2,3,4,5,6,]
print(type(ayesha))
print(ayesha)

yasin_begum=['a','a','b','c','d']
print(yasin_begum)

sattar12=[12.40,34.770,45.90]
print(sattar12)

ibrahim123=[20,'male',True,60000.00,3+7j]
print(ibrahim123)

az=['hello',345,45.89,4+7j,'hii']
print(az)

num=['name',45,40,1+6j,400.90]
print(num)


kl=[15.60,50.70,60.30,70.59,80,90]
print(kl)

num1=[1,50,60,70,80,90]
print(num1)

hii=[1+4j,50+70j,60+90j,70+30j,80+7j,900+6j]
print(hii)

num10=[100,5000,6000,7000,8000,9000]
print(num10)

#Index:it is used to access single varible in a list.

a=[1,2,3,4,5,6,]
print(a[3])

b=[1.0,2.5,3.6,4.6,5.7]
print(b[-2])

c=['a','b','c','d']
print(c[0])

d=[1+3j,3+5j,5+7j,7+8j]
print(d[-1])

e=[20,40.50,'JAVA',609,30,11]
print(e[-4])

F=[20,40.50,'PTHON',True,609,5678.70]
print(F[0])

FK=[920,40.50,'KUKKI',True,609,389]
print(FK[3])

HII=[520,40.50,23,'DO U KNOW',False,609]
print(HII[4])

L=[20,40.50,'heyy',49.509,True,609]
print(L[5])

ayesha=[20,40.50,'akka',True,609,409]
print(ayesha[4])

#slice:Specify the start index and the end index, separated by a colon, to return a part of the string. ExampleGet your own Python Server.

a=[1,2,3,4,5,6,7]
print(a[0:3])

a=[1+4j,'ayesha',2,3,4,5,6,7]
print(a[-3:-5])

d=[11,12,13,14,54,6.46,56,7]
print(d[4:6])

ao=['a','b','d','j','dfdg','tgt','rtrete']
print(ao[0:3])

ah=[1,2,3,4,5,6,7,8,9,10]
print(ah[0:5])

good1=[13,34.67,42.657,122.35,454,]
print(good1[0:3])

a=[1+4j,2+5j,57+667j,34209+5645j,56+436j,45+65j]
print(a[5:7])

ak=[10,20,300,4,5,6,7]
print(ak[1:3])

anu=[134.60,2,3+5j,48,500.34,600,7]
print(anu[4:6])

#list methods:
      #1.append():it will add single element at end of the list.

a=[1,2,3,4,5,6,7]
a.append(10)
print(a)

     #2:extend():adding more elements
b=[1,2,3,4,5,6]
c=['a','b','c','d']
b.extend(c)
print(b)

    #pop():it will remove last element.
a=[1,2,3,4,5] 
a.pop()
print(a)

    #length():lenght of element.
ayesha=[10,20,30,40,50,60,70,80]
print(len(ayesha))

    #count():it count how many times repeat.
ah45=['a',1+4j,39.40,56,'hii',45,45,23,45]    
print(ah45.count(45))
print(ah45)