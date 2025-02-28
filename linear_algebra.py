import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from math import *
class Matrix():
    def __init__(self,np_array):
        dmsn= np_array.shape[0]#dmsn stands for dimension
        rows=[f"Row{i+1}" for i in range(dmsn)]
        columns=[f"Col{i+1}" for i in range(dmsn)]
        self.matrix= pd.DataFrame(np_array,columns=columns,index=rows)
        mat= pd.DataFrame(np_array,columns=columns,index=rows)
det_func_calls=0 #number of calls for the determinant function
#Calculates the determinant of a Square Matrix
def det(matrix):
    global det_func_calls
    det_func_calls+=1
    matrix_size= matrix.shape[0]
    result=0
    if matrix_size>2:
        for i in range(matrix_size):
            m=matrix.copy()
            factor= m.loc["Row1",f"Col{i+1}"]
            sign= pow(-1,i)
            m.drop(columns= f"Col{i+1}",index=f"Row1",inplace=True)#remove the "i"th column and 1st row
            rows= [f"Row{x+1}" for x in range(matrix_size-1)]
            cols= [f"Col{x+1}" for x in range(matrix_size-1)]
            m.columns= cols
            m.index= rows
            result+= factor*sign*det(m)
        return result
    else:
        return matrix.loc["Row1","Col1"]*matrix.loc["Row2","Col2"]-matrix.loc["Row1","Col2"]*matrix.loc["Row2","Col1"]
#returns the adjoint/ adjugate for a given square matrix
def adj(matrix):
    matrix_size= matrix.shape[0]
    adj_matrix=np.zeros((matrix_size,matrix_size))
    for i in range(matrix_size):
        for j in range(matrix_size):
            m= matrix.copy()
            sign= pow(-1,i+j)
            m.drop(columns= f"Col{j+1}",index=f"Row{i+1}",inplace=True)
            rows= [f"Row{x+1}" for x in range(matrix_size-1)]
            cols= [f"Col{x+1}" for x in range(matrix_size-1)]
            m.columns= cols
            m.index= rows
            adj_matrix[i,j]=sign*det(m)
    adj_matrix= adj_matrix.T
    return Matrix(adj_matrix).matrix
if __name__== "__main__":
    my_matrix= np.random.randn(6,6)
    my_matrix= Matrix(my_matrix)
    print(f"My Matrix:\n{my_matrix.matrix}")
    Det= det(my_matrix.matrix)
    print(f"\nDeterminant:{Det}")
    print(f"\nFunction calls for determinant function:{det_func_calls}")
    ADJ= adj(my_matrix.matrix)
    print("The inverse of the matrix:\n")
    inverse_mat= ADJ/Det
    print(f"{inverse_mat}\n\nProduct of matrix and its inverse(Identity Matrix):")
    x= np.array(my_matrix.matrix)
    y= np.array(inverse_mat)
    print(Matrix(np.matmul(x,y)).matrix)
    #Investigate the relationship between determinant function calls and matrix size
    det_func_calls_arr=[]
    for i in range(3,9):
        det_func_calls=0
        my_matrix= np.random.randn(i,i)
        my_matrix= Matrix(my_matrix)
        Det= det(my_matrix.matrix)
        det_func_calls_arr.append(det_func_calls)
    plt.title("Computational Complexity")
    plt.grid(True)
    sns.lineplot(pd.DataFrame({"Function Calls":det_func_calls_arr,"Matrix Size":list(range(3,9))}),x="Matrix Size",y="Function Calls")
    plt.show()