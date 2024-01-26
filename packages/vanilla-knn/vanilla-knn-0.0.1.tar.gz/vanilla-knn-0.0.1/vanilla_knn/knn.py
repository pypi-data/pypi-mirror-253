from functools import reduce

def euclidean_distance(x1, x2):
    
    """
    Calcula a distância euclidiana entre dois pontos no espaço.

    Esta função recebe dois pontos, 'x1' e 'x2', e retorna a distância euclidiana entre eles.

    Parâmetros:
    x1 (array-like): Coordenadas do primeiro ponto.
    x2 (array-like): Coordenadas do segundo ponto.

    Retorna:
    float: A distância euclidiana entre os pontos 'x1' e 'x2'.
    """
    squared_diff = [(x1[i] - x2[i]) ** 2 for i in range(len(x1))]
    total_sum = reduce(lambda x, y: x + y, squared_diff)
    return total_sum ** (1/2)

class k_neighbors_classifier():
    def __init__(self, n_neighbors=3):
        self.n_neighbors = n_neighbors
    
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
    
    def predict(self, X_test):
        return [self.mode_neighbors(self.get_neighbors(x)) for x in X_test]
    
    def get_neighbors(self, x):
        distance_between = [(idx, euclidean_distance(x, self.X_train[idx])) for idx in range(len(self.X_train))]
        sorted_distance_between = sorted(distance_between, key=lambda x: x[1])
        idx_neighbors = [idx for idx, distance in sorted_distance_between]

        return idx_neighbors[:self.n_neighbors]
    
    def mode_neighbors(self, idx_neighbors):
        labels = [self.y_train[idx] for idx in idx_neighbors]
        frequency_dict = {label: labels.count(label) for label in set(labels)}
        sorted_frequency_dict = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
        return sorted_frequency_dict[0][0]