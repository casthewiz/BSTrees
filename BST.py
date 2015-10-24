class node:
    key = None
    val = None
    lhs = None
    rhs = None
    prnt = None

    def __init__(self, key = None, val = None, lhs = None, rhs = None, prnt = None):
        self.key = key
        self.val = val
        self.lhs = lhs
        self.rhs = rhs
        self.prnt = prnt

    def _put(self, key, value):

        if (key is self.key):
            self.val = value
        elif (key < self.key):
            if (self.lhs is not None):
                return self.lhs._put(key, value)
            else:
                self.lhs = node(key, value)
                return True
        else:
            if (self.rhs is not None):
                return self.rhs._put(key, value)
            else:
                self.rhs = node(key, value)
                return True

    def _get(self, key):
        if (self.key == key):
            return self.val
        elif (key < self.key and self.lhs is not None):
            return self.lhs._get(key)
        elif (key > self.key and self.rhs is not None):
            return self.rhs._get(key)


class BSTree:

    def __init__(self, root = None):
        self.root = root
        self.size = 0
        self.keys = set([])


    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __str__(self):


    def set(self, key, value):
        if(self.root is not None):
            if(self.root._put(key, value)):
                self.keys.add(key)
        else:
            self.root = node(key, value)
            self.keys.add(key)

    def get(self, key):
        if(self.root is None):
            return None
        else:
            return self.root._get(key);

    def balance(self):
        self.root = self._naiveRebalance()


    def _naiveRebalance(self, keys = None):
        print(keys)
        if (keys == None):
            keys = self.keys
        if(not keys):
            return None
        else:
            middle = int(len(keys)/2)
            newKey = list(keys)[middle]
            return node(
                key = newKey,
                val = self.get(newKey),
                lhs = self._naiveRebalance(set(list(keys)[:middle])),
                rhs = self._naiveRebalance(set(list(keys)[middle + 1:]))
                )

    # def _treeToVine(self):
    #
    # def _vineToTree(self):
    #
    # def _compress(self):


#implementation of Day-Stout-Warren Tree rebalancing
# def dayStoutWarren(tree):
