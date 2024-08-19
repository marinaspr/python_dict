import os
os.system("cls")


notas = {
    'Joao': 9.5,
    'Maria': 10.0,
    'Jose': 4.5
}


def add_aluno(d: dict) -> None :
    nome = str(input("Digite o nome do Aluno: "))
    nota = int(input("Digite a nota do Aluno: "))
    if nome not in d:
        if nota >= 0 and nota <= 10:
            d[nome] = nota
            print("aluno adicionado") 
        else:
            print("Nota inválida")
    else:
        print("Este nome já existe")
    
def editar_aluno(d: dict) -> None :
        
    nome = str(input("Digite o nome do Aluno para editar: "))
    if nome in d:
        nnovo = str(input("Digite novo nome: "))
        nnota = int(input("Digite a nota nova: "))
        if nnota >= 0 and nnota <= 10:
            d[nnovo] = d.pop(nome)
            print(d)
    else:
        print("Aluno não existe")

    










import os
os.system("cls")   
""""
x = int(input("1- cadastrar aluno2\n 2- editar aluno| nota\nEscolha: "))
if x == 1:
    add_aluno(notas)
elif x == 2:
    editar_aluno(notas)
else:
    print('opcão inválida')
"""
print("\n 0 - Sair")
print(" 1 - Adicionar novo Aluno | Nota limite (10)")
print(" 2 - Editar Aluno | Nota")
print(" 3 - Listar Alunos")
print(" 4 - Excluir Aluno")
print(" 5 - Caucular a média da turma")
print(" 6 - Consultar Aluno")
print(" 7 - Apagar todos os alunos da sala")

escolha = int(input("\nEscolha: "))
t = 0
while t == 0:
    match escolha:

        case 0:
           t = 1

        case 1:
            add_aluno(notas)

        case 2:
            editar_aluno(notas)

        #case 3:
            
        #case 4:
            
        #case 5:
            
        #case 6:
            
        #case 7: