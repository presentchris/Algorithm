import numpy as np

def min_max_scaler(X):
    X_min = X.min(axis=0)
    X_max = X.max(axis=0)
    X_norm = (X - X_min) / (X_max - X_min)
    return X_norm

# 샘플 데이터 생성
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Min-Max Scaling 적용
X_scaled = min_max_scaler(X)

print("Original X:")
print(X)
print("\nScaled X:")
print(X_scaled)
