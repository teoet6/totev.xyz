import math
import itertools
from tqdm.auto import tqdm
import json

def sign(x):
	if x > 0: return 1
	if x < 0: return -1
	return 0

def ratio(x):
	if isinstance(x, int): return (x, 1)
	if x is None: return None
	p, q = x
	g = math.gcd(p, q) * sign(q)
	return (p//g, q//g)

def add(x, y):
	x = ratio(x)
	y = ratio(y)
	if x is None or y is None: return None

	xp, xq = x
	yp, yq = y

	return ratio((xp * yq + xq * yp, xq * yq))

def sub(x, y):
	x = ratio(x)
	y = ratio(y)
	if x is None or y is None: return None

	xp, xq = x
	yp, yq = y

	return ratio((xp * yq - xq * yp, xq * yq))

def mul(x, y):
	x = ratio(x)
	y = ratio(y)
	if x is None or y is None: return None

	xp, xq = x
	yp, yq = y

	return ratio((xp * yp, xq * yq))

def div(x, y):
	x = ratio(x)
	y = ratio(y)
	if x is None or y is None: return None

	xp, xq = x
	yp, yq = y

	if xq * yp == 0: return None

	return ratio((xp * yq, xq * yp))

def is_ten(x):
	x = ratio(x)
	return x is not None and x[0] == 10 and x[1] == 1

def count_solutions(nums):
	ans = 0

	for a, b, c, d in itertools.permutations(nums):
		for f, g, h in itertools.product((add, sub, mul, div), repeat=3):
			if is_ten(f(g(h(a, b), c), d)): ans += 1
			if is_ten(f(g(a, h(b, c)), d)): ans += 1
			if is_ten(f(g(a, b), h(c, d))): ans += 1
			if is_ten(f(a, g(h(b, c), d))): ans += 1
			if is_ten(f(a, g(b, h(c, d)))): ans += 1

	return ans

def print_solutions(nums):
	for a, b, c, d in itertools.permutations(nums):
		for f, g, h in itertools.product((add, sub, mul, div), repeat=3):
			if is_ten(f(g(h(a, b), c), d)): print(f'({f.__name__}({g.__name__}({h.__name__}({a}, {b}), {c}), {d})')
			if is_ten(f(g(a, h(b, c)), d)): print(f'({f.__name__}({g.__name__}({a}, {h.__name__}({b}, {c})), {d})')
			if is_ten(f(g(a, b), h(c, d))): print(f'({f.__name__}({g.__name__}({a}, {b}), {h.__name__}({c}, {d}))')
			if is_ten(f(a, g(h(b, c), d))): print(f'({f.__name__}({a}, {g.__name__}({h.__name__}({b}, {c}), {d}))')
			if is_ten(f(a, g(b, h(c, d)))): print(f'({f.__name__}({a}, {g.__name__}({b}, {h.__name__}({c}, {d})))')
			

if __name__ == '__main__':
	gen = list(itertools.combinations_with_replacement(range(1, 10), 4))
	data = [(count_solutions(it), it) for it in tqdm(gen)]
	data = [(cnt, it) for cnt, it in data if cnt > 0]
	data = sorted(data, reverse=True)
	data = [''.join(str(jt) for jt in it) for cnt, it in data]
	print(json.dumps(data))

