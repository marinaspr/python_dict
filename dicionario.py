import os
os.system('cls')

contato ={
    'nome': 'Edson',
    'idade': 50,
    'casado': True,
    'peso': 70.5
}
def exibicao_manual(d: dict) -> None:
    print(f"nome: {contato['nome']}")
    print(f"idade: {contato['idade']}")
    print(f"casado: {contato['casado']}")
    print(f"peso: {contato['peso']}")

def exibicao_metodos(d:dict) -> None:
    for k, v in d.items():
        print(f"{k} ->{v}")

contato['altura'] = 1.70
print(contato)

#del contato['altura']
#contato.pop('nome')
os.system('cls')
#bruto
print(contato.values())
#lista
print(list(contato.values()))
#valores
for chave in contato.values():
    print(chave)
#itens
print(contato.items())

os.system('cls')
exibicao_manual(contato)
del contato['nome']
os.system('cls')
exibicao_metodos(contato)

#for i in range(len(list))