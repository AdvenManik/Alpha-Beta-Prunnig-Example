class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def alpha_beta_pruning(node, alpha, beta, maximizing_player):
    if len(node.children) == 0:
        return node.value
    
    if maximizing_player:
        value = float('-inf')
        for child in node.children:
            value = max(value, alpha_beta_pruning(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alpha_beta_pruning(child, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

# Buat pohon pencarian
root = Node(None)
root.children = [Node(3), Node(8), Node(12), Node(2), Node(4), Node(6), Node(14), Node(5), Node(2)]

# Jalankan algoritma alpha-beta pruning
result = alpha_beta_pruning(root, float('-inf'), float('inf'), True)
print("Nilai terbaik yang diperoleh:", result)
