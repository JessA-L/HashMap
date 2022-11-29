# Name: Jessica Allman-LaPorte
# OSU Email: allmanlj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6 - HashMap
# Due Date: 12/2/22
# Description: An implementation of a HashMap using Separate Chaining.


from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2, SLNode)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        TODO: Write this implementation
        This method updates the key/value pair in the hash map. If the given key already exists in
        the hash map, its associated value must be replaced with the new value. If the given key is
        not in the hash map, a new key/value pair must be added.
        """

        if self.table_load() >= 1:
            self.resize_table(self._capacity * 2)

        # Use hash function to determine "bucket"
        bucket = self._hash_function(key) % self._capacity
        bucket_ll = self._buckets[bucket]

        # insert node if bucket is empty
        if bucket_ll._head is None:
            bucket_ll.insert(key, value)
            self._size += 1
            return

        # put node in bucket in sorted order
        node = bucket_ll._head
        next_node = node.next

        # find correct spot to insert
        while next_node and key > next_node.key:
            node = next_node
            next_node = next_node.next

        # handle duplicate keys
        if key == node.key:
            node.value = value
            return

        new_node = SLNode(key, value)

        # insert new_node:
        node.next = new_node
        # if new_node is not the tail:
        if next_node:
            new_node.next = next_node
            # handle duplicate keys
            if new_node.key == next_node.key:
                new_node.next = next_node.next
                return
        # if new_node is tail
        else:
            new_node.next = None

        self._size += 1

    def empty_buckets(self) -> int:
        """
        TODO: Write this implementation
        This method returns the number of empty buckets in the hash table.
        """
        empty_buckets_count = 0
        for bucket in range(0, self._buckets.length()):
            if not self._buckets[bucket]._head:
                empty_buckets_count += 1

        return empty_buckets_count

    def table_load(self) -> float:
        """
        This method returns the current hash table load factor.
        """
        return self._size / self._capacity

    def clear(self) -> None:
        """
        TODO: Write this implementation
        This method clears the contents of the hash map. It does not change the underlying hash
        table capacity.
        """
        pass

    def resize_table(self, new_capacity: int) -> None:
        """
        TODO: Write this implementation
        This method changes the capacity of the internal hash table. All existing key/value pairs
        must remain in the new hash map, and all hash table links must be rehashed.
        """
        # First check that new_capacity is not less than 1; if so, the method does nothing.
        if new_capacity < 1:
            return
        # If new_capacity is 1 or more, make sure it is a prime number. If not, change it to the next
        # highest prime number.
        # print(new_capacity)
        if not self._is_prime(new_capacity):
            new_capacity = self._next_prime(new_capacity)
        # print(new_capacity)

        add_num_of_buckets = new_capacity - self._capacity

        # print(type(self._buckets))
        for buckets in range(add_num_of_buckets):
            self._buckets.append(LinkedList())

        self._capacity = new_capacity

    # def _resize_da(self, new_capacity: int) -> None:
    #     """
    #     Method that changes the capacity of the underlying storage
    #     for the elements in the dynamic array. It does not change the values
    #     or the order of any elements currently stored in the array.
    #     """
    #     # Check for positive integers or whether new_capacity <= _size:
    #     if new_capacity <= 0 or new_capacity < self._size:
    #         return
    #
    #     _new_data = StaticArray(new_capacity)
    #
    #     # copy data from _data to _new_data
    #     for index in range(0, self._size):
    #         _new_data[index] = self._data[index]
    #
    #     # _new_data replaces original _data array
    #     self._data = _new_data
    #     self._capacity = new_capacity

    def get(self, key: str):
        """
        TODO: Write this implementation
        This method returns the value associated with the given key. If the key is not in the hash
        map, the method returns None.
        """
        pass

    def contains_key(self, key: str) -> bool:
        """
        TODO: Write this implementation
        This method returns True if the given key is in the hash map, otherwise it returns False. An
        empty hash map does not contain any keys.
        """
        pass

    def remove(self, key: str) -> None:
        """
        TODO: Write this implementation
        This method removes the given key and its associated value from the hash map. If the key
        is not in the hash map, the method does nothing (no exception needs to be raised).
        """
        pass

    def get_keys_and_values(self) -> DynamicArray:
        """
        TODO: Write this implementation
        This method returns a dynamic array where each index contains a tuple of a key/value pair
        stored in the hash map. The order of the keys in the dynamic array does not matter.
        """
        pass


