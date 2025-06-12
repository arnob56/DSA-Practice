#printing 20 fibonacci numbers

prev1=0
prev2=1

print(prev1)
print(prev2)

for i in range(18):  # First two number is already printed and rest of 18 numbers need to be printed out of 20
    new_fibo= prev1+prev2
    print(new_fibo)
    prev1=prev2
    prev2=new_fibo