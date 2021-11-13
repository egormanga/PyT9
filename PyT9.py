#!/usr/bin/env python3
# PyT9

import copy

class Trie:
	__slots__ = ('vertices',)

	def __init__(self, iterable=None):
		self.vertices = [{}] # [*{char: (to, isTerminal)}]
		if (iterable is not None): self.update(iterable)

	def __contains__(self, x: str):
		v = int()

		for i in x:
			if (i not in self.vertices[v]): return False
			v = self.vertices[v][i][0]

		return self.vertices[v-1][i][1]

	def add(self, x: str):
		lv, v = (int(),)*2

		for i in x:
			lv = v

			if (i not in self.vertices[v]):
				l = len(self.vertices)
				if (l >= len(self.vertices)): self.vertices.append(dict())
				self.vertices[v][i] = (l, False)
				v = l

			else: v = self.vertices[v][i][0]

		self.vertices[lv][i] = (self.vertices[lv][i][0], True)

	def complete(self, x: str, *, maxdepth=None):
		v = int()
		t = bool()

		for i in x:
			if (i not in self.vertices[v]): return {}
			v, t = self.vertices[v][i]

		r = {x} if (t) else set()

		def dfs(c, v, *, depth=int()):
			for i, (v, t) in self.vertices[v].items():
				if (t): r.add(c+i)
				if (not maxdepth or depth < maxdepth): dfs(c+i, v, depth=depth+1)

		dfs(x, v)

		return r

	def update(self, iterable):
		for i in iterable:
			self.add(i)

	def copy(self):
		r = Trie()
		r.vertices = copy.deepcopy(self.vertices)
		return r

# TODO: https://en.wikipedia.org/wiki/Radix_tree

# by Sdore, 2021
