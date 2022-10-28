import functools
import operator

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

'''итератор, который принимает список списков, и возвращает их плоское представление'''

class FlatIterator:
    def __init__(self, list_):
        self.list_ = sum(list_, [])
        self.len = len(self.list_)

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor >= self.len:
            raise StopIteration
        item = self.list_[self.cursor]
        self.cursor += 1
        return item

# проверяем
for item in FlatIterator(nested_list):
    print(item)
print('=' * 80)


'''компрехеншн'''
flat_list = [i for i in FlatIterator(nested_list)]
# проверяем
print(flat_list)
print('=' * 80)

'''генератор, который принимает список списков, и возвращает их плоское представление'''

# вариант с "разглаживанием" списка до итерации
def flat_generator(list_):
    list_ = sum(list_, [])
    for item in list_:
        yield item

# проверяем
for item in  flat_generator(nested_list):
	print(item)
print('=' * 80)

# вариант с "разглаживанием" в процессе итерации
def flat_generator(list_):
    for i in list_:
        for item in i:
            yield item

# проверяем
for item in  flat_generator(nested_list):
	print(item)

print('=' * 80)





