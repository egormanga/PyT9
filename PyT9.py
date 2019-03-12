#!/usr/bin/python3
# PyT9

class Trie:
	__slots__ = ('verticies')

	def __init__(self, iterable=None):
		self.verticies = [{}] # [*{char: (to, isTerminal)}]
		if (iterable is not None):
			self.update(iterable)

	def __contains__(self, x: str):
		v = int()
		for i in x:
			if (i not in self.verticies[v]): return False
			v = self.verticies[v][i][0]
		return self.verticies[v-1][i][1]

	def add(self, x: str):
		lv, v = (int(),)*2
		for i in x:
			lv = v
			if (i not in self.verticies[v]):
				l = len(self.verticies)
				if (l >= len(self.verticies)): self.verticies.append(dict())
				self.verticies[v][i] = (l, False)
				v = l
			else: v = self.verticies[v][i][0]
		self.verticies[lv][i] = (self.verticies[lv][i][0], True)

	def complete(self, x: str, maxdepth=None):
		v = int()
		t = bool()
		for i in x:
			if (i not in self.verticies[v]): return {}
			v, t = self.verticies[v][i]
		r = {x} if (t) else set()
		def dfs(c, v, depth=int()):
			for i, (v, t) in self.verticies[v].items():
				if (t): r.add(c+i)
				if (not maxdepth or depth < maxdepth): dfs(c+i, v, depth=depth+1)
		dfs(x, v)
		return r

	def update(self, iterable):
		for i in iterable:
			self.add(i)

# TODO: https://en.wikipedia.org/wiki/Radix_tree

# by Sdore, 2019
