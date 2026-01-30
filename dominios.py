import json
import os

class Medicacao:
    arquivo_json = "remedios.json"  # arquivo padrão, pode ser alterado se necessário

    def __init__(self, nome: str, classificacao: str, descricao: str):
        self.nome = nome
        self.classificacao = classificacao
        self.descricao = descricao

    @classmethod
    def _carregar_remedios(cls):
        """Carrega o dicionário de remédios do JSON, ou retorna um vazio se não existir."""
        if os.path.exists(cls.arquivo_json):
            with open(cls.arquivo_json, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    @classmethod
    def _salvar_remedios(cls, remedios):
        """Salva o dicionário de remédios no arquivo JSON."""
        with open(cls.arquivo_json, "w", encoding="utf-8") as f:
            json.dump(remedios, f, ensure_ascii=False, indent=4)

    def adicionar_medicacao(self):
        remedios = self._carregar_remedios()
        remedios[self.nome] = {
            "classificacao": self.classificacao,
            "descricao": self.descricao
        }
        self._salvar_remedios(remedios)
        print(f"Medicação '{self.nome}' adicionada/atualizada com sucesso!")

    def remover_medicacao(self):
        remedios = self._carregar_remedios()
        if self.nome in remedios:
            del remedios[self.nome]
            self._salvar_remedios(remedios)
            print(f"Medicação '{self.nome}' removida com sucesso!")
        else:
            print(f"Medicação '{self.nome}' não encontrada no arquivo.")

    @classmethod
    def listar_todas(cls):
        remedios = cls._carregar_remedios()
        if not remedios:
            print("Nenhuma medicação encontrada.")
            return
        print("Lista de todas as medicações:")
        for nome, info in remedios.items():
            print(f"- {nome} ({info['classificacao']}): {info['descricao']}")

    @classmethod
    def buscar_medicacao(cls, nome):
        remedios = cls._carregar_remedios()
        if nome in remedios:
            info = remedios[nome]
            print(f"{nome} ({info['classificacao']}): {info['descricao']}")
        else:
            print(f"Medicação '{nome}' não encontrada.")
