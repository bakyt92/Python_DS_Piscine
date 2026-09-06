from typing import Any


def callLimit(limit: int):
	""" Limit function. If function is called
	too many times, it does not executes """
	count = 0
	def callLimiter(function):
		def limit_function(*args: Any, **kwds: Any):
			nonlocal count
			if count >= limit:
				print(f"Error {function.__name__} call too many times")
				return
			count += 1
			return function(*args, **kwds)
		return limit_function
	return callLimiter


def main() -> None:
	""" Demonstration example of code """
	@callLimit(3)
	def f():
		print ("f()")

	@callLimit(1)
	def g():
		print ("g()")

	for i in range(3):
		f()
		g()
	return


if __name__ == "__main__":
	main()
