# 二叉树相关代码测试用例

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node001 = TreeNode(val=4)
node002 = TreeNode(val=5)
node003 = TreeNode(val=6)
node004 = TreeNode(val=7)

node01 = TreeNode(val=2, left=node001, right= node002)
node02 = TreeNode(val=3, left=node003, right=node004)

node1=TreeNode(val=1,left=node01,right=node02)
