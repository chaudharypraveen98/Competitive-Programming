# Here is my Python implementation of the hash table data structure.
class Hashtable:
    # Assumption: table_length is a prime number (for example, 5, 701, or 30011)
    def __init__(self, table_length):
        self.table = [None] * table_length
        self.table_length = table_length

    ## An internal search function.
    # If it finds the given key in the table, it will return (True, index)
    # If not, it will return (False, the index where it would be inserted)
    # If the table is full, it will return (False, -1)
    # If test_mode is true, it will also add a third return value that shows
    # the number of elements that have been checked (in the case where
    # the key is not found and the table is not full).
    # Assumption: key is a string.
    def _search(self, key, test_mode=False):
        hash1 = hash(key)
        m = self.table_length
        initial_i = hash1 % m  # initial_i's range: [0, m - 1] (inclusive)

        count = 1  # the number of elements that have been checked - only used when test_mode = True.
        if self.table[initial_i] is None:
            if test_mode:
                return False, initial_i, count
            return False, initial_i
        elif self.table[initial_i][0] == key:
            return True, initial_i

        ## We have a collision!
        # We're going to deal with it with double-hashing.
        # First, create a new hashed value by slightly modifying the input key.
        hash2 = hash(key + 'd')
        # hash2 = hash1 # I tried this method and it worked as well as the above method.
        # hash2 = 0 # This would be linear probing. It did NOT perform as well as the above method.

        # Our constraint here: 1 <= c < m
        # Note that hash2 % (m - 1) produces a number in the range [0, m - 2] inclusive
        c = hash2 % (m - 1) + 1
        i = (initial_i + c) % m

        while i != initial_i:
            count += 1
            if self.table[i] is None:
                if test_mode:
                    return False, i, count
                return False, i
            elif self.table[i][0] == key:
                return True, i
            i = (i + c) % m
        return False, -1  # The table is full.

    ## Inserts a key value pair. If the key exists, it updates the value.
    # If it doesn't exit, it inserts it.
    # If the table is full, it returns without doing anything.
    # Assumption: key is a string.
    # Returns: nothing.
    def insert(self, key, value):
        result = self._search(key)

        if result[1] == -1:
            return  # The table is full.

        # If the key already exists, update the value.
        if result[0]:
            i = result[1]
            self.table[i][1] = value
            return

        # At this point, we'll know that the given key doesn't exist
        # in the table yet, and that result[1] is the index
        # where the new key-value pair should be inserted.
        i = result[1]
        self.table[i] = [key, value]

    ## Returns the value if the key is found.
    # If not, it will return False.
    # Assumption: key is a string.
    def search(self, key):
        result = self._search(key)
        if result[1] == -1:
            return False  # The table is full.

        if not result[0]:
            return False

        i = result[1]
        return self.table[i][1]

    ## I haven't implemented this yet.
    # To implement this one with open-addressing (double-hashing),
    # you should replace the deleted entry with a dummy value instead of deleting it.
    def delete(key):
        pass


## The following is for testing the Hashtable class.
if __name__ == "__main__":
    ht = Hashtable(5)
    ht.insert('key1', 9)
    ht.insert('key2', 2)
    ht.insert('key3', 10)
    ht.insert('key4', 100)
    assert not ht.search('key5')  # Since this key doesn't exist yet, it should return False.
    ht.insert('key5', 10)

    assert ht.search('key1') == 9
    assert ht.search('key2') == 2
    assert ht.search('key3') == 10
    assert ht.search('key4') == 100
    assert ht.search('key5') == 10
    assert not ht.search('key6')  # Since this key doesn't exist, it should return False.

    # You should be able to update existing values, too.
    ht.insert('key3', -1)
    ht.insert('key5', 42)
    assert ht.search('key3') == -1
    assert ht.search('key5') == 42

    ## The following part is for checking the number of
    # elements being checked for un unsuccessful search.
    ht2 = Hashtable(30011)
    for i in range(1, 20004):  # We're going to fill in about two thirds of the table.
        ht2.insert('key' + str(i), 1)

    # Try searching for a bunch of new keys.
    # Then, find the average number of elements that were checked.
    total = 0
    num_trials = 10 ** 5
    max_num = 0

    for i in range(0, num_trials):
        num_checked = ht2._search('new_key_' + str(i), test_mode=True)[2]
        total += num_checked
        if num_checked > max_num:
            max_num = num_checked

    average = total / num_trials
    print('Average number of elements checked:', average)
    print('Max number of elements checked:', max_num)