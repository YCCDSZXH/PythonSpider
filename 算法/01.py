import time

start_time = time.time()
for a in range(0,1001):
    for b in range(0,1001):
        for c in range(0,1001):
            if a+b+c == 1000 and a**2 + b**2 == c**2:
                print("a,b,c:%d,%d,%d"%(a,b,c))

end_time = time.time()
print("times:%d"%(end_time-start_time))
print("end")

# T = 1000*1000*1000*2
# T = 2000*2000*2000*2
# T = N*N*N*2
# T(n) = n^3 * 2
# T(n) = k*g(n)
# g(n) = n^3