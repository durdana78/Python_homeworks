import numpy as np
random_matrix = np.random.rand(5,5)

min_value = np.min(random_matrix)
max_value = np.max(random_matrix)

normalized_matrix = (random_matrix - min_value) / (max_value - min_value)

print(random_matrix)
print(f"Normalized matrix: {normalized_matrix}")