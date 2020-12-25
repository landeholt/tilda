# Author: John Landeholt [TA]

class Hash_node:
    def __init__(self, key = None, data = None):
        self.key = key
        self.data = data
    def __repr__(self):
        return f'<hash_node containing {self.data}>'

class Hash_table:
    def __init__(self, size = 100):
        """size dictates the size of the array (bucket)"""
        # YOUR CODE HERE
        pass
    
    def __setitem__(self, key, value):
        """
        usage:
        h = Hash_table()
        h['key'] = 'value'
        """
        # YOUR CODE HERE
        pass
    def __getitem__(self, key):
        """
        usage:
        h = hash_table()
        h['key'] = 'value'
        print(h['key'])
        >> 'value'
        """
        # YOUR CODE HERE
        return None

    def __contains__(self, key):
        """
        usage:
        h = Hash_table()
        if 'key' in h:
            print('"key" exists in h')
        """
        try:
            # YOUR CODE HERE
            return None
        except:
            raise KeyError
    @staticmethod
    def _hash(key):
        """Creates a number from the given key"""
        r = 0
        for char in str(key):
            r = r*32 + ord(char)
        return r

if __name__ == "__main__":
    """Driver code for checking if the implementation is working"""
    h = Hash_table()
    h['key1'] = 'value1'
    h['key2'] = 'value2'

    if 'key1' in h: print(h['key1'])
    if 'key2' in h: print(h['key2'])
    if 'key3' in h: print(h['key3'])