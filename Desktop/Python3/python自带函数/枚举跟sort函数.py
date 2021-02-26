import numpy as np
# sorted 函数的使用
char_tuple =  ('a','b','c','d','e','f','g','a','b','c','d')
char_set = list(set(char_tuple))
print(char_set)
set_sorted = sorted(char_set)
print(set_sorted)

# 枚举
sorted_enumerate = enumerate(set_sorted)
for i in sorted_enumerate:
    print(i)
enumerate_sorted = {i:ch for i,ch in enumerate(sorted(char_tuple))}
print(enumerate_sorted) 