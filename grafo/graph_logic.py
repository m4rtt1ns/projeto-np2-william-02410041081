
# graph_logic.py — você edita APENAS este arquivo nesta atividade.
# Dica: use apenas LISTAS para a fila/estrutura de dados (nada de deque).
# Você pode fazer BFS com:
#   fila = [a]; visitados = [a]
#   while fila:
#       u = fila.pop(0)          # remove o primeiro
#       if u == b: return True
#       for v in graph.get(u, []):
#           if v not in visitados:
#               visitados.append(v)
#               fila.append(v)
#   return False
#
# Alternativamente, pode usar DFS com uma lista como "pilha":
#   pilha = [a]; visitados = []
#   while pilha:
#       u = pilha.pop()          # remove o último
#       ...
#   return False

def connected(graph, a, b):
    """
    Retorna True se existe um caminho (qualquer) entre 'a' e 'b' no grafo não direcionado.
    'graph' é um dicionário: { "Ana": ["Beto", ...], ... }
    Implemente uma busca simples (BFS com listas ou DFS com listas).
    Tratamento recomendado:
      - Se 'a' ou 'b' não existirem como vértices, você pode retornar False OU levantar ValueError.
      - Pode normalizar maiúsculas/minúsculas, desde que seja consistente.
    """
    # TODO: implemente aqui usando APENAS listas.
    # Exemplo (BFS com lista), em pseudocódigo:
    # if a not in graph or b not in graph:
    #     return False
    # fila = [a]
    # visitados = [a]
    # while fila:
    #     u = fila.pop(0)
    #     if u == b:
    #         return True
    #     for v in graph.get(u, []):
    #         if v not in visitados:
    #             visitados.append(v)
    #             fila.append(v)
    # return False
    raise NotImplementedError("Implemente a função connected usando apenas listas.")

#LOGO ABAIXO O CODIGO COMPLETO:

def connected(graph, a, b):
    """
    Retorna True se existe um caminho (qualquer) entre 'a' e 'b' no grafo não direcionado.
    'graph' é um dicionário: { "Ana": ["Beto", ...], ... }
    """
    # Verificação de existência dos nós no grafo
    # Assumindo que as chaves do dicionário contêm todos os nós válidos
    if a not in graph or b not in graph:
        return False
    
    # Caso base: o início é o fim
    if a == b:
        return True

    # Inicialização da BFS usando listas
    fila = [a]
    visitados = [a]  # Usando lista para rastrear visitados (conforme restrição)

    while fila:
        # Remove o primeiro elemento da lista para simular comportamento de Fila (FIFO)
        # Obs: pop(0) tem custo O(n), mas atende ao requisito de não usar deque
        u = fila.pop(0)

        if u == b:
            return True

        # Itera sobre os vizinhos
        # O .get(u, []) previne erros caso 'u' não tenha vizinhos listados (folha ou isolado)
        for v in graph.get(u, []):
            if v not in visitados:
                visitados.append(v)
                fila.append(v)

    return False
