
# tree_logic.py — você edita APENAS este arquivo nesta atividade.

class Node:
    def __init__(self, question, yes=None, no=None):
        """
        Se 'yes' e 'no' forem None, este nó é uma FOLHA e 'question' guarda a decisão final (string).
        Caso contrário, 'question' é o texto da pergunta e 'yes'/'no' são seus filhos.
        """
        self.question = question
        self.yes = yes
        self.no = no

def is_leaf(node):
    return node is not None and node.yes is None and node.no is None

def navigate_tree(node, answers):
    """
    Percorre a árvore a partir de 'node' seguindo a sequência de respostas (lista de strings).
    Cada resposta deve ser 'sim' ou 'não' (aceite 'nao' como 'não').
    Retorna a decisão final (string) quando alcançar uma folha.
    Se a sequência terminar antes de chegar a uma folha, levante ValueError com dica.
    Se alguma resposta for inválida, levante ValueError com mensagem clara.
    >>> # Exemplo (não-executável aqui): navigate_tree(root, ["sim", "não"]) -> "É um pardal/pássaro diurno"
    """
    # TODO: implemente aqui. Sugestão:
    # - Enquanto o nó atual não for folha:
    #     - Se não houver mais respostas, levante ValueError("Faltam respostas para concluir a decisão.")
    #     - Pegue a próxima resposta, normalize para minúsculas, trate 'nao' como 'não'.
    #     - Se "sim": vá para node.yes; se "não": vá para node.no; senão levante ValueError("Resposta inválida: ...")
    # - Ao chegar numa folha, retorne node.question (a decisão final).
    raise NotImplementedError("Implemente a função navigate_tree.")

#o codigo completo com a função recebida:

def navigate_tree(node, answers):
    """
    Percorre a árvore a partir de 'node' seguindo a sequência de respostas.
    """
    current_node = node
    idx = 0
    
    # Helper para identificar se é folha (assumindo que folhas não têm filhos)
    # Ajuste a condição conforme a estrutura da sua classe Node real
    def is_leaf(n):
        return n.yes is None and n.no is None

    while not is_leaf(current_node):
        # Verifica se acabaram as respostas antes de chegar numa folha
        if idx >= len(answers):
            raise ValueError("Faltam respostas para concluir a decisão.")
        
        raw_answer = answers[idx]
        normalized_answer = raw_answer.strip().lower()
        
        # Normalização específica pedida
        if normalized_answer == 'nao':
            normalized_answer = 'não'
            
        if normalized_answer == 'sim':
            current_node = current_node.yes
        elif normalized_answer == 'não':
            current_node = current_node.no
        else:
            raise ValueError(f"Resposta inválida: '{raw_answer}'. Esperado 'sim' ou 'não'.")
            
        idx += 1

    # Ao chegar numa folha, retorna a decisão (question)
    return current_node.question

class DecisionNode:
    def __init__(self, question, yes=None, no=None):
        self.question = question
        self.yes = yes
        self.no = no

# --- Cenário de Teste ---

# Construindo a árvore:
# Pergunta: Tem penas?
#   - Sim: Voa?
#       - Sim: Pardal (Folha)
#       - Não: Avestruz (Folha)
#   - Não: Tem escamas?
#       - Sim: Cobra (Folha)
#       - Não: Sapo (Folha)

leaf_pardal = DecisionNode("É um Pardal")
leaf_avestruz = DecisionNode("É um Avestruz")
leaf_cobra = DecisionNode("É uma Cobra")
leaf_sapo = DecisionNode("É um Sapo")

node_voa = DecisionNode("O animal voa?", yes=leaf_pardal, no=leaf_avestruz)
node_escamas = DecisionNode("O animal tem escamas?", yes=leaf_cobra, no=leaf_sapo)
root = DecisionNode("O animal tem penas?", yes=node_voa, no=node_escamas)

# Testando a navegação
try:
    # Caminho: Não (tem penas) -> Sim (tem escamas) -> Cobra
    resultado = navigate_tree(root, ["nao", "SIM"]) 
    print(f"Resultado: {resultado}") # Esperado: É uma Cobra

    # Teste de erro (falta resposta)
    # navigate_tree(root, ["sim"]) 

except ValueError as e:
    print(f"Erro: {e}")