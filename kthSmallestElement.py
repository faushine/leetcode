class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(4)
    root.right = TreeNode(7)
    root.right.right = TreeNode(9)
    root.right.right.left = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(1)
    root.left.left.right = TreeNode(3)
    tree = getKthElement(root,4)
    print(tree)