for segundos in range(10, 0, -1):  
    if segundos % 2 == 0: 
        print(f"Faltam apenas {segundos} segundos")
    else: 
        print(f"A contagem continua: {segundos} segundos restantes.")

print("Acabou o tempo!")