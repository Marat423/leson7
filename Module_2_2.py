first = int(input()) # Проссим ввести число
second = int(input()) # Проссим ввести число
third = int(input()) # Проссим ввести число

if first == second and first == third: # Если все числа равны то 3
    print(3)
elif first == second or first == third or second == third: # Если два числа равно то 2
    print(2)   
else: # Иначе 0
    print(0)
