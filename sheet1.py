#question 3-
s1='Nice to have it'
s2='here'
s1+=s2
print(s1)

#question4-
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#question5-
a[0]=s1
a[5]=s2
print(a)

#question6-


num= [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]

for i in num:
    if i == 237:
        print(i)
        break
    elif i % 2 == 0:
        print(i)

#question7-
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))


#question9-
n=eval(input('enter the number:'))
n2= str(n)*2
n3= str(n)*3
n4= int(n+int(n2)+int(n3))
print(n4)

#question11
a=eval(input('enter the list:'))
a.split(',')
sorted(a)
print(a)

#question12-
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],
'Marks': [57,87,67,79]}
d1=d['Marks']
l=max(d['Marks'])
j=0
for i in range(len(d1)):
    if(d1[i]==l):
        j=i

d2=d['Student']
print(d2[j])

#question13-
s=input("Enter a string:")
l=0
d=0
for i in s:
    if i.isalpha():
        l=l+1
    if i.isdigit():
        d=d+1
print("LETTERS ",l)
print("DIGITS ",d)

#question14-
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

s=input('Enter a Subject: ')
l1=d['Name']
l2=[]
l3=[]
l4=d['Ratings']
l5=[]
sub=d['Subject']
for i in range(len(sub)):
    if sub[i]==s:
        l2+=[sub[i]]
        l3+=[l1[i]]
        l5+=[l4[i]]
d1={}
d1['Name']=l3
d1['Subject']=l2
d1['Ratings']=l5
print(d1)





















        
        
        

       
       
