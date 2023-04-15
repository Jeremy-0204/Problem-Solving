H,M = map(int,input().split())
H,M = (H,M-45) if M-45>=0 else (23,M+15) if H==0 else (H-1,M+15)
print(H, M)