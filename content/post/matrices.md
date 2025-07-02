---
author: TheSusian
title: Matrices
date: 2023-10-15
description: University notes for matrices
math: true
tags: [linear algebra, notes]
---

> I have very little knowledge about this topic I'm writing about as I'm still learning it, some information here might be wrong or inaccurate. These are just my personal notes that I decided to publish in case someone might find them useful, feel free to point out any mistakes by sending me an email :)

The following is a matrix of size \\(m\times n\\)

$$
  A_{m\times n} =
  \left[ {\begin{matrix}
    a_{11} & a_{12} & \cdots & a_{1n}\\\\
    a_{21} & a_{22} & \cdots & a_{2n}\\\\
    \vdots & \vdots & \ddots & \vdots\\\\
    a_{m1} & a_{m2} & \cdots & a_{mn}\\\\
  \end{matrix}} \right]
$$

Not that unlike normal coordinates, when we reference an element, we first reference the column *then* the row, they are ***Reversed***

## Types

You have **Real** matrices and **Complex** matrices, but there is nothing special about either now so I will omit them

### Complex Matrices

Matrices with complex numbers in them, the only important thing here is to remember that \\(\overline{AB}=\overline{A}\cdot \overline{B}\\)

*reminder: \\(z=a+bi\\) and \\(\overline{z}=a-bi\\)*
### Square Matrices

Exactly what they sound like, like \\(A_{n\times n}\\) and they can be complex of real, does not matter, most of our work will be on these, they are explained below

### Vectors (Column Matrices)

Row matrices can also be considered vectors, basically these are 1 dimensional matrices like \\(V = \left[ {\begin{matrix} 1 & 2 & 3 & 4 \end{matrix}} \right]\\)
\\(R^n\\) is the set of all n-vectors with real entries and \\(\mathbb{C}^n\\) is the same but for complex entries

## Operations

### Addition/Subtraction

You can get the sum or difference of two matrices only if they were the *same size*, you will add them just like you'd expect, each element with the corresponding element in the other matrix

### Scalar Multiplication

Multiplication of a real number with a matrix, also works just like you'd expect, multiplying the number with each element of the matrix

$$
  A =
  \left[ {\begin{matrix}
	1 & 2 & 3\\\\
	4 & 5 & 6\\\\
  \end{matrix}} \right]
  \quad
  A\cdot 2=
    \left[ {\begin{matrix}
	2 & 4 & 6\\\\
	8 & 10 & 12\\\\
  \end{matrix}} \right]
$$

### Transposal

Is getting the **Transposition** of a matrix, to do this, we interchange the rows and the columns of a matrix, it's denoted as \\(A^T\\)

$$
  A =
  \left[ {\begin{matrix}
	1 & 2 & 3\\\\
	4 & 5 & 6\\\\
  \end{matrix}} \right]
  \quad
  A^T=
    \left[ {\begin{matrix}
	1 & 4\\\\
	2 & 5\\\\
	3 & 6\\\\
  \end{matrix}} \right]
$$

### Matrix Multiplication

Multiplying a matrix by another, this will be interesting

#### Vectors

*AKA (Dot/Scalar) product*
Dot products for n-vectors can be denoted as \\(\overrightarrow{a}\cdot\overrightarrow{b}\\)  or \\((<\overrightarrow{a},\overrightarrow{b}>)\\)
To get the dot product, we multiply each two corresponding numbers in the vector then add them all together
$$
    \overrightarrow{a}\cdot\overrightarrow{b} = a_1\cdot b_1 + a_2\cdot b_2+\cdots +a_n\cdot b_n
$$

#### Normal Matrices

To multiply two matrices, the number of rows in one *must* equal the number of columns in the other, so \\(A_{p\times m}\times B_{n\times p}\\) can be multiplied and the result will be of size \\(n\times m\\)
To do it we multiply each element from the first set with it's corresponding element in the first column of the second set and add the results, this result will be the 1st element of our new matrix, then do the same for the rest of the first set
I know my explanation is bad so here are 2 examples to give you a better chance of understanding

