'''a=10 #integer type number using the int datatype
print(type(a))

b=33.33 #float type point refer to float datatype
print(type(b))

a='string value is charters'
print(type(a))

a=[1234567] #list [] brackets using the is called list datatype.

b=(1,12,3,44,5)#tuple ()peranthasis is using is called tuple datatype.

c={1,2,333,444,2}#set {} curly datatype using.

print(type(a),type(b),type(c))


A=19
print(A)

v=7+5j  #complex datatype using values are number and characters 
print(type(v))

g=True #when true false is the bool datatypes using true and false in programming 
f=False
print(type(g),type(f))

#typecasting Or type conversion using one datatype to another datatype is called type conversionS
'''
'''int()
bool()
str()
float()'''
'''
f=22 #this the integer value when convert the float datatype in called type conversion 
print(float(f))

#examples
h=33.5
print(bool(h))

#data lose--> explicit type conversion
#no data lose-->implicit type conversion

'''
a = 4 + 5j
print(type(a))

b = 'nagamalleswari'
print(len(b),b[8])

age = ['hello',1,'hello2','hello333',5,'hel']  #list lo unaa values nee modifiy cheyavachu 
age[3]=10
print(age)

c =(3,5.2,'hii',6 ) #tuple lo unaa value nee modifiy cheyalemu
print(c)
print(type(c))

d = list(range(2,21,2)) #range anedhi motham at time istam  # list lo range kudaa rasukovachu
print(d)
print(type(d))

hi = {'name':'vayanandana','age':28}
print(hi['name'])

def name( a,b):
    return(a,b)

name('gopi','nandu')
