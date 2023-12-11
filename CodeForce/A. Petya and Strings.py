n1 = str(input())
n2 = str(input())

list1 = []
list2 = []
count = 0

for i in n1:
    list1.append(i)

for j in n2:
    list2.append(j)

for i in range(len(list1)):
    if (ord(list1[i].lower()) != ord(list2[i].lower())):

       
        if (ord(list1[i].lower()) > ord(list2[i].lower())):
            count += 1

        if (ord(list1[i].lower()) < ord(list2[i].lower())):
            count -= 1
#
#a = input()
#b = input()
#a = (a.lower())
#b = (b.lower())
#if a == b:
 #   print("0")
#elif a > b:
  #  print('1')
#elif a < b:
   # print('-1')


   
#sum1 = 0
#sum2 = 0
#for j in range(len(list1)):
 #   sum1 += ord(list1[j])
  #  sum2 += ord(list2[j])

#if (sum1 > sum2) :
 #   print(1)
#elif (sum2 > sum1):
 #   print(-1)
#else:
 #   print(0)


