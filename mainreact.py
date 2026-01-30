from atributos import *
from dominios import *

def main():
    try:
        # Cria técnico
        tecnico1 = Tecnico("João da Silva", "joao.silva", "senha1234")

        # Cria paciente
        paciente1 = Paciente("Maria Souza", 1)

        # Cria um trabalho
        trabalho1 = Trabalho(
            paciente=paciente1,
            tecnico=tecnico1,
            dataInicio="01/10/2025",
            dataFinal="15/10/2025",
            tipo="Coroa",
            dentes=["11", "12", "13"],
            cor="A3,5",
            translucidez="HT"
        )

        # Mostra os dados
        print(trabalho1)

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()