from key_binary_node import KeyBinaryNode
from linkqueue import LinkQueue
from printtree import PrintTree

# tree's degree = 2
class KeyBinaryTree:
    def __init__(self, root=None):
        self.root = root
    

    #DLR Data Left Right
    @staticmethod
    def preorder_traversal(tree, handle, end=id):
        if tree.root:
            handle(tree)
            if tree.root.left:
                KeyBinaryTree.preorder_traversal(KeyBinaryTree(tree.root.left), handle, end)
            if tree.root.right:
                KeyBinaryTree.preorder_traversal(KeyBinaryTree(tree.root.right), handle, end)
            end(tree)

    # LDR
    @staticmethod
    def inorder_traversal(tree, handle, end=id):
        if tree.root:
            if tree.root.left:
                KeyBinaryTree.inorder_traversal(KeyBinaryTree(tree.root.left), handle, end)
            handle(tree)
            if tree.root.right:
                KeyBinaryTree.inorder_traversal(KeyBinaryTree(tree.root.right), handle, end)
            end(tree)

    # LRD
    @staticmethod
    def postorder_traversal(tree, handle, end=id):
        if tree.root:
            if tree.root.left:
                BinaryTree.postorder_traversal(BinaryTree(tree.root.left), handle, end)
            if tree.root.right:
                BinaryTree.postorder_traversal(BinaryTree(tree.root.right), handle, end)
            handle(tree)
            end(tree)
    
    def print_line(self):
        rst = []
        def handle(tree):
            rst.append(str(tree.root))
        # LDR 中序遍历显示
        self.inorder_traversal(self, handle)
        rst = "binary tree => " + str(rst)
        return rst

    def print_tree(self):
        rst = PrintTree(list_=self.level_traversal()).rst
        return rst[:-1]

    def level_traversal(self):
        level = -1
        list_ = []
        def handle(tree):
            nonlocal level
            level += 1
            # list_ = [(key,level),...]
            list_.append((str(tree.root), level))
        def end(tree):
            nonlocal level
            level -= 1
        self.preorder_traversal(self, handle, end)
        return list_

    def __str__(self):
        #return self.print_line()
        return self.print_tree()
    
    def add(self, key, item):
        if not self.root:
            self.root = KeyBinaryNode(key, item)
        elif key < self.root.key:
            if not self.root.left:
                self.root.left = KeyBinaryNode(key, item)
                return
            KeyBinaryTree(self.root.left).add(key, item)
        else:
            if not self.root.right:
                self.root.right = KeyBinaryNode(key, item)
                return
            KeyBinaryTree(self.root.right).add(key, item)
    

if __name__ == '__main__':
    t = KeyBinaryTree()
    t.add(3,4)
    t.add(1,'a')
    t.add(8,'hello')
    print(t)
