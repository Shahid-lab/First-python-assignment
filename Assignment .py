#!/usr/bin/env python
# coding: utf-8

# In[1]:


2+2


# In[6]:


a= [5,10]


# In[107]:





# In[108]:


#  Q2-Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.-


 #List Approach#
    
result=[]
for x in range(2000,3200):
        if x % 7 ==0 and x %5 != 0:
            result.append(x)
print(result)
            


# In[109]:


#String Approach#
  

result=''
for x in range(2000,3200):
      if x % 7 ==0 and x %5 != 0:
          result += str(x) + ' , '
print(result)           


# In[50]:


# Q3Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.


a= input('Please give your First name ')
b= input('Please giv your Last name ')
"Your name in Reverse Order is {} {}".format(b, a)

# Alternate 1
name = ["Saima", "Karim"]
name.reverse()
print(name)

# ALternate
name = ["Saima", "Karim"]
name[::-1]


# In[73]:


# Q3. Write a Python program to find the volume of a sphere with diameter 12 cm.
      # diameter = 12
print(float(4/3)*3.14*float(6^3))


# In[81]:


# Q4. Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.

values = input("Input some comma seprated numbers : ")
list = values.split(",")
print('List : ',list)


# In[94]:


# Q6. Write a Python program to reverse a word after accepting the input from the user.

Word = input("Type any word : ")
Rev = Word[::-1]
print('Reverse : ',Rev)


# In[ ]:


#######  6 may class


# In[ ]:





# # Tuple
# 
# 1. slicing and indexing are same in list and tuble
# 2. Mutation(item assignment) is not possible in Tuple
# 3.Tuple iteration is diffrent please check
# 4. In Tuple on concatenate is possiple (ex- t1 + t2)
# 5. For insertion or other operation or manipulation- type conversion is the best way
# 6.string is also immutable
# 

# In[114]:


t = (1, 71, 8, 9)
type(t)


# In[115]:


# Tuple 
for i in t:
    print(t)


# In[116]:


for i in t:
    print(i)


# In[117]:


for i in range(len(t)):
    print(t[i])


# In[119]:


t
t2 = (3,7)


# In[121]:


t + 1


# # Set
# 1. it removes the duplicate and shows only unique values in output
# 2. application in nlp..sentiment analysis
# 3.case sensitive
# 4.accepts hetrogenous data
# 5.no indexing
# 6. on iteration the unique data and in ascending order also called as ordered in case th elements are homogenous if the elements are hetrogenous the output behaves as per the operation defination that is unordered
# 7. it takes list and tuple as an argument
# 8. for data manipulation type conversion is done
# 9.empty curly bracket, type() will show "dict", however upon assigning elements in the curly bracket it will show "set" on type() and also behaves lik tuple example unique sorted value
# 10.pop function removes element at 0th index, but no index pop operation present like list
# 11. some example behave in order ---query?
# 12. data manipulation with type conversion
# 
# 
# 

# In[193]:


# List as an argument in set
s_list  = set([1,1,2,3,4,57,7,7,8,8,8,9,9,9,0,0,0,9])

# Tuple as an argument in set
s_tuple  = set((1,1,2,3,4,57,7,7,8,8,8,9,9,9,0,53,53,53,-1,289,0,9))


# In[195]:


type(s_tuple)


# In[127]:


# iterates the unique data and in ascending order
for i in s:
    print(i)
    


# In[137]:


# empty curly bracket, type() will show "dict", however upon assigning elements in the 
# curly bracket it will show "set" on type() and also behaves lik tuple ex unique sorted value
b = {}


# In[143]:


type(b)


# In[144]:


b


# In[168]:


b1 = {-1, 0, 1, 2, 3, 4, 7, 8, 9, 53, 57, 289, 289, 289, 53, 53}
type(b1)
b1


# In[165]:


b1


# In[140]:


type(b1)


# In[ ]:


Dictionary


# In[146]:


s = {"shahid", "karim", "saima", "aaple", "mango", "jihain"}


# In[147]:


type(s)


# In[148]:


s


# In[181]:


s_mixed = {78, 57, 89,"shahid", "karim", "saima", "aaple", "#","mango", "jihain", 45, 98,29,72, "##"}


# In[182]:


s_mixed


# In[189]:


new_set= {44,4,45,48,49,49,0,"#", "hi",49,48}


# In[190]:


type(new_set)


# In[191]:


new_set


# In[ ]:





# In[158]:


type(s_mixed)


# In[179]:


s_4 = {4,5,67,3,4,7,5,4,565,5656,"abc","##","sudh"}


# In[180]:


s_4


# # Dictionary
# 
# 1.empty {}, type() will give dict--recheck
# 2.duplicate key will show latest key entries value
# 3.Integers can be accepted as keys
# 4.special character can be accepted as keys unless quoted amd made string
# 5.As value- List, Nested List, set, tuple, another dictionary are allowed(10:42)
# 6. Valye cannnot be reteived with index but with index key, once the key is addressed then only iindexing is possible
# 7.iteration (printing the local variable in iteration gives the key of the dictionary
# 8.8.iteration (printing the local variable as Index in iteration gives the value of the dictionary
# 9.new value assignemt to a existing key ca be done by indexing
# 

# In[ ]:


#1


# In[198]:


#2 duplicate key will show latest key entries value
k= {'name' : "shahid", 'lastname':"name", '1': "saiama"}


# In[200]:


k


# In[201]:


#3.Integers can be accepted as keys
k_int= {1 : "shahid", 2:"karim"}


# In[209]:


#4.special character can be accepted as keys unless quoted amd made string
k_splchar= {1 : "shahid", 2:"karim", "#$*" : "quoted value"}


# In[211]:


# 4.iteration (printing the local variable in iteration gives the key)
for i in k_splchar:
    print(i)


# In[214]:


# 8.iteration (printing the local variable as Index in iteration gives the value)
for i in k_splchar:
    print(k_splchar[i])