$$
 A_{1\times3}=\left[ {\begin{matrix}
	1 & 2 & 3\\\\
  \end{matrix}} \right]
\quad
 B_{3\times2}=\left[ {\begin{matrix}
	1 & 2\\\\
	3 & 4\\\\
	5 & 6\\\\
  \end{matrix}} \right]
\quad
 A\cdot B=C_{1\times2}=
  \left[ {\begin{matrix}
	22 & 28
  \end{matrix}} \right]
$$

Explanation

$$
    C=\left[ {\begin{matrix}
        1\cdot1+2\cdot3+3\cdot5 & 1\cdot2+2\cdot4+3\cdot6
    \end{matrix}} \right]
    =
    \left[ {\begin{matrix}
        22 & 28
    \end{matrix}} \right]
$$

And another example for clarity

$$
 A_{2\times3}=\left[ {\begin{matrix}
	1 & 2 & 3\\\\
	4 & 5 & 6\\\\
  \end{matrix}} \right]
\quad
 B_{3\times3}=\left[ {\begin{matrix}
	7  & 8  & 9 \\\\
	10 & 11 & 12\\\\
	13 & 14 & 15\\\\
  \end{matrix}} \right]
\quad
 A\cdot B=C_{2\times3}=
  \left[ {\begin{matrix}
	66  & 72  & 78 \\\\
	156 & 171 & 186\\\\
  \end{matrix}} \right]
$$

And it's explanation

$$
C=
    \left[ {\begin{matrix}
        1\cdot7+2\cdot10+3\cdot13  & 1\cdot8+2\cdot11+3\cdot14  & 1\cdot9+2\cdot12+3\cdot15 \\\\
        4\cdot7+5\cdot10+6\cdot13  & 4\cdot8+5\cdot11+6\cdot14  & 4\cdot9+5\cdot12+6\cdot15 \\\\
    \end{matrix}} \right]
    =
    \left[ {\begin{matrix}
        66  & 72  & 78 \\\\
        156 & 171 & 186\\\\
    \end{matrix}} \right]
$$

Now we get into the "fun" part

## Square Matrices

Matrices that are squares..., interesting right?

### Trace

We can find a ***Trace*** for the matrix, denoted as \\(\mathrm{Tr}(A)\\), by adding all elements on the matrix's diagonal
$$
  A =
  \left[ {\begin{matrix}
	1 & 2 & 3\\\\
	4 & 5 & 6\\\\
	7 & 8 & 9\\\\
  \end{matrix}} \right]
  \quad
  \mathrm{Tr}(A)=1+5+9=15
$$

### Inverse

If \\(AB=BA=In\\) then \\(B\\) is said to be the *inverse* of \\(A\\), each matrix can have only 1 inverse, if a matrix doesn't have any inverses it's said to be a ***Nonsingular*** matrix, meaning it can't be reduced to an identity matrix ($In$), we can check if a matrix is nonsingular if its determinant is \\(0\\)

Consequently, if a matrix (\\(A\\)) is **nonsingular**, if \\(AB=AC\\) then \\(B=C\\)

### Stupid Types

Apparently we have to name EVERY POSSIBLE PATTERN in square matrices so here we go, I will list them with examples, I bet you are smart enough to figure it out

I suggest you try to prove my example manually to get a better understanding of how you do it, if I got something wrong contact me to tell me how stupid I am

#### Identity Matrix (\\(In\\))

$$
  \left[ {\begin{matrix}
	1 & 0 & 0\\\\
	0 & 1 & 0\\\\
	0 & 0 & 1\\\\
  \end{matrix}} \right]
$$

#### Upper Triangular

$$
  \left[ {\begin{matrix}
	1 & 2 & 3\\\\
	0 & 5 & 6\\\\
	0 & 0 & 9\\\\
  \end{matrix}} \right]
