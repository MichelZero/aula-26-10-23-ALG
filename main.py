####  abaixo revisão de DIC para a turma de POO

#
# autores: Cristiano e Michel
# data: 26/10/2023

#
# precipitação de chuvas 
# set out nov
# 10  20  30
#
print("precipitação de chuvas")
print('-'*22)
print("set\t| out\t| nov")
print("10\t| 20\t| 40")
print('-'*22)


# dicionário
chuvas = {'set':10,'out':20,'nov':30} # dict

print(f"{chuvas}-> original") # {'set': 10, 'out': 20, 'nov': 30} -> original


# imprimir lista de chaves
for maria in chuvas: 
  print(f"{maria} -> {chuvas[maria]}")
  
print(chuvas.keys()) # dict_keys(['set', 'out', 'nov'])
print(chuvas.values()) # dict_values([10, 20, 30])
print(chuvas.items()) # dict_items([('set', 10), ('out', 20), ('nov', 30)])



for i in chuvas.keys(): # dict_keys(['set', 'out', 'nov'])
  print(f"{chuvas[i]} -> {i}")

for i in chuvas.keys(): # dict_keys(['set', 'out', 'nov'])  
  print(f"{i} -> {chuvas[i]}")
  


# for i in chuvas.values(): # dict_values([10, 20, 30])
#   print(i, end=' ')  # 10 20 30 
# print()

# for i,j in chuvas.items(): # dict_items([('set', 10), ('out', 20), ('nov', 30)])
#   print(f"chave = {i}, e valor = {j}")
#   if not (j % 2 != 0):
#     print(i, "é par")
#   else:
#     print(i, "é impar")