def solution(arr):
    result=[0,0]
    length=len(arr)
    
    def quad(a,b,l):
        start=arr[a][b]
        for i in range(a,a+l):
            for j in range(b,b+l):
                if arr[i][j]!=start:
                    l=l//2
                    quad(a,b,l)
                    quad(a,b+l,l)
                    quad(a+l,b,l)
                    quad(a+l,b+l,l)
                    return
                
        result[start]+=1
        
    quad(0,0,length)
    
    return result