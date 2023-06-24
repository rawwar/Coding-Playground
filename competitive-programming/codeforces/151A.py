n, k, l, c, d, p, nl, np = list(map(int, input().split()))

drink_toasts = (k*l)//nl
lime_toasts = c * d
salt_toasts = p//np

print( min([drink_toasts,lime_toasts, salt_toasts])//n)