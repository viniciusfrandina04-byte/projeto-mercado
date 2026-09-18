from produto import Produto
from estoque import Estoque

class MenuSistema:
    def __init__(self):
        self.estoque = Estoque()

    def exibir_menu(self):
        print("\n--- SISTEMA DE GERENCIAMENTO DE ESTOQUE ---")
        print("1. Cadastrar Produto")
        print("2. Consultar Produto")
        print("3. Alterar Produto")
        print("4. Remover Produto")
        print("5. Listar Todos os Produtos")
        print("6. Calcular Total em Estoque")
        print("0. Sair")

    def executar(self):
        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                codigo = int(input("Código do produto: "))
                nome = input("Nome do produto: ")
                preco = float(input("Preço: R$ "))
                quantidade = int(input("Quantidade: "))
                
                novo_produto = Produto(codigo, nome, preco, quantidade)
                if self.estoque.cadastrar_produto(novo_produto):
                    print("--> Produto cadastrado com sucesso!")
                else:
                    print("--> Erro: Código de produto já existente.")

            elif opcao == "2":
                codigo = int(input("Digite o código para consultar: "))
                prod = self.estoque.buscar_produto(codigo)
                if prod:
                    print(f"--> {prod}")
                else:
                    print("--> Produto não encontrado.")

            elif opcao == "3":
                codigo = int(input("Digite o código do produto a alterar: "))
                if self.estoque.buscar_produto(codigo):
                    novo_preco = float(input("Novo preço: R$ "))
                    nova_qtd = int(input("Nova quantidade: "))
                    self.estoque.alterar_produto(codigo, novo_preco, nova_qtd)
                    print("--> Produto alterado com sucesso!")
                else:
                    print("--> Produto não encontrado.")

            elif opcao == "4":
                codigo = int(input("Digite o código do produto a remover: "))
                if self.estoque.remover_produto(codigo):
                    print("--> Produto removido com sucesso!")
                else:
                    print("--> Produto não encontrado.")

            elif opcao == "5":
                print("\n--- LISTA DE PRODUTOS ---")
                if not self.estoque.produtos:
                    print("Nenhum produto cadastrado.")
                else:
                    for prod in self.estoque.produtos:
                        print(prod)

            elif opcao == "6":
                total = self.estoque.calcular_quantidade_total()
                print(f"--> Quantidade total de itens no estoque: {total}")

            elif opcao == "0":
                print("Encerrando o sistema... Até logo!")
                break

            else:
                print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    sistema = MenuSistema()
    sistema.executar()