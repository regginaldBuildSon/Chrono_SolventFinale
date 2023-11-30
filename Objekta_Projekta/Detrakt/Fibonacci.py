import time

##a+b=c+d=e

def fibonacci(idx):
    seq=[0,1]
    for i in range(idx):
        seq.append(seq[-1]+seq[-2])
    return seq[-2]

def Fibonacci(idx):
    if idx <= 1:
        return idx
    else:
        return Fibonacci(idx-1)+Fibonacci(idx-2)


print("*****recursion*****")
rec = time.time()
print(Fibonacci(21))
print("speed : " + str(time.time()-rec))

print("*****iteration*****")
it = time.time()
print(fibonacci(21))
print("speed : " + str(time.time()-it))
