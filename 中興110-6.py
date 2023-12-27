class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    # 前序遍歷的第一個元素即為根節點
    root_val = preorder[0]
    root = TreeNode(root_val)

    # 在中序遍歷中找到根節點的位置
    root_index_inorder = inorder.index(root_val)

    # 遞迴構建左子樹和右子樹
    root.left = buildTree(preorder[1:1 + root_index_inorder], inorder[:root_index_inorder])
    root.right = buildTree(preorder[1 + root_index_inorder:], inorder[root_index_inorder + 1:])

    return root

# 測試
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = buildTree(preorder, inorder)

# 在此可以添加額外的程式碼來確認樹是否正確建立，例如進行中序遍歷
def inorderTraversal(node):
    if node:
        inorderTraversal(node.left)
        print(node.val, end=" ")
        inorderTraversal(node.right)

print("Inorder Traversal of the reconstructed tree:")
inorderTraversal(root)
