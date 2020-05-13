# Chapter 2 : page - 40 manipulating bits
# how to use XOR : return 1 in each bit where only one of two compared
# bits is a 1

a = 10
b = 5
print('a = ', a, '\tb = ', b)

a = a ^ b  # 1010 ^ 0101 = 1111 (decimal 15)

b = a ^ b  # 1111 ^ 0101 = 1010 (decimal 10)

a = a ^ b  # 1111 ^ 1010 = 0101 (decimal 5)


print('a =', a, '\tb =', b)