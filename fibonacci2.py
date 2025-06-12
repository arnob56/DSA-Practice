print(0)
print(1)

count=2

def fibo(prev1,prev2):
    global count
    if count <=19:
        new_fibo=prev1+prev2
        print(new_fibo)
        prev1=prev2
        prev2=new_fibo
        count+=1
        fibo(prev1,prev2)
fibo(0,1)