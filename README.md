Matrices are a very useful tool in Mathematics and various scientific fields. In this project I was mainly trying to focus on square matrices.
The 2 most important properties of any given matrix are its determinant and its adjoint/adjugate. Knowing these 2 properties are valuable in Linear Algebra.
My module mainly consists of 4 parts :(A)Creating a matrix Class (B) The determinant function (C) The Adjoint function (D)Computational Complexity Analysis
The Matrix class takes a numpy array as an instance and has only one property "matrix" which is a pandas DataFrame.
The determinant function uses recursion to compute the determinant of any given square matrix.However since Python has a resursion limit it can only handle an 8X8 matrix and below.
The adjoint function calls the determinant function for every element in the matrix to coumpute their respective co-factors and returns the adjoint matrix.
In Computational Complexity Analysis ,I investigate the effect of increasing the matrix size on the number of recursive function calls. 
