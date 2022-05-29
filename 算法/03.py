# 如果a+b+c=N，且a^2+b^2=c^2(a,b,c为自然数)，如何求出所有a，b，c可能的组合
import time

start_time = time.time()

# 注意是两重循环
for a in range(0, 1001):
    for b in range(0, 1001-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a, b, c: %d, %d, %d" % (a, b, c))

# T(n) = n * n * (1+max(1,0))
#      = n^2



end_time = time.time()
print("elapsed: %f" % (end_time - start_time))
print("complete!")