def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    TODO: Write this implementation
    """
    # if you'd like to use a hash map,
    # use this instance of your Separate Chaining HashMap
    map = HashMap()


# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":
    #
    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    # print("\nPDF - put example 3")
    # print("-------------------")
    # hash_function_3 = lambda a : a % 7
    # m = HashMap(7, hash_function_3)
    # m.put(0, "zero")
    # print(m)
    # m.put(7, 7)
    # print(m)
    # m.put(21, 21)
    # print(m)
    # m.put(14, "fourteen")
    # print(m)
    # m.put(49, "fortynine")
    # print(m)
    # m.put(28, 28)
    # print(m)
    # m.put(14, 14)
    # print(m)
    # m.put(49, 49)
    # print(m)
    # m.put(0, 0)
    # print(m)

    # print("\nPDF - put example 4")
    # print("-------------------")
    # m = HashMap(53, hash_function_1)
    # m.put("Jen", "Wife")
    # m.put("Gregg", "Dog")
    # m.put("Gregl", "Same bucket")
    # m.put("Jei", "Same bucket")
    # # print(m)
    # m.put("Gregg", "Dumb")
    # print(m)

    # print("\nPDF - put example 5")
    # print("-------------------")
    # m = HashMap(53, hash_function_1)
    # for i in range(150):
    #     m.put('str' + str(i), i * 100)
    #     # if i % 25 == 24:
    #     #     print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    # print(m)

    # print("\nPDF - empty_buckets example 1")
    # print("-----------------------------")
    # m = HashMap(101, hash_function_1)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())
    # m.put('key1', 10)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())
    # m.put('key2', 20)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())
    # m.put('key1', 30)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())
    # m.put('key4', 40)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())
    #
    # print("\nPDF - empty_buckets example 2")
    # print("-----------------------------")
    # m = HashMap(53, hash_function_1)
    # for i in range(150):
    #     m.put('key' + str(i), i * 100)
    #     if i % 30 == 0:
    #         print(m.empty_buckets(), m.get_size(), m.get_capacity())

    # print("\nPDF - empty_buckets example 3")
    # print("-----------------------------")
    # m = HashMap(53, hash_function_1)
    # print(m.empty_buckets())
    #
    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

    # print("\nPDF - clear example 1")
    # print("---------------------")
    # m = HashMap(101, hash_function_1)
    # print(m.get_size(), m.get_capacity())
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key1', 30)
    # print(m.get_size(), m.get_capacity())
    # m.clear()
    # print(m.get_size(), m.get_capacity())
    #
    # print("\nPDF - clear example 2")
    # print("---------------------")
    # m = HashMap(53, hash_function_1)
    # print(m.get_size(), m.get_capacity())
    # m.put('key1', 10)
    # print(m.get_size(), m.get_capacity())
    # m.put('key2', 20)
    # print(m.get_size(), m.get_capacity())
    # m.resize_table(100)
    # print(m.get_size(), m.get_capacity())
    # m.clear()
    # print(m.get_size(), m.get_capacity())
    #
    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(23, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        # for key in keys:
        #     # all inserted keys must be present
        #     result &= m.contains_key(str(key))
        #     # NOT inserted keys must be absent
        #     result &= not m.contains_key(str(key + 1))
        # print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    # print("\nPDF - get example 1")
    # print("-------------------")
    # m = HashMap(31, hash_function_1)
    # print(m.get('key'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    #
    # print("\nPDF - get example 2")
    # print("-------------------")
    # m = HashMap(151, hash_function_2)
    # for i in range(200, 300, 7):
    #     m.put(str(i), i * 10)
    # print(m.get_size(), m.get_capacity())
    # for i in range(200, 300, 21):
    #     print(i, m.get(str(i)), m.get(str(i)) == i * 10)
    #     print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)
    #
    # print("\nPDF - contains_key example 1")
    # print("----------------------------")
    # m = HashMap(53, hash_function_1)
    # print(m.contains_key('key1'))
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key3', 30)
    # print(m.contains_key('key1'))
    # print(m.contains_key('key4'))
    # print(m.contains_key('key2'))
    # print(m.contains_key('key3'))
    # m.remove('key3')
    # print(m.contains_key('key3'))
    #
    # print("\nPDF - contains_key example 2")
    # print("----------------------------")
    # m = HashMap(79, hash_function_2)
    # keys = [i for i in range(1, 1000, 20)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.get_size(), m.get_capacity())
    # result = True
    # for key in keys:
    #     # all inserted keys must be present
    #     result &= m.contains_key(str(key))
    #     # NOT inserted keys must be absent
    #     result &= not m.contains_key(str(key + 1))
    # print(result)
    #
    # print("\nPDF - remove example 1")
    # print("----------------------")
    # m = HashMap(53, hash_function_1)
    # print(m.get('key1'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    # m.remove('key1')
    # print(m.get('key1'))
    # m.remove('key4')
    #
    # print("\nPDF - get_keys_and_values example 1")
    # print("------------------------")
    # m = HashMap(11, hash_function_2)
    # for i in range(1, 6):
    #     m.put(str(i), str(i * 10))
    # print(m.get_keys_and_values())
    #
    # m.put('20', '200')
    # m.remove('1')
    # m.resize_table(2)
    # print(m.get_keys_and_values())
    #
    # print("\nPDF - find_mode example 1")
    # print("-----------------------------")
    # da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    # mode, frequency = find_mode(da)
    # print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")
    #
    # print("\nPDF - find_mode example 2")
    # print("-----------------------------")
    # test_cases = (
    #     ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
    #     ["one", "two", "three", "four", "five"],
    #     ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    # )
    #
    # for case in test_cases:
    #     da = DynamicArray(case)
    #     mode, frequency = find_mode(da)
    #     print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")
