nome = input("Nome do aluno")
idade = int(input("Idade do aluno: "))
nota1= float(input("Nota 1: "))
nota2= float(input("Nota 2: "))
nota3= float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

print()
print("======CADASTRO======")
print(f"Nome: {nome}, {idade} anos")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média: {media:.1f}")
print(f"Daqui a 10 anos: {idade + 10} anos")


if media >= 9:
    print("Média Excelente")
elif media >= 7:
    print("Média Boa")
else:
 print("Média insuficiente")



def eh_par(numero):
   return numero % 2==0

print(eh_par(4)) #True
print(eh_par(7)) #False

def celsius():
   f = (c *9/5) + 32