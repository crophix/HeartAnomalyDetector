import math

def train(trainFile):
    """Use the given file name to train the detector.
    
    This returns 2 lists.  One contains the count of normal and abnormal
    instances.  The other contains the count of each feature in an instance."""
    file = open(trainFile, 'r')
    F = [[0]*22 for i in range(2)]
    N = [0,0]
    for line in file: 
        features = line.split(',')
        cl = int(features[0])
        N[cl] = N[cl] + 1
        for f in range(22):
            if int(features[f+1]) == 1:
                F[cl][f] = F[cl][f] + 1
    return N, F

def test(testFile, N, F):
    """Use the given file name to test the detector.
    
    This returns 2 lists with 2 values.  The first is the number of correctly 
    identified abnormal or normal instances.  The second is the total number
    of abnormal or abnormal instances."""
    file = open(testFile, 'r')
    A = [0,0]
    B = [0,0]    
    for line in file:
        features = line.split(',')
        cl = int(features[0])
        B[cl] = B[cl] + 1
        c = []
        for f in range(22):
            c.append(int(features[f+1]))
        if classify(c,N,F) == cl:
            A[cl] = A[cl] + 1
    return A, B
        
def classify(c, N, F):
    """Determines whether the data is normal(1) or abnormal(0).
    
    Returns either a one or a zero."""
    L = []
    for i in range(2):
        L.append(math.log(N[i]+0.5) - math.log(N[0]+N[1]+0.5))
        for j in range(22):
            s = F[i][j]
            if c[j] == 0:
                s = N[i] - s
            L[i] = L[i] + math.log(s+0.5) - math.log(N[i]+0.5)
    if L[1] > L[0]:
        return 1
    return 0
	
def formatPrint(fTrain, fTest, name):
	"""Runs the training and test sets for a specified file"""
	N, F = train(fTrain)
	A, B = test(fTest, N, F)
	print "{3} {0}/{1}({2})".format(A[0] + A[1], B[0] + B[1], round((A[0] + A[1])/(1.0 * B[0] + B[1]),2), name),
	print "{0}/{1}({2})".format(A[0], B[0], round(A[0] / (1.0* B[0]), 2)),
	print "{0}/{1}({2})".format(A[1], B[1], round(A[1] / (1.0* B[1]), 2))
	
formatPrint("heart-data\spect-orig.train.csv", "heart-data\spect-orig.test.csv", "orig")
formatPrint("heart-data\spect-itg.train.csv", "heart-data\spect-itg.test.csv", "itg")
formatPrint("heart-data\spect-resplit.train.csv", "heart-data\spect-resplit.test.csv", "resplit")
