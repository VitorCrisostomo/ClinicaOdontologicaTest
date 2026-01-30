from datetime import datetime
import re
import hashlib
from dataclasses import dataclass

class Data:
    def __init__(self, data):
        if isinstance(data, str):
            try:
                dia, mes, ano = map(int, data.split("/"))
            except ValueError:
                raise ValueError("Data inválida. Use o formato DD/MM/AAAA.")
        elif isinstance(data, (list, tuple)) and len(data) == 3:
            dia, mes, ano = data
        else:
            raise TypeError("Data deve ser string 'DD/MM/AAAA' ou (dia, mes, ano).")

        try:
            datetime(ano, mes, dia)
        except ValueError:
            raise ValueError("Data inválida.")

        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"

    @classmethod
    def hoje(cls):
        """Retorna a data atual"""
        agora = datetime.now()
        return cls(agora.day, agora.month, agora.year)

class Nome:
    def __init__(self, nome: str):
        nome = nome.strip()
        if not nome.replace(" ", "").isalpha():
            raise ValueError("Nome inválido. Deve conter apenas letras e espaços.")
        self.nome = nome

    def __str__(self):
        return self.nome

class Login:
    def __init__(self, login: str):
        if not self._validar_login(login):
            raise ValueError(
                "Login inválido. Use apenas letras, números, ponto ou underline (mínimo 3 caracteres)."
            )
        self.login = login

    def __str__(self):
        return self.login

    def __eq__(self, other):
        if isinstance(other, Login):
            return self.login.lower() == other.login.lower()
        return False

    @staticmethod
    def _validar_login(login: str) -> bool:
        """Login deve ter pelo menos 3 caracteres e conter apenas letras, números, pontos ou underline."""
        padrao = r"^[a-zA-Z0-9._]{3,}$"
        return re.match(padrao, login) is not None

class Senha:
    def __init__(self, senha: str):
        if not self._validar_forca(senha):
            raise ValueError(
                "Senha fraca. Use pelo menos 8 caracteres, com letras e números."
            )
        self.hash_senha = self._gerar_hash(senha)

    def verificar(self, senha: str) -> bool:
        """Verifica se a senha informada confere com o hash."""
        return self.hash_senha == self._gerar_hash(senha)

    def _gerar_hash(self, senha: str) -> str:
        """Cria o hash SHA256 da senha."""
        return hashlib.sha256(senha.encode()).hexdigest()

    @staticmethod
    def _validar_forca(senha: str) -> bool:
        """Verifica se a senha é forte o suficiente."""
        tem_letra = any(c.isalpha() for c in senha)
        tem_numero = any(c.isdigit() for c in senha)
        return len(senha) >= 8 and tem_letra and tem_numero

    def __str__(self):
        """Evita exibir a senha real."""
        return "********"

class TipoTrabalho:
    tabela = {
        "Coroa": 90,
        "Inlay": 90,
        "Coroa Sobre Implante": 90,
        "Faceta": 90,
        "Enceramento": 45,
        "Placa de Mordida": 300,
    }

    def __init__(self, tipo: str):
        self.validar_tipo(tipo)
        self.tipo = tipo
        self.valor = self.tabela[tipo]

    @classmethod
    def validar_tipo(cls, tipo: str):
        if tipo not in cls.tabela:
            raise ValueError(f"Tipo de trabalho inválido: {tipo}")

class Dentes:
    QUADRANTES_VALIDOS = ['1', '2', '3', '4']
    POSICOES_VALIDAS = ['1', '2', '3', '4', '5', '6', '7', '8']
    GRUPOS_VALIDOS = {
                      'A': ['1','2','3','3,5','4'],
                      'B': ['1','2','3','4'],
                      'C': ['1','2','3','4'],
                      'D': ['1','2','3'],
                      'BL':['1','2','3','4']
                    }
    TRANSLUCIDEZ_VALIDAS = ['LT', 'HT', '']  # inclui vazio como válido

    def __init__(self, numeros: list[str], cor: str, translucidez: str = ""):
        """
        Cria um grupo de dentes com uma cor e translucidêz específicas.
        Exemplo: Dentes(['11', '12'], 'A2', 'LT') ou Dentes(['11', '12'], 'A2')
        """
        self.numeros = numeros
        self.cor = cor
        self.translucidez = translucidez

        # Validação dos números
        for n in self.numeros:
            if not self._validar_numero(n):
                raise ValueError(f"Número de dente inválido: {n}")

        # Validação da cor e translucidêz
        if not self._validar_cor(self.cor, self.translucidez):
            raise ValueError(f"Cor inválida: {self.translucidez}{self.cor}")
    
    @staticmethod
    def separar_cor(cor: str):
        """
        Recebe algo como 'A3,5', 'BL4', 'C2', etc.
        Retorna uma tupla (grupo, matiz)
        """
        cor = cor.strip().upper()

        if cor.startswith('BL'):
            grupo = 'BL'
            matiz = cor[2:]
        else:
            grupo = cor[0]
            matiz = cor[1:]

        return (grupo,matiz)


    def _validar_numero(self, numero: str) -> bool:
        """Valida um número de dente individual"""
        return (
            len(numero) == 2 and
            numero[0] in self.QUADRANTES_VALIDOS and
            numero[1] in self.POSICOES_VALIDAS
        )

    def _validar_cor(self, cor: str, translucidez: str) -> bool:
        """
        Valida a cor e a translucidêz separadamente.
        Exemplo de válidos: ('A2',''), ('A3,5','LT'), ('BL4','HT')
        """
        grupo, matiz = self.separar_cor(cor)

        # 1. Translucidez deve ser válida (pode ser vazia)
        if translucidez not in self.TRANSLUCIDEZ_VALIDAS:
            print(f" Translucidez inválida: {translucidez}")
            return False

        # 2. Grupo deve existir
        if grupo not in self.GRUPOS_VALIDOS:
            print(f"Grupo de cor inválido: {grupo}")
            return False

        # 3. Matiz deve ser válida dentro do grupo
        if matiz not in self.GRUPOS_VALIDOS[grupo]:
            print(f"Matiz inválida '{matiz}' para o grupo {grupo}")
            return False

        # Tudo certo
        return True

    def __repr__(self):
        """Retorna a lista de dentes e a cor"""
        lista = ", ".join(self.numeros)
        return f"Dentes([{lista}], cor={self.cor})"