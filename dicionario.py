dict = {
    "Nome": input("Digite o nome: "),
    "Telefone": input("Digite o telefone: "),
    "E-mail": input("Digite o e-mail: ")
}
print("-"*30)
for chave,valor in dict.items():
    print(f"\033[1;34m{chave}\033[0m - {valor}")
print("-"*30)