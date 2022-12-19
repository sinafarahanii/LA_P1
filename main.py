import numpy as np


def step1(matrix1):
    for j in range(C-1):
        matrix1[j] = np.multiply(matrix1[j], 1 / matrix1[j, j])
        for i in range(j+1, R):
            matrix1[i] = np.add(matrix1[i], np.multiply(matrix1[j], -matrix1[i, j]))
    print(matrix1)


R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
print(
    f"Enter the entries in a single line (separated by space)\ne.g., if the number of rows and columns=2\n1 2 3 4 "
    f"-->\n[[1 2]\n [3 4]]\n{R * C} numbers expected: ")
entries = list(map(float, input().split()))
matrix = np.array(entries).reshape(R, C)
#print(matrix)
step1(matrix)

