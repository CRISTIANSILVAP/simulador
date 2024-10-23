import numpy as np

def transitionAmplitude(vector1, vector2):
    nVector1 = np.linalg.norm(vector1)
    vector1 = vector1 / nVector1
    nVector2 = np.linalg.norm(vector2)
    vector2 = vector2 / nVector2
    if len(vector1) != len(vector2):
        return "length error between the two vectors"
    else:
        transitionAmplitude = np.dot(np.conjugate(vector2.T), vector1)
        return transitionAmplitude
    
def calculaMedia(matrix,Ket):
    esHermitania = np.array_equal(matrix,np.conjugate(np.transpose(matrix)))
    
    nMatrix = np.linalg.norm(matrix)
    matrix = matrix/nMatrix

    Ket = np.array([[1],[0]])
    nVector = np.linalg.norm(Ket)
    Ket = Ket/nVector
    if not esHermitania:
        return "La matriz no es hermitania"
    else:
        valorEsperado = np.dot(np.conjugate(matrix.T),Ket)
        valorEsperado = np.dot(np.conjugate(valorEsperado.T),Ket)
        return valorEsperado
        
    
def calculateVariance(matrix, ket):
    isHermitian = np.array_equal(matrix, np.conjugate(np.transpose(matrix)))
    nMatrix = np.linalg.norm(matrix)
    matrix = matrix / nMatrix
    ket = np.array([[1], [0]])
    nVector = np.linalg.norm(ket)
    ket = ket / nVector
    if not isHermitian:
        return "The matrix is not Hermitian"
    else:
        length = len(ket)
        identityMatrix = np.eye(int(length))
        expectedValue = calculaMedia(matrix, ket)
        operator1 = matrix
        operator2 = expectedValue * identityMatrix
        operatorDelta = operator1 - operator2
            
        operator = np.dot(operatorDelta, operatorDelta)
        variance = np.dot(np.conjugate(operator.T), ket)
        variance = np.dot(np.conjugate(variance.T), ket)
        return variance
    
def calculateTransitionOfEigenvectors(matrix, ket):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    probabilities = []
    for rep in range(len(eigenvectors)):
        probability = np.dot(np.conjugate(eigenvectors[rep].T), ket)
        probability = probability ** 2
        probabilities.append(probability)  
    return probabilities, eigenvalues, eigenvectors

def finalState(initialState, matrices):
    numberOfMatrices = len(matrices)
    matrices = map(np.array, matrices) 
    for rep in range(numberOfMatrices):
        initialState = np.dot(initialState, matrices[rep])
        
    return initialState
