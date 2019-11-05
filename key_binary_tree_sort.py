from key_binary_tree import KeyBinaryTree

def key_binary_tree_sort(list_, key=lambda x: x, reverse=False):

    class Tree(KeyBinaryTree):
        def to_list(self):
            list_ = []
            def handle(tree):
                list_.append(tree.root.key)
            self.inorder_traversal(self, handle)
            return list_

    list_ = list(map(lambda item: (key(item), item), list_))
    tree = Tree()
    for key, item in list_:
        tree.add(key, item)
    list_ = tree.to_list()
    return list_
        

