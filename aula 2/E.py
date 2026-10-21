n1 = float(input("Me fala sua primeira nota"))
n2 = float(input("Me fala sua segunda nota"))


media = (n1 + n2)/2

if media >= 5 and media <= 10:
    print(f"Aprovado!!!!, sua nota foi {media}")
elif media >= 4 and media <5: 
    print(f"Você esta de recuperação! sua nota foi {media}")
elif media >= 0 and media < 4:
    print(f"Você foi reprovado! sua nota foi {media}")
else:
    print("As notas foram digitadas erradas")