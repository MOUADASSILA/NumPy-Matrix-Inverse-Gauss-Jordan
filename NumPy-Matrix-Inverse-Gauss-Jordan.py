#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:37:28 2024

@author: mac
"""

import numpy as np  # dakhalna numpy bach ndiro hssabat mathematique

def gauss_jordan_inverse(matrix):
    # Gha3dine nchoufou ch7al men sater ou 3amoud 3ndna
    rows, cols = matrix.shape
    if rows != cols:
        raise ValueError("MATRIS KARE OLMALIDIR.")  # Khass lmatrix tkoun kare bach n9drou n7sbou t-ters dyalha

    augmented_matrix = np.hstack((matrix, np.eye(rows)))  # rbatna lmatrix l'asliya m3a lmatrix l'identite
    for i in range(rows):
        pivot = augmented_matrix[i, i]
        if pivot == 0:
            raise ValueError("MATRISIN TERSI YOKTUR.")  # Ila kan pivot = 0, lmatrix ma 3ndhash t-ters

        augmented_matrix[i] = augmented_matrix[i] / pivot  # Mnoramlizaw l-sater 3la l-pivot

        for j in range(rows):
            if i != j:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]  # N9aydou l-elementat l-khara bach ywsslo 0

    inverse_matrix = augmented_matrix[:, cols:]  # Nakhdo ghi l-partie l-taania dyal lmatrix l-mwss3a bach nakhdo t-ters
    return inverse_matrix

matrix = np.array([[2, 1, 1], [1, -1, 0], [3, -1, 2]], dtype=float)  # Hadi hiya lmatrix l'asliya

try:
    inverse = gauss_jordan_inverse(matrix)  # Kan7awlou n7sbou t-ters
    print("MATRISIN TERSI:\n", inverse)  # Kan3rdou t-ters
except ValueError as e:
    print(e)  # Ila kan chi khata, nkhrjo l-khata
