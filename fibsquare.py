def calculateSquareSum(n):
	fibo = [0] * (n + 1);
	if (n <= 0):
		return 0;
	fibo[0] = 0;
	fibo[1] = 1;
	
	# Initialize result
	sum = ((fibo[0] * fibo[0]) +
		(fibo[1] * fibo[1]));
	
	# Add remaining terms
	for i in range(2, n + 1):
		fibo[i] = (fibo[i - 1] +
				fibo[i - 2]);
		sum += (fibo[i] * fibo[i]);

	return sum; 

# Driver Code
n = 6; 

print("Sum of squares of Fibonacci numbers is :",
						calculateSquareSum(n)); 
def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n + 2:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
    return fib

def sum_of_squares_vs_product(n):
    fib = fibonacci(n)
    sum_of_squares = sum(x ** 2 for x in fib[:n])
    product = fib[n] * fib[n+1]
    return sum_of_squares, product

n = int(input("Enter the value of n: "))
sum_squares, product = sum_of_squares_vs_product(n)
print(f"Sum of squares of Fibonacci numbers up to the {n}th term: {sum_squares}")
print(f"Product of the {n}th and {n+1}th Fibonacci numbers: {product}")

if sum_squares == product:
    print(f"The equation is satisfied: {sum_squares} = {product}")
else:
    print("The equation is not satisfied.")
