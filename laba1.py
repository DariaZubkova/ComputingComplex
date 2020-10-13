import numpy as np

def mid(matrix):
    n = len(matrix)
    middle = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            middle[i][j] = (matrix[i][j][0] + matrix[i][j][1]) / 2
    return middle

def rad(matrix):
    n = len(matrix)
    radius = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            radius[i][j] = (matrix[i][j][1] - matrix[i][j][0]) / 2
    return radius

def beckCriterion(matrix):
    middle = mid(matrix)
    radius = rad(matrix)
    inv = np.linalg.inv(middle)
    inv = np.abs(inv)

    A = inv.dot(radius)
    eig = np.abs(np.linalg.eigvals(A))
    rho = np.max(eig)

    if rho < 1:
        res = 'it is non-special matrix'
    else:
        res = 'undefined'

    return res, rho

def diagMaxCriterion(matrix):
    n = len(matrix)
    middle = mid(matrix)
    radius = rad(matrix)
    inv = np.linalg.inv(middle)
    inv = np.abs(inv)
    A = radius.dot(inv)

    diagMax = A[0][0]
    for i in range(1, n):
        if diagMax < A[i][i]:
            diagMax = A[i][i]

    if diagMax >= 1:
        res = 'true, it is special matrix'
    else:
        res = 'undefined'

    return res, diagMax

def createMatrix(size, eps):
    matrix = [[(0, 0) for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i][j] = (0, eps)
            else:
                matrix[i][j] = (1, 1)
    return matrix

def min4(a, b, c, d):
    return min(min(min(a, b), c), d)

def max4(a, b, c, d):
    return max(max(max(a, b), c), d)

def sumIntervals(a_l, a_r):
    return a_l[0] + a_r[0], a_l[1] + a_r[1]

def supIntervals(a_l, a_r):
    return a_l[0] - a_r[1], a_l[1] - a_r[0]

def mulIntervals(a_l, a_r):
    l_low, l_up = a_l[0], a_r[1]
    r_low, r_up = a_l[0], a_r[1]
    return min4(l_low * r_low, l_low * r_up, l_up * r_low, l_up * r_up), \
           max4(l_low * r_low, l_low * r_up, l_up * r_low, l_up * r_up)

def determinant2(matrix):
    return supIntervals(mulIntervals(matrix[0][0], matrix[1][1]), mulIntervals(matrix[0][1], matrix[1][0]))

def determinant3(matrix):
    first = mulIntervals(matrix[0][0], supIntervals(mulIntervals(matrix[1][1], matrix[2][2]), mulIntervals(matrix[1][2], matrix[2][1])))
    second = mulIntervals(matrix[0][1], supIntervals(mulIntervals(matrix[1][0], matrix[2][2]), mulIntervals(matrix[2][0], matrix[1][2])))
    third = mulIntervals(matrix[0][2], supIntervals(mulIntervals(matrix[1][0], matrix[2][1]), mulIntervals(matrix[2][0], matrix[1][1])))
    return sumIntervals(supIntervals(first, second), third)


def determinant4(matrix, eps):
    matrix_l = createMatrix(3, eps)
    first = mulIntervals(matrix[0][0], determinant3(matrix_l))
    matrix_r = [[(0, eps), (0, eps), (0, eps)], [(0, eps), (1, 1), (0, eps)], [(0, eps), (0, eps), (1, 1)]]
    second = mulIntervals(matrix[0][1], determinant3(matrix_r))
    matrix_t = [[(0, eps), (1, 1), (0, eps)], [(0, eps), (0, eps), (0, eps)], [(0, eps), (0, eps), (1, 1)]]
    third = mulIntervals(matrix[0][2], determinant3(matrix_t))
    matrix_s = [[(0, eps), (1, 1), (0, eps)], [(0, eps), (0, eps), (1, 1)], [(0, eps), (0, eps), (0, eps)]]
    forth = mulIntervals(matrix[0][3], determinant3(matrix_s))
    return sumIntervals(supIntervals(first, second), supIntervals(third, forth))


print('First task:')
print('Enter eps: ')
eps = float(input())
matrix = [[(1 - eps, 1 + eps), (1 - eps, 1 + eps)], [(1.1 - eps, 1.1 + eps), (1 - eps, 1 + eps)]]
beckRes, rho = beckCriterion(matrix)
diagRes, diagMax = diagMaxCriterion(matrix)
print('BeckCriterion result:', beckRes, '; rho = ', np.around(rho, decimals=3))
print('DiagMaxCriterion result:', diagRes, '; max in diagonal = ', np.around(diagMax, decimals=3))
det1 = determinant2(matrix)
print('Det: (', np.around(det1[0], decimals=5), ', ', np.around(det1[1], decimals=5), ')')

print('\nRefinement of the assessment: ')
eps = 0
continu = True
while continu:
    matrix = [[(1 - eps, 1 + eps), (1 - eps, 1 + eps)], [(1.1 - eps, 1.1 + eps), (1 - eps, 1 + eps)]]
    det2 = determinant2(matrix)
    if det2[0] * det2[1] < 0:
        print('Det: (', np.around(det2[0], decimals=5), ', ', np.around(det2[1], decimals=5), ')')
        print('Found eps:', np.around(eps, decimals=3))
        continu = False
    eps += 0.001



print('\nSecond tast: ')
print('Enter size: ')
size = int(input())
eps = 0
continu = True
while continu:
    matrix = createMatrix(size, eps)
    if size == 3:
        det3 = determinant3(matrix)
    else:
        det3 = determinant4(matrix, eps)
    if det3[0] * det3[1] <= 0:
        print('Det: (', np.around(det3[0], decimals=5), ', ', np.around(det3[1], decimals=5), ')')
        print('Found eps:', np.around(eps, decimals=3))
        continu = False
    beckRes, rho = beckCriterion(matrix)
    diagRes, diagMax = diagMaxCriterion(matrix)
    if beckRes == 'undefined' and diagRes == 'true, it is special matrix':
        print('Found eps:', np.around(eps, decimals=3))
        continu = False
        print('BeckCriterion result:', beckRes, '; rho = ', np.around(rho, decimals=3))
        print('DiagMaxCriterion result:', diagRes, '; max in diagonal = ', np.around(diagMax, decimals=3))
    eps += 0.01

print('\nRefinement of the assessment: ')
print('size: ', size)
eps = 0
continu = True
while continu:
    matrix = createMatrix(size, eps)
    if size == 3:
        det3 = determinant3(matrix)
    else:
        det3 = determinant4(matrix, eps)
    if det3[0] * det3[1] <= 0:
        print('Det: (', np.around(det3[0], decimals=5), ', ', np.around(det3[1], decimals=5), ')')
        print('Found eps:', np.around(eps, decimals=3))
        continu = False
    eps += 0.001
