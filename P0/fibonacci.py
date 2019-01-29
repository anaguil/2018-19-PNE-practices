n= 13
fibonacci = [0, 1]
for index in range(2,n):
    fibonacci.append(fibonacci[index-1] + fibonacci[index-2])


print("The first", n ,"terms of the fibonacci series are:", fibonacci)
