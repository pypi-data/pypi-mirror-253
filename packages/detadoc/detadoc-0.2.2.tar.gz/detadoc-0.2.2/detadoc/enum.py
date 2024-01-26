import datetime
from collections import namedtuple
from decimal import Decimal
from enum import Enum

from ormspace.enum import StrEnum


class Month(StrEnum):
    JAN = "Janeiro"
    FEB = "Fevereiro"
    MAR = 'Março'
    APR = "Abril"
    MAY = 'Maio'
    JUN = 'Junho'
    JUL = 'Julho'
    AUG = 'Agosto'
    SEP = 'Setembro'
    OCT = 'Outubro'
    NOV = 'Novembro'
    DEC = 'Dezembro'
    
class MedicationRoute(StrEnum):
    O = 'Oral'
    P ='Parenteral'
    T = 'Tópica'
    F = 'Oftalmológica'
    N = 'Nasal'
    A = 'Otoscópica'
    R = 'Retal'
    
class DosageForm(StrEnum):
    TAB = 'Comprimido'
    CAP = 'Cápsula'
    PAT = 'Adesivo'
    LIQ = 'Líquido'
    STR = 'Strip'
    POW = 'Pó'
    PAS = 'Pasta'
    DRO = 'Gota'
    AER = 'Aerosol'
    
    
class PaymentMethod(StrEnum):
    NO = 'Nenhum'
    CA = 'Dinheiro'
    PI = 'Pix'
    TR = 'Transferência'
    CC = 'Cartão de Crédito'
    DC = 'Cartão de Débito'
    AD = 'Débito em Conta'
    CH = 'Cheque'


class AccountType(StrEnum):
    C = 'Crétido'
    D = 'Débito'
    
    def __str__(self):
        return self.name
    

class AccountSubtype(namedtuple('AccountTypeMember', 'title type'), Enum):
    DI = 'Dividendo', AccountType.D
    AT = 'Ativo', AccountType.D
    EX = 'Despesa', AccountType.D
    SE = 'Equidade', AccountType.C
    LI = 'Dívida', AccountType.C
    RE = 'Receita', AccountType.C
    
    def __str__(self):
        return self.name


class Account(namedtuple('AccountMember', 'title subtype'), Enum):
    # ativos
    CAT = 'Dinheiro', AccountSubtype.AT
    BAT = 'Conta Bancária', AccountSubtype.AT
    RAT = 'Contas a Receber', AccountSubtype.AT
    SAT = 'Investimento de Curto Prazo', AccountSubtype.AT
    LAT = 'Investimento de Longo Prazo', AccountSubtype.AT
    PPE = 'Propriedade, Planta e Equipamento', AccountSubtype.AT
    INV = 'Inventario', AccountSubtype.AT
    PAT = 'Produtos', AccountSubtype.AT
    # receitas
    GRE = 'Receita Geral', AccountSubtype.RE
    SRE = 'Receita de Serviço', AccountSubtype.RE
    RRE = 'Receita de Aluguel', AccountSubtype.RE
    PRE = 'Receita de Produto', AccountSubtype.RE
    # despesas
    GEX = 'Despesa Geral', AccountSubtype.EX
    SEX = 'Despesa com Serviço', AccountSubtype.EX
    REX = 'Despesa com Aluguel', AccountSubtype.EX
    PEX = 'Despesa com Produto', AccountSubtype.EX
    IEX = 'Despesa com Imposto', AccountSubtype.EX
    SAE = 'Despesa com Salários', AccountSubtype.EX
    EEX = 'Despesa com Energia', AccountSubtype.EX
    WEX = 'Despesa com Água/Esgoto', AccountSubtype.EX
    TEX = 'Despesa com Telefone/Internet', AccountSubtype.EX
    # compromissos
    PLI = 'Contas a Pagar', AccountSubtype.LI
    STL = 'Empréstimo de Curto Prazo', AccountSubtype.LI
    LTL = 'Empréstimo de Longo Prazo', AccountSubtype.LI
    SLI = 'Salários a Pagar', AccountSubtype.LI
    CLI = 'Créditos Retidos', AccountSubtype.LI
    # equidade
    REA = 'Lucros Retidos', AccountSubtype.SE
    CAP = 'Capital Societário', AccountSubtype.SE
    # dividendos
    WDI = 'Saque de Lucro', AccountSubtype.DI

    
    def __str__(self):
        return self.name
    
    @property
    def type(self):
        return self.subtype.type

        
class CashFlow(StrEnum):
    RE = 'Receita'
    EX = 'Despesa'
    
    
class InvoiceType(StrEnum):
    G = 'Geral'
    S = 'Serviço'
    R = 'Aluguel'
    P = 'Produto'


class Period(StrEnum):
    H = 'Hora'
    D = 'Dia'
    W = 'Semana'
    M = 'Mês'
    Y = 'Ano'
    
    
    def timedelta(self):
        if self.name == 'H':
            return datetime.timedelta(hours=1)
        elif self.name == 'D':
            return datetime.timedelta(days=1)
        elif self.name == 'W':
            return datetime.timedelta(days=7)
        elif self.name == 'M':
            return datetime.timedelta(days=30)
        elif self.name == 'Y':
            return datetime.timedelta(days=365)
        
        
class Frequency(StrEnum):
    _ignore_ = 'Frequency i'
    Frequency = vars()
    for i in range(1, 13):
        Frequency[f'N{i}'] = f'{i}'
        
    def __int__(self):
        return int(self.value)
        
        
class Kinship(StrEnum):
    K1 = 'Primeiro Grau'
    K2 = 'Segundo Grau'
    K3 = 'Terceiro Grau'
    
    def __int__(self):
        return int(self.name[-1])
        
if __name__ == '__main__':
    for i in Kinship.__members__.values():
        print(i)
        print(int(i))