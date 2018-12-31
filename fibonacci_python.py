def nth_fibonacci(n):
	if n <= 1:
		return n
	else:
		return nth_fibonacci(n-1)+nth_fibonacci(n-2)

def fibonacci_until_n(n):
	i=0
	while (nth_fibonacci(i)<n):
		print(nth_fibonacci(i))
		i+=1
