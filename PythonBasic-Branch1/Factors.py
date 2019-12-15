def prime_factors(n):
   i=2
   factor_list=[]
   while i * i < n:
       while n % i == 0:
           factor_list.append(i)
           n = n / i
       i = i + 1
       return factor_list
print(prime_factors(80))

