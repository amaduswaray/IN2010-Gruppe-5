l = [0,1,2,3,4,5,6,7,8,9,10]


def rek(x, A):
    #Definerer pekere
    start = 0
    slutt = len(A)-1
    mid = (start+slutt)//2

    #Basissteg
    if A[mid] == x:
        return True
    
    #Slicer liste fra mid til slutt, når A[mid] er mindre enn x
    if A[mid] < x:
        return rek(x, A[mid+1:slutt])
    
    #Slicer liste fra start til mid, når A[mid] er stærre enn x
    if A[mid] > x:
        return rek(x, A[start:mid-1])

    return False
