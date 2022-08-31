l = [0,1,2,3,4,5,6,7,8,9,10]

def iter(x, A):
    #Definerer start og slutt pekere
    start = 0
    slutt = len(A)-1


    while start <= slutt:
        #Finner midt indexn mellom start og slutt
        mid = (start+slutt)//2
        
        if A[mid] == x:
            return True 
        elif A[mid] < x:
            start = mid + 1
        elif A[mid] > x:
            slutt = mid - 1
    return False


print(iter(2, l))
