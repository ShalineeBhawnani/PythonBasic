# ******************************************************************************************************************
# @purpose :Demonstrate Factors.
# @file  :Factors.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************

#creating method to check prime factors
def prime_factors(n):
   i=2

   #creating empty list
   factor_list=[]

   #taking given condition
   while i * i < n:
       while n % i == 0:
           factor_list.append(i)
           n = n / i
       i = i + 1
       return factor_list

#printing prim factors
print(prime_factors(80))

