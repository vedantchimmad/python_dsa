'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

list1=[{"Janavary":2200},{"Februvary":2350},{"march":2630},{"April":2130},{"May":2190}]

# 1 Ans

print(f"The amount of many spend extra on feb as compare to Jan :", list1[1]["Februvary"]-list1[0]["Janavary"])

# 2nd ans
totalamount=0
for i in list1[0:3]:
   for j in i.values():
      amount = j
      totalamount = totalamount+amount

print("Total amount spend on first 3 month :",totalamount)

#3rd ans

count=0
for i in list1:
   for j in i.values():
      if j ==2000:
         count=count+1

if count>=1:
   print("Total number of amount spend 2000",count)

else:
   print("There is no any amount 2000 amount spend")

# 4th ans

list2=list1.copy()
list2.append({"Jun":1980})
print("adding jun expenditure in list2 : ",list2)

# 5 ans
list1[3]["April"]=2130-200
print("updated expenditure of april month :",list1)