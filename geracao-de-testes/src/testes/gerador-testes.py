from blessings import Terminal
from openai import OpenAI

client = OpenAI(
    api_key='insira sua chave aqui'
)


def ler_codigo_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        return arquivo.read()


def gerar_analise(codigo):
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": """
                Você é um desenvolvedor muito experiente com conhecimento em diferentes stacks e conceitos teóricos sobre programação e engenharia de software.
                Você está trabalhando na geração de testes dos códigos dos Benchmarks usando o critério de teste All-sync-edges.
                Analise o código fornecido e gere o conjunto de testes usando o critério de teste All-sync-edges.
            """
        }, {
            "role": "user",
            "content": f"Aqui está o código do Benchmark:\n\n{codigo}\n\nGere uma análise dos testes usando o critério de teste All-sync-edges."
        }]
    )

    return resposta.choices[0].message.content


term = Terminal()
caminho_arquivo = input(
    "Insira o caminho para o arquivo de código do Benchmark: ")

codigo_benchmark = ler_codigo_arquivo(caminho_arquivo)

print("Carregando...")
analise = gerar_analise(codigo_benchmark)

print(term.clear)
print(term.bold("Análise dos Testes Usando o Critério de Teste All-sync-edges:"))
print(analise)
