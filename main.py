import random


a = random.randint(1, 6)
b = random.randint(1, 6)

r = random.randint(1, 6)
g = random.randint(1, 6)

tet = a + b
stb = r + g 

if tet < stb:
    print("Вася виграв")
elif tet > stb:
    print("Гєна ван лав")
else:
    print("Два дибіла, то є сила")
