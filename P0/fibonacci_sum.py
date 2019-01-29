def fibonacci_sum(n):
    fibonacci = [0, 1]
    for index in range(2, n):
        fibonacci.append(fibonacci[index-1] + fibonacci[index-2])
    return fibonacci

n = int(input("Enter the number of terms you want to sum: "))
total_sum = 0
for elem in fibonacci_sum(n):
    total_sum += elem
print("Fibonacci series is:", fibonacci_sum(n))
print("The sum of the", n, "terms is:", total_sum)