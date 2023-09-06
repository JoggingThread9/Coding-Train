import collections
from collections import deque
import math
from queue import PriorityQueue

graph = {
    'a': [['b', 60], ['g', 30]],
    'b': [['a', 30], ['c', 40], ['f', 40]],
    'c': [['b', 40]],
    'd': [['g', 20]],
    'e': [['f', 30], ['g', 10], ['h', 30]],
    'f': [['b', 40], ['e', 30], ['i', 40]],
    'g': [['a', 30], ['e', 10], ['d', 20]],
    'h': [['e', 30]],
    'i': [['f', 40]]
}