$$

#### Lower Triangular

$$
  \left[ {\begin{matrix}
	1 & 0 & 0\\\\
	4 & 5 & 0\\\\
	7 & 8 & 9\\\\
  \end{matrix}} \right]
$$

#### Symmetric

If \\(A=A^T\\)

$$
  \left[ {\begin{matrix}
	1 & 2 & 3\\\\
	2 & 5 & 6\\\\
	3 & 6 & 9\\\\
  \end{matrix}} \right]
$$

#### Skew

If \\(A=-A^T\\), note that the diagonal has to be all \\(0\\) for this to work

$$
  \left[ {\begin{matrix}
	0  & 1 & 2 \\\\
	-1 & 0 & -3\\\\
	-2 & 3 & 0 \\\\
  \end{matrix}} \right]
$$

#### Periodic

If \\(A=A^{p+1}\\) then \\(A\\) is a periodic matrix with a period of \\(p\\), if \\(A=A^2\\) then \\(A\\) is an ***Idempotent*** matrix

$$
A=\left[ {\begin{matrix}
	0  & 1\\\\
	-1 & 0\\\\
  \end{matrix}} \right]\implies A=A^5\implies p=4
$$

#### Nilpotent

If \\(A^q=0\\), \\(q\\) is called the *Index of nilpotency*

$$
A=\left[ {\begin{matrix}
	0 & 1 & 0\\\\
	0 & 0 & 1\\\\
	0 & 0 & 0\\\\
  \end{matrix}} \right]\implies A^3=0\implies q=3
$$

#### Involutory

If \\(A^2=In\\)
$$
A=\left[ {\begin{matrix}
	2  & 1  & 1 \\\\
	-1 & 5  & -1\\\\
	-2 & -2 & -1\\\\
  \end{matrix}} \right]\implies
A^2=\left[ {\begin{matrix}
	1 & 0 & 0\\\\
	0 & 1 & 0\\\\
	0 & 0 & 1\\\\
  \end{matrix}} \right]
$$

#### Orthogonal

If \\(AA^T=A^TA=In\\)
$$
\dfrac{1}{9}\left[ {\begin{matrix}
	-2 & 1  & 2\\\\
	2  & 2  & 1\\\\
	1  & -2 & 2\\\\
  \end{matrix}} \right]
$$

####  Hermitian

If \\(A=(\overline{A})^T\\)

$$
  \left[ {\begin{matrix}
	3   & 3+i\\\\
	3-i & 2  \\\\
  \end{matrix}} \right]
$$

#### Skew Hermitian

If \\(A=-(\overline{A})^T\\), no idea why this exists

$$
  \left[ {\begin{matrix}
	0   & -2+i\\\\
	2+i & 0  \\\\
  \end{matrix}} \right]
$$

## Echelon Forms

*From French "échelon" means "level" or a step of a ladder*

The number of steps is called the *rank* of the matrix, the two examples below are of rank \\(3$

### Row Echelon Form (REF)

For a matrix to be in *row echelon form* the following rules has to apply

1) All rows having only zero entries are at the bottom
2) All leading entries (first entry from the left) must be to the right of the entry above it (like a staircase), but note that the difference doesn't have to always be 1, it can be more

$$
  \left[ {\begin{matrix}
	1 & a_1 & a_2 & a_3 & a_4\\\\
	0 & 0   & 2   & a_5 & a_6\\\\
	0 & 0   & 0   & 7   & a_7\\\\
	0 & 0   & 0   & 0   & 0  \\\\
  \end{matrix}} \right]
$$

### Reduced Row Echelon Form (RREF)

very similar to REF with a few differences, the rules for a matrix to be in RREF are

1) It is in row echelon form
2) The leading entry is always \\(1\\)
3) All entries above the leading \\(1\\) must be \\(0\\)

