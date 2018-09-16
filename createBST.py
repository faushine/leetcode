class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insert(tree, node):
    if tree is None:
        tree = TreeNode(node.val)
    if node.val > tree.val:
        if tree.right is None:
            tree.right = TreeNode(node.val)
        else:
            insert(tree.right, node)
    else:
        if tree.left is None:
            tree.left = TreeNode(node.val)
        else:
            insert(tree.left, node)


def getKthElement(root,k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k = k-1
        if k == 0:
            return root.val
        root = root.right

def inorder(tree):
    if tree:
        inorder(tree.left)
        print(tree.val)
        inorder(tree.right)

if __name__ == '__main__':
    root = TreeNode(6)
    insert(root,TreeNode(4))
    insert(root,TreeNode(2))
    insert(root,TreeNode(1))
    insert(root,TreeNode(5))
    insert(root,TreeNode(7))
    insert(root,TreeNode(8))
    insert(root,TreeNode(3))
    insert(root,TreeNode(9))
    # inorder(root)
    print(getKthElement(root,7))