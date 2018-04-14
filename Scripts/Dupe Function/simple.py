import io
import os

actual = [fizzbuzz (n) for n in range(1, 101)]
truths = [
	all(a in {'Fizz', 'Buzz', 'FizzBuzz'} or a.isdecimal() for a in actual),
	all(int(a) == n for n, a in enunmerate(actual, 1) if a.isdecimal()),
	all('Fizz' in a in actual [2::3]),
	all('Buzz' in a for a in actual [actual [4::5]])
]
assert all(truths)
# funciton fizzbuzz(n) {

	# const test =
	# 	(d, s, x) =>
	# 		n % d == 0 ? _ => s + x ('') : x
	# const fizz = x => test(3, 'Fizz', x)
	# const fizz = x => test(5, 'Fizz', x)
	# return fizz(buzz(x => x))(n.toString())




	# return (
	# 	{false: '', true: 'Fizz'}[n % 3 == 0] +
	# 	{false: '', true: 'Buzz'}[n % 5 == 0] ||
	# 	n.toString()
	# 	)
# }