import math as __math
import random as __random
from functools import partial as __partial
from typing import Self as __Self
from copy import deepcopy as __deepcopy

class Collection(dict):
    def __init__(self, *data):
        super().__init__()
        if data:
            for chunk in data:
                key = list(chunk)[0]
                value = chunk[key]
                self.set(key, value)

    # Obtains the value of the given key if it exists, otherwise sets and returns the value provided by the default value generator.
    def ensure(self, key, default_value_generator = None) -> str|int|list|dict|None:
        if self.has(key): return self.get(key)
        if default_value_generator:
            default_value = self.__run(default_value_generator, key)
            self.set(key, default_value)
            return default_value

    # Checks if the element exist in the collection.
    def has(self, key) -> bool:
        if self.get(key): return True
        return False

    # Checks if all of the elements exist in the collection.
    def has_all(self, *keys: []) -> bool:
        for k in keys:
            if not self.has(k): return False
        return True

    # Checks if any of the elements exist in the collection.
    def has_any(self, *keys: []) -> bool:
        for k in keys:
            if self.has(k): return True
        return False

    # Identical to [Array.at()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/at).
    # Returns the item at a given index, allowing for positive and negative integers.
    # Negative integers count back from the last item in the collection.
    def at(self, index: int) -> str|int|list|dict|None:
        index = __math.floor(index)
        arr = [*self.values()]
        return arr[index]

    # Identical to [Array.at()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/at).
    # Returns the key at a given index, allowing for positive and negative integers.
    # Negative integers count back from the last item in the collection.
    def key_at(self, index: int) -> str|int|list|dict|None:
        index = __math.floor(index)
        arr = [*self.keys()]
        return arr[index]

    # Obtains unique random value(s) from this collection.
    def random(self, amount = None) -> str|int|list|dict|None:
        arr = [*self.values()]
        if not amount or not isinstance(amount, int) or amount <= 0: return arr[__random.randint(0,len(arr)-1)]
        if not len(arr): return []
        result = []
        limit = min(len(arr), amount)
        while len(result) < limit:
            element = arr[__random.randint(0,len(arr)-1)]
            arr.remove(element)
            result.append(element)
        return result

    # Obtains unique random key(s) from this collection.
    def random_key(self, amount = None) -> str|list|None:
        arr = [*self.keys()]
        if not amount or not isinstance(amount, int) or amount <= 0: return arr[__random.randint(0,len(arr)-1)]
        if not len(arr): return []
        result = []
        limit = min(len(arr), amount)
        while len(result) < limit:
            element = arr[__random.randint(0,len(arr)-1)]
            arr.remove(element)
            result.append(element)
        return result

    # Identical to [Array.reverse()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse)
    # but returns a Collection instead of an Array.
    def reverse(self, silent = False) -> __Self:
        items = [*self.items()]
        items.reverse()
        if silent:
            result = self.clone()
            for [key, value] in items: result.set(key, value)
        else:
            self.clear()
            for [key, value] in items: self.set(key, value)
            result = self
        return result

    # Searches for a single item where the given function returns a truthy value. This behaves like
    # [Array.find()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find).
    # <warn>All collections used in Discord.js are mapped using their `id` property, and if you want to find by id you
    # should use the `get` method. See
    # [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/get) for details.</warn>
    #
    # @example
    # collection.find(lambda user: user.username == 'Bob');
    def find(self, fn, self_arg = None) -> str|int|list|dict|None:
        if self_arg: fn = __partial(fn, self_arg)
        for key in self:
            val = self.get(key)
            if bool(fn(val, key, self)): return val
        return None

    # Searches for the key of a single item where the given function returns a truthy value. This behaves like
    # [Array.findIndex()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex),
    # but returns the key rather than the positional index.
    #
    # @example
    # collection.find_key(lambda user: user.username == 'Bob');
    def find_key(self, fn, self_arg = None) -> str|int|list|dict|None:
        if self_arg: fn = __partial(fn, self_arg)
        for key in self:
            if bool(fn(self[key], key, self)): return key
        return None

    # Removes items that satisfy the provided filter function.
    def sweep(self, fn, self_arg = None) -> int:
        if self_arg: fn = __partial(fn, self_arg)
        previous_size = len(self)
        results = self.clone()
        for key in self:
            val = self.get(key)
            if not bool(fn(val, key, self)):
                results.set(key, val)
        self = results
        return previous_size - len(self)

    # Identical to
    # [Array.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter),
    # but returns a Collection instead of an Array.
    #
    # @example
    # collection.filter(lambda user, *_: user.language == 'en');
    def filter(self, fn, self_arg = None) -> __Self:
        if self_arg: fn = __partial(fn, self_arg)
        results = self.clone()
        for key in self:
            val = self.get(key)
            if bool(fn(val, key, self)): results.set(key, val)
        return results

    # Partitions the collection into two collections where the first collection
    # contains the items that passed and the second contains the items that failed.
    #
    # @example
    # [big, small] = collection.partition(lambda: guild, *_: guild.member_count > 10)
    def partition(self, fn, self_arg = None) -> [__Self]:
        if self_arg: fn = __partial(fn, self_arg)
        results = [self.clone(), self.clone()]
        for key in self:
            val = self.get(key)
            if fn(val, key, self):
                results[0].set(key, val)
            else:
                results[1].set(key, val)
        return results

    # Maps each item into a Collection, then joins the results into a single Collection. Identical in behavior to
    # [Array.flatMap()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap).
    #
    # @example
    # collection.flat_map(lambda guild, *_: guild.members.cache)
    def flat_map(self, fn, self_arg = None) -> __Self:
        collections = []
        for value in self.map(fn, self_arg):
            collections.append(self.clone().set(str(value)))
        return self.clone().concat(*collections)

    # Maps each item to another value into an array. Identical in behavior to
    # [Array.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map).
    #
    # @example
    # collection.map(lambda user, *_: user.id)
    def map(self, fn, self_arg = None) -> list[str|int|list|dict]:
        if self_arg: __partial(fn, self_arg)
        iterable = self.items().mapping
        result = []
        for key in iterable:
            result.append(fn(iterable[key], key, self))
        return result

    # Maps each item to another value into a collection. Identical in behavior to
    # [Array.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map).
    #
    # @example
    # collection.map_values(lambda user, *_: user.id)
    def map_values(self, fn, self_arg = None) -> __Self:
        if self_arg: __partial(fn, self_arg)
        coll = self.clone()
        for key in self:
            coll.set(key, fn(self[key], key, self))

    # Checks if there exists an item that passes a test. Identical in behavior to
    # [Array.some()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some).
    #
    # @example
    # collection.some(lambda user, *_: user.language == 'en')
    def some(self, fn, self_arg = None) -> bool:
        if self_arg: __partial(fn, self_arg)
        for key in self:
            if bool(fn(self[key], key, self)): return True
        return False

    # Checks if all items passes a test. Identical in behavior to
    # [Array.every()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every).
    #
    # @example
    # collection.every(lambda user: user.language != 'en')
    def every(self, fn, self_arg = None) -> bool:
        if self_arg: __partial(fn, self_arg)
        for key in self:
            if not bool(fn(self[key], key, self)): return False
        return True

    # Applies a function to produce a single value. Identical in behavior to
    # [Array.reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce).
    #
    # @example
    # collection.reduce(lambda acc, guild, *_: acc + guild.member_count(), 0)
    def reduce(self, fn, initial_value = None):
        accumulator = None
        if initial_value or isinstance(initial_value, int):
            accumulator = initial_value
            for key in self: accumulator = fn(accumulator, self[key], key, self)
            return accumulator
        first = True
        for key in self:
            if first:
                accumulator = self[key]
                first = False
                continue
            accumulator = fn(accumulator, self[key], key, self)

        # No items iterated.
        if first:
            return print(TypeError('Reduce of empty collection with no initial value'))

        return accumulator

    # Identical to
    # [Map.forEach()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/forEach),
    # but returns the collection instead of undefined.
    #
    # @example
    # (collection
    #   .each(lambda user, *_: print(user.id))
    #   .filter(lambda user, *_: user.language == 'en')
    #   .each(lambda user, *_: print(user.id)))
    def each(self, fn) -> __Self:
        for key in self:
            fn(self[key], key, self)
        return self

    # Runs a function on the collection and returns the collection.
    #
    # @example
    # (collection
    #   .tap(lambda coll: print(len(coll)))
    #   .filter(lambda user, *_: user.language == 'en')
    #   .tap(lambda coll: print(len(coll))))
    def tap(self, fn, self_arg = None) -> __Self:
        if self_arg: fn = __partial(fn, self_arg)
        fn(self)
        return self

    # Creates an identical shallow copy of this collection.
    #
    # @example
    # new_coll = coll.clone()
    def clone(self, clear = True):
        copy = __deepcopy(self)
        if clear: copy.clear()
        return copy

    # Combines this collection with others into a new collection.
    #
    # @example
    # new_coll = coll.concat(some_coll, another_coll, oh_boy_a_coll)
    def concat(self, *collections: __Self) -> __Self:
        new_coll = self.clone(False)
        for coll in collections:
            for key in coll: new_coll.set(key, coll[key])
        return new_coll

    # Checks if this collection shares identical items with another.
    # This is different to checking for equality using equal-signs, because
    # the collections may be different objects, but contain the same data.
    def equals(self, collection: __Self) -> bool:
        if self == collection: return True
        if len(self) != len(collection): return False
        for key in self:
            if not collection.has(key) or self[key] != collection.get(key):
                return False
        return True

    # Sets the value of the key in self.
    def set(self, key, val = None) -> __Self:
        self[str(key)] = val
        return self

    # The sort method sorts the items of a collection in place and returns it.
    # The default sort order is according to string Unicode code points.
    #
    # @example
    # collection.sort(lambda user, *_: user.created_timestamp)
    #
    # @example
    # collection.sort(lambda user, *_: user.created_timestamp and user.language)
    def sort(self, compare_function):
        items = [*self.items()]
        items.sort(key = lambda item: compare_function(item[1], item[0]))

        # Perform clean-up
        self.clear()

        # Set the new items
        for key in items:
            self.set(key[0], key[1])
        return self

    # The intersect method returns a new structure containing items where the keys are present in both original structures.
    def intersect(self, other: __Self) -> __Self:
        coll = self.clone()
        for key in other:
            if self.has(key): coll.set(key, other[key])
        return coll

    # The difference method returns a new structure containing items where the key is present in one of the original structures but not the other.
    def difference(self, other: __Self) -> __Self:
        coll = self.clone()
        for key in other:
            if not self.has(key): coll.set(key, other[key])
        for key in self:
            if not other.has(key): coll.set(key, self[key])
        return coll

    # The sorted method sorts the items of a collection and returns it.
    # The default sort order is according to string Unicode code points.
    #
    # @example
    # collection.sorted(lambda user, *_: user.created_timestamp)
    #
    # @example
    # collection.sorted(lambda user, *_: user.created_timestamp and user.language)
    def sorted(self, compare_function):
        return self.clone(False).sort(compare_function)

    def to_json(self):
        return [*self.values()]

    def default_sort(self, first_value: int, second_value: int) -> int:
        return int(first_value > second_value) | int(first_value == second_value) - 1

    def __run(self, fn, value, key = None):
        if key:
            try: return fn(value, key, self)
            except TypeError: pass
        try: return fn(value, self)
        except TypeError: return fn(value)
