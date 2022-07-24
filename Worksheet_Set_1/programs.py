#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = int(input())
fact = 1
if num < 0:
    print("No Factorial")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of given number is")
    for i in range(1,num+1):
        fact = fact*i
    print(fact)    


# In[13]:


num = int(input())
if num< 0:
    print('Not prime')
elif num == 1:
    print("Not prime nor composite")
else:
    for i in range(2,num):
        if num%i == 0:
            print("Composite number")
            break
    else:
        print("Prime Number")


# In[ ]:


str = input()
str1 = str[::-1]
if str == str1:
    print("Palandrome")
else:
    print("Not Palandrome")


# In[7]:


import math

a = int(input("Enter base: "))
b = int(input("Enter height: "))


c = int(math.sqrt(a ** 2 + b ** 2))

print("Hypotenuse =", c)


# In[ ]:


test_str = input()
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print ("Frequency of characters is"
                                        +  str(all_freq))


# In[ ]:




