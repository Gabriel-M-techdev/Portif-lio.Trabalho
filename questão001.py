# Nome Gabriel Macedo dos Santos Gonçalves   
# Matricula 202515168

n=int(input("Digite um numero inteiro positivo: ")) 
while n<=0:
    n=int(input("Numero invalido! Digite um numero inteiro positivo: "))

atual=n
passos=0

print(f"sequencia gerada a partir do numero {n}:")

while atual!=1:
    print(atual)
    if atual%2==0:
        atual=atual//2
    else:
        atual=3*atual+1
    passos+=1
print(atual)
print(f"Total de passos para chegar a 1: {passos}")