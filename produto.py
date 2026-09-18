class Produto:
    def __init__(self, codigo: int, nome: str, preco: float, quantidade: int):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_preco(self, novo_preco: float) -> None:
        if novo_preco > 0:
            self.preco = novo_preco

    def atualizar_quantidade(self, nova_quantidade: int) -> None:
        if nova_quantidade >= 0:
            self.quantidade = nova_quantidade

    def __str__(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Nome: {self.nome} | "
            f"Preço: R$ {self.preco:.2f} | "
            f"Qtd: {self.quantidade}"
        )