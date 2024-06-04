from blessings import Terminal
from openai import OpenAI

client = OpenAI(
    api_key='sk-proj-pn39wZ2coe9PYahP09yXT3BlbkFJHoM2Gi2SUdUKc3MK0j4s'
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
               You are a very experienced developer with knowledge in different stacks and theoretical concepts about programming and software engineering. You are working on generating tests for Benchmark codes using the All-sync-edges testing criterion. Analyze the provided code and generate the test set using the All-sync-edges testing criterion.
               
                About test criteria consider:
                Thus, for a given parallel program "ProgPar" composed of processes labeled as $P^0, P^1, \ldots, P^{n-1}$, each process $P_i$ has its Control Flow Graph (CFG), constructed similarly to sequential programs.
                Therefore, a node $n$ may or may not involve a communication function such as "send" or "receive". Based on this, a Parallel Control Flow Graph (PCFG) is constructed for "ProgPar", comprising the CFGs of all processes within "ProgPar" and communication edges between parallel processes. It's important to note that, in this model, the sets of nodes and edges are denoted by $N$ and $E$ respectively. A node $i$ in process $p$ is represented as $n^p_i$. Additionally, two node subsets are defined: $N_s$ containing nodes with message sending functions, and $N_r$ containing nodes with message receiving primitives.
                For each $n^p_i \in N_s$, a set $R^p_i$ is associated, indicating the possible nodes that could receive the message sent by node $n^p_i$. PCFG edges can occur in two ways:
                Intra-process edges ($E_i$): internal edges within a process $p$.
                Inter-process edges ($E_s$): edges representing communication between different processes.
                
                All-sync-edges: Requires that all edges of the $E_s$ set be exercised at least once by the test set.
            
                Give me tests in following format:
                Data Test [1]: [input, input] length array is equal number of params
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