$$
  \left[ {\begin{matrix}
	1 & a_1 & 0   & 0   & a_2\\\\
	0 & 0   & 1   & 0   & a_3\\\\
	0 & 0   & 0   & 1   & a_4\\\\
	0 & 0   & 0   & 0   & 0  \\\\
  \end{matrix}} \right]
$$

## Row Operations

Later we will need to convert a matrix to its echelon form, in order to do that, we will use row operations, we have 3 elementary operations

**Type I** - Interchanging rows, e.g. \\(R_x\leftrightarrow R_y\\)

$$
A= \left[ {\begin{matrix}
	1 & 2 & 3\\\\
	4 & 5 & 6\\\\
	7 & 8 & 9\\\\
  \end{matrix}} \right]\Longrightarrow R_1\leftrightarrow R_2 \Longrightarrow
  \left[ {\begin{matrix}
	4 & 5 & 6\\\\
	1 & 2 & 3\\\\
	7 & 8 & 9\\\\
  \end{matrix}} \right]
$$

**Type II** - Multiply row by scalar, e.g. \\(kR_x\rightarrow R_x\\)

$$
A= \left[ {\begin{matrix}
	1 & 2 & 3\\\\
	4 & 5 & 6\\\\
  \end{matrix}} \right]\Longrightarrow 3R_1\rightarrow R_1 \Longrightarrow
  \left[ {\begin{matrix}
	3 & 6 & 9\\\\
	4 & 5 & 6\\\\
  \end{matrix}} \right]
$$

**Type III** - Multiply another row by scalar and add to row, e.g. \\(R_x+kR_y\rightarrow R_x,\ where\ x\neq y\\)

$$
A= \left[ {\begin{matrix}
	1 & 2 & 3\\\\
	4 & 5 & 6\\\\
	7 & 8 & 9\\\\
  \end{matrix}} \right]\Longrightarrow R_1-3R_2\rightarrow R_1 \Longrightarrow
  \left[ {\begin{matrix}
	-11 & -13 & -15\\\\
	4   & 5   & 6  \\\\
	7   & 8   & 9  \\\\
  \end{matrix}} \right]
$$

### Inverse Matrix (again?)

Using row operations we can figure out the inverse of a matrix, here is how

First you create a new matrix by putting our matrix on the left and the identity matrix on the right \\([\begin{array}{c:c}A & In\end{array}]\\)

$$
A= \left[ {\begin{matrix}
	1 & 2 & 3\\\\
	2 & 6 & 4\\\\
	3 & 4 & 5\\\\
  \end{matrix}} \right]\Longrightarrow
  \left[ {\begin{array}{ccc:ccc}
	1 & 2 & 3 & 1 & 0 & 0\\\\
	2 & 6 & 4 & 0 & 1 & 0\\\\
	3 & 4 & 5 & 0 & 0 & 1\\\\
  \end{array}} \right]
$$

Now we keep doing row operations until the identity matrix is on the other side, then \\(A^{-1}\\) will be on the right side \\([\begin{array}{c:c}In & A^{-1}\end{array}]\\), the solutions is rather long so bear with me

$$
R_2-2R_1\rightarrow R_2
\Longrightarrow
  \left[ {\begin{array}{ccc:ccc}
	1 & 2 & 3  & 1  & 0 & 0\\\\
	0 & 2 & -2 & -2 & 1 & 0\\\\
	3 & 4 & 5  & 0  & 0 & 1\\\\
  \end{array}} \right]
$$

$$
R_3-3R_1\rightarrow R_3
\Longrightarrow
  \left[ {\begin{array}{ccc:ccc}
	1 & 2  & 3  & 1  & 0 & 0\\\\
	0 & 2  & -2 & -2 & 1 & 0\\\\
	0 & -2 & -4 & -3 & 0 & 1\\\\
  \end{array}} \right]
$$

