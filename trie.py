'''
26th february 2019 tuesday
trie implentation clean
'''
class Node:
    def __init__(self, val=None, r_base=26):
        self.val = val
        self.next = [None for i in range(r_base)]

class Trie:
    def __init__(self, r_base=26):
        self.r_base = r_base
        self.root = None

    def _to_index(self, x):
        return ord(x) - ord('a')
    
    def _to_char(self, i):
        return chr(i + ord('a'))

    def put(self, key, val):
        self.root = self.put_util(self.root, key, val, 0)
    
    def put_util(self, x, key, val, d):
        if x is None:
            x = Node()
        
        # base case
        if d == len(key):
            x.val = val
            return x
        
        i = self._to_index(key[d])
        x.next[i] = self.put_util(x.next[i], key, val, d + 1)
        return x

    def get_value(self, key):
        x = self.get_branch(self.root, key, 0)
        if x is None:
            return None
        return x.val

    def get_branch(self, x, key, d):
        if x is None:
            return None
        if d == len(key):
            return x
        
        i = self._to_index(key[d])
        return self.get_branch(x.next[i], key, d + 1)

    def inorder(self):
        head = self.root
        self.inorder_util(head)

    def inorder_util(self, x):
        for i in range(self.r_base):
            if x.next[i] is not None:
                print(self._to_char(i))
                self.inorder_util(x.next[i])
                
    def keys(self):
        q = self.collect(self.root, "", [])
        return q

    '''
    Better version of starts_with_prefix
    '''
    def collect(self, x, prefix, q):
        # x could've been None for branches regrardless of the following omission
        if x is None:
            return None

        if x.val is not None:
            q.append(prefix)

        for i in range(self.r_base):
            # removed the following line, need to check if x is None
            # if x.next[i] is not None:
            self.collect(x.next[i], prefix + self._to_char(i), q)
        return q
    
    '''
    Absolute genius!!!
    '''
    def keys_with_prefix(self, prefix):        
        branch = self.get_branch(self.root, prefix, 0)
        return self.collect(branch, prefix, [])

    def longest_prefix_of(self, query):
        # lim is the limiting variable for the query
        lim = self.search(self.root, query, 0, 0)
        return query[:lim + 1]

    def search(self, x, query, d, lim):
        if x is None:
            return lim

        if x.val is not None:
            lim = d

        if d == len(query):
            return lim

        i = self._to_index(query[d])
        return self.search(x.next[i], query, d + 1, lim)

def main():
    passage = 'she sells sea shells by the'
    wordlist = passage.split(' ')

    tr = Trie()
    for i in range(len(wordlist)):
        tr.put(wordlist[i], i)

    print(tr.starts_with_prefix(''))
    
    print(tr.starts_with_prefix('s'))

    print(tr.keys())
    print(tr.keys_with_prefix('s'))

if __name__ == '__main__':
    main()