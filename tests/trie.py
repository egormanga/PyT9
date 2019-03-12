#!/usr/bin/python3
# PyT9 Trie test

from PyT9 import Trie

t = Trie(['he', 'hi', 'she', 'his', 'hers'])

assert t.verticies == [
	{'h': (1, False), 's': (4, False)},
	{'e': (2, True), 'i': (3, True)},
	{'r': (8, False)},
	{'s': (7, True)},
	{'h': (5, False)},
	{'e': (6, True)},
	{},
	{},
	{'s': (9, True)},
	{},
]

assert 'he' in t
assert 'lol' not in t
assert 'hist' not in t
assert 'hers' in t

assert t.complete('h') == {'hi', 'his', 'he', 'hers'}
assert t.complete('s') == {'she'}
assert t.complete('he') == {'he', 'hers'}
assert t.complete('hi') == {'his', 'hi'}
assert t.complete('i') == {}
assert t.complete('') == {'hi', 'she', 'hers', 'he', 'his'}

print('Trie test ok.')

# by Sdore, 2019
