from atributos import *

class Dentista:
    def __init__(self, nome: str, login: str, senha: str):
        self.nome = Nome(nome)
        self.login = Login(login)
        self.senha = Senha(senha)

    def __str__(self):
        return f"Dentista: {self.nome}"


class Tecnico:
    def __init__(self, nome: str, login: str, senha: str):
        self.nome = Nome(nome)
        self.login = Login(login)
        self.senha = Senha(senha)

    def __str__(self):
        return f"Técnico: {self.nome}"
    
class Paciente:
    def __init__(self, nome:str, idPaciente:int):
        self.nome = nome
        self.idPaciente = idPaciente


class Trabalho:
    def __init__(self, paciente: Paciente, tecnico: Tecnico, dataInicio: str,
                 dataFinal: str, tipo: str, dentes: list[str], cor: str, translucidez: str):
        self.tecnico = tecnico
        self.paciente = paciente
        self.dataInicio = Data(dataInicio)
        self.dataFinal = Data(dataFinal)
        self.tipo = TipoTrabalho(tipo)
        self.dentes = Dentes(dentes, cor, translucidez)
        self.preco = self.tipo.valor * len(self.dentes.numeros)

    def __str__(self):
        return (f"Paciente = {self.paciente.nome}, Técnico = {self.tecnico.nome}, "
                f"Data Inicial = {self.dataInicio}, Data Final = {self.dataFinal}, "
                f"Tipo = {self.tipo.tipo}, Dentes = {self.dentes.numeros}, "
                f"Cor = {self.dentes.cor}, Translucidez = {self.dentes.translucidez}, Preço = R${self.preco:.2f}")

    
