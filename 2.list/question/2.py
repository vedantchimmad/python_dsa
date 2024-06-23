'''
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''

heros=['spider man','thor','hulk','iron man','captain america']

# 1st ans
print(" Length of the list :",len(heros))

# 2nd ans
heros1=heros.copy()
heros1.append("black panther")
print("added list item at the end :",heros1)

# 3rd  ans

heros1.remove("black panther")
heros1.insert(3,"black panther")

print("added the black panther after hulk : ",heros1)

#4th ans

heros2=heros.copy()
'''heros2.remove("thor")
   heros2.remove("hulk")'''

for i in heros2[1:3]:
    heros2.remove(i)

heros2.insert(1,"doctr strange")
print("I have removed thor and hulk from the list and added doctr strange: ",heros2)

# 5th ans
heros2.sort()
print("I have listed all the heroes in alphabetical order : ",heros2)