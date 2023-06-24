k, n, w  = input().split()
k, n, w = int(k), int(n), int(w)
 
print(max(0,int(k*0.5*w*(w+1) - n)))