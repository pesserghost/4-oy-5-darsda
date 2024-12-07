# num=123.38798
# print(round(num,3))
# numbers=[2,5,7,3,9,6,45]
# min=min(numbers)
# print(min)
# max=max(numbers)
# print(max)
# sum_numbers=sum(numbers)
# print(sum_numbers)


import math
# darajaga kotarish
num=math.pow(3,3)
print(num)

# kvadrat ildi olish
print(math.sqrt(16))

# yuqoriga yaxlitlash
print(math.ceil(12.3))

# pastga yaxlitlash
print(math.floor(12.8888888))

# moduldan chiqarish
print(math.fabs(5))

# factorial
print(math.factorial(5))

# radiandan gradusga otkaish
print(math.degrees(3))

# gradusdan radianga otkazish
print(math.radians(60))

# sin
print(math.sin(math.radians(90)))

#tan
print(math.cos(math.radians(60)))

# log
print(math.log(16,2))

#------------------------------
from decimal import Decimal
print(Decimal('0.2')+Decimal('0.2')+Decimal('0.1'))

