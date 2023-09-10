#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
def multiplication_or_sum(number_1, number_2):
    product=number_1*number_2
    sum=number_1+number_2
    if product<=1000:
        return product
    else:
        return sum

try:
    number_1=int(input("Please enter a number:"))
    number_2=int(input("Please enter a number:"))
    result=multiplication_or_sum(number_1, number_2)
    print("The result is:", result)
except:
    print("OOps,enter a valid number")
    


        