$$
\frac{R_2}{2}\rightarrow R_2
\Longrightarrow
  \left[ {\begin{array}{ccc:ccc}
	1 & 2  & 3  & 1  & 0           & 0\\\\
	0 & 1  & -1 & -1 & \frac{1}{2} & 0\\\\
	0 & -2 & -4 & -3 & 0           & 1\\\\
  \end{array}} \right]
$$

$$
R_1-2R_2\rightarrow R_1
\Longrightarrow
  \left[ {\begin{array}{ccc:ccc}
	1 & 0  & 5  & 3  & -1           & 0\\\\
	0 & 1  & -1 & -1 & \frac{1}{2} & 0\\\\
	0 & -2 & -4 & -3 & 0           & 1\\\\
  \end{array}} \right]
$$

$$
R_3+2R_2\rightarrow R_3
\Longrightarrow
  \left[ {\begin{array}{ccc:ccc}
	1 & 0 & 5  & 3  & -1           & 0\\\\
	0 & 1 & -1 & -1 & \frac{1}{2} & 0\\\\
	0 & 0 & -6 & -5 & 1           & 1\\\\
  \end{array}} \right]
$$

We are getting there

$$
-\frac{R_3}{6}\rightarrow R_3
\Longrightarrow
  \left[ {\begin{array}{ccc:ccc}
	1 & 0 & 5  & 3           & -1           & 0           \\\\
	0 & 1 & -1 & -1          & \frac{1}{2}  & 0           \\\\
	0 & 0 & 1  & \frac{5}{6} & -\frac{1}{6} & -\frac{1}{6}\\\\
  \end{array}} \right]
$$

$$
R_1-5R_3\rightarrow R_1
\Longrightarrow
  \left[ {\begin{array}{ccc:ccc}
	1 & 0 & 0  & -\frac{7}{6} & -\frac{1}{6} & \frac{5}{6} \\\\
	0 & 1 & -1 & -1           & \frac{1}{2}  & 0           \\\\
	0 & 0 & 1  & \frac{5}{6}  & -\frac{1}{6} & -\frac{1}{6}\\\\
  \end{array}} \right]
$$

And finally

$$
R_2+R_3\rightarrow R_2
\Longrightarrow
  \left[ {\begin{array}{ccc:ccc}
	1 & 0 & 0 & -\frac{7}{6} & -\frac{1}{6} & \frac{5}{6} \\\\
	0 & 1 & 0 & -\frac{1}{6} & \frac{1}{3}  & -\frac{1}{6}\\\\
	0 & 0 & 1 & \frac{5}{6}  & -\frac{1}{6} & -\frac{1}{6}\\\\
  \end{array}} \right]
$$

And this is our final solution

$$
A= \left[ {\begin{matrix}
	1 & 2 & 3\\\\
	2 & 6 & 4\\\\
	3 & 4 & 5\\\\
  \end{matrix}} \right]\implies
A^{-1}=\left[ {\begin{matrix}
	-\frac{7}{6} & -\frac{1}{6} & \frac{5}{6} \\\\
	-\frac{1}{6} & \frac{1}{3}  & -\frac{1}{6}\\\\
	\frac{5}{6}  & -\frac{1}{6} & -\frac{1}{6}\\\\
  \end{matrix}} \right]
$$

## Determinant

I'm really tired after writing all of this so here is the gist of it

The determinant of a \\(1\times1\\) matrix is itself

For a \\(2\times 2\\) matrix

$$
A= \left[ {\begin{matrix}
	a & b\\\\
	c & d
  \end{matrix}} \right] \implies \det A=ad-bc
$$

For a \\(3\times 3\\)

$$
A= \left[ {\begin{matrix}
	a & b & c\\\\
	d & e & f\\\\
	g & h & i\\\\
  \end{matrix}} \right] \implies \det A=aei+bfg+cdh-ceg-afh-bdi
$$

For larger determinants please refer to Youtube, I'm too tired for thiss
