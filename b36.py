import string
import collections as ct
special_chars = string.punctuation
sum(v for k, v in ct.Counter(text).items() if k in special_chars)
