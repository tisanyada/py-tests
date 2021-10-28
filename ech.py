import sys
import numpy as np

def fixRowTwo(A) :

    # Sets the sub-diagonal elements of row two to zero
    A[2] = A[2] - A[2,0] * A[0] ## Change this to A[0] instead of A[1]
    A[2] = A[2] - A[2,1] * A[1]

    # Test if diagonal element is not zero.
    if A[2,2] == 0 :
        # Add a lower row to row two.
        A[2] = A[2] + A[3]

        # Sets the sub-diagonal elements to zero again ???
        A[2] = A[2] - A[2,0] * A[0] ## Same as earlier
        A[2] = A[2] - A[2,1] * A[1]

    if A[2,2] == 0 :
        print("S I N G U L A R")
        sys.Exit()

    # Set the diagonal element to one
    A[2] = A[2] / A[2,2]

    return A

def fixRowThree(A) :

    # Sets the sub-diagonal elements of row two to zero
    A[3] = A[3] - A[3,0] * A[0] ## Similar to above, change this to A[0]
    A[3] = A[3] - A[3,1] * A[1] ## Change to A[1]
    A[3] = A[3] - A[3,2] * A[2]    

    # Test if diagonal element is not zero.
    if A[3,3] == 0:
        print("S I N G U L A R")
        sys.Exit()

    # Set the diagonal element to one
    A[3] = A[3] / A[3,3]

    return A

A = np.array([
        [1, 7, 4, 3],
        [0, 1, 2, 3],
        [3, 2, 0, 3],
        [1, 3, 1, 3]
    ], dtype=np.float_)

fixRowTwo(A)
print("")
print("Row Two:")
print(A)

fixRowThree(A)
print("")
print("Row Three:")
print(A)
