from simple_term_menu import TerminalMenu
import numpy as np
import click as cl

def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    matrix = np.empty((rows, cols), dtype=float)
    
    print("Enter matrix elements:")
    for i in range(rows):
        for j in range(cols):
            value = float(input(f"Enter value for row {i + 1}, column {j + 1}: "))
            matrix[i, j] = value
    
    return matrix

def add_matrices(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        raise ValueError("Matrices must have the same shape for addition.")
    
    result_matrix = matrix1 + matrix2
    return result_matrix

def calculate_matrix_inverse(matrix):
    try:
        inverse_matrix = np.linalg.inv(matrix)
        return inverse_matrix
    except np.linalg.LinAlgError:
        raise ValueError("Matrix is singular and does not have an inverse.")

def calculate_transpose_alt(matrix):
    return matrix.T

def multiply_matrices(matrix1, matrix2):
    try:
        product_matrix = np.dot(matrix1, matrix2)
        return product_matrix
    except ValueError:
        raise ValueError("Matrix dimensions are not suitable for multiplication.")

def first_menu():
    print("=========0xabdelbari_zaoui.exe Copyrights=============|")
    print("======================Welcome=========================|")
    print("======================Menu============================|")
    print("   Welcome, you can work with one matrix or two       |")    
    options =  ["1.   Work with One Matrix","2.   Work with Two Matrices","3.   Exit"]
    main_menu = TerminalMenu(options)
    quit = False
    while not quit:
        optionsIndex = main_menu.show()
        optionsChoice = options[optionsIndex]
        if optionsChoice == "1.   Work with One Matrix":
            sub_menu1()
        if optionsChoice == "2.   Work with Two Matrices":
            sub_menu2()
        elif optionsChoice == "3.   Exit":
            quit = True

def sub_menu1():
    opt1 = ["1. Enter & print your matrix", "2. Calculate & print the inverse of a matrix", "3. Give me the matrix transposed", "4. Go back", "5. Exit"]
    main_menu1 = TerminalMenu(opt1)
    while True:
        optionsIndex = main_menu1.show()
        optionsChoice = opt1[optionsIndex]
        if optionsChoice == "1. Enter & print your matrix":
            matrix1 = input_matrix()
            print(matrix1)
            print("==================================")
        elif optionsChoice == "2. Calculate & print the inverse of a matrix":
            inverse = calculate_matrix_inverse(matrix1)
            print(inverse)
            print("==================================")
        elif optionsChoice == "3. Give me the matrix transposed":
            transposed = calculate_transpose_alt(matrix1)
            print(transposed)
        elif optionsChoice == "4. Go back":
            return
        elif optionsChoice == "5. Exit":
            exit()

def sub_menu2():
    opt2 = ["1. Enter & print your matrices", "2. Add two matrices", "3. Multiply two matrices", "4. Go back", "5. Exit"]
    main_menu2 = TerminalMenu(opt2)
    while True:
        optionsIndex = main_menu2.show()
        optionsChoice = opt2[optionsIndex]
        if optionsChoice == "1. Enter & print your matrices":
            matrix1 = input_matrix()
            print(matrix1)
            matrix2 = input_matrix()
            print(matrix2)
            print("==================================")
        elif optionsChoice == "2. Add two matrices":
            result1 = add_matrices(matrix1, matrix2)
            print(result1)
            sub_menu2_1(result1, matrix2)
            print("==================================")
        elif optionsChoice == "3. Multiply two matrices":
            result2 = multiply_matrices(matrix1, matrix2)
            print(result2)
            print("==================================")
        elif optionsChoice == "4. Go back":
            return
        elif optionsChoice == "5. Exit":
            exit()

def sub_menu2_1(result1, matrix2):
    opt2_1 = ["1. Calculate & print the inverse of a matrix", "2. Give me the matrix transposed", "3. Go back", "4. Exit"]
    main_menu2_1 = TerminalMenu(opt2_1)
    while True:
        optionsIndex = main_menu2_1.show()
        optionsChoice = opt2_1[optionsIndex]
        if optionsChoice == "1. Calculate & print the inverse of a matrix":
            result3 = calculate_matrix_inverse(result1)
            print(result3)
            print("==================================")
        elif optionsChoice == "2. Give me the matrix transposed":
            result4 = calculate_transpose_alt(result1)
            print(result4)
            print("==================================")
        elif optionsChoice == "3. Go back":
            return
        elif optionsChoice == "4. Exit":
            exit()

if __name__ == "__main__":
    first_menu()
