import enum


class TipoAtivo(enum.Enum):
    renda_fixa = "renda_fixa"
    acao = "acao"
    opcao = "opcao"
    fii = "fii"
