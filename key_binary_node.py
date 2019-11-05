class KeyBinaryNode:
    def __init__(self, key=None, item=None, left=None, right=None):
        self.key = key
        self.item = item
        self.left = left
        self.right = right

    def add_left(self, key, item):
        if self:
            self.left = BinaryNode(key, item)

    def add_right(self, key, item):
        if self:
            self.right = BinaryNode(key, item)
    
    def __str__(self):
        return str({self.key: self.item})
