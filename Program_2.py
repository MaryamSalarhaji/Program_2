#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
num=list(range(10))
for i in range (10):
    if i>=1:
        current_num=num[i]
        previuous_num=num[i-1]
#exclude index zero, because for index 0, (i-1)=-1 and num[i-1]=9 and is incorrect        
    if i==0:
        current_num=0
        previuous_num=0 
    sum=current_num+previuous_num
    print("Current number", current_num, "Previuos number", previuous_num, "Sum:", sum)
    
    