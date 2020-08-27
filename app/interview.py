# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        
        if not root:
            return True
        else:
            def symmetry(left, right):
                if (left and right and left.val==right.val):
                    return symmetry(left.left, right.right) and symmetry(right.left,left.right)
                if left==None and right==None:
                    return True
                else:
                    return False
         
            return symmetry(root.left, root.right)



from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root: return [] #base case 
        res = []
        #queue to colloct all the nodes
        queue = deque([root]) 

        while queue:
            level_vals = [] #hold the values at the current level.
            for _ in range(len(queue)): #evalute once before execution enter the loop
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_vals.append(node.val)
            res.append(level_vals)
        return res            


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return [] #base case 
        res = []
        #queue to colloct all the nodes
        queue = deque([root]) 
        i=0

        while queue:
            i+=1
            
            level_vals = [] #hold the values at the current level.
            for _ in range(len(queue)): #evalute once before execution enter the loop
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_vals.append(node.val)
            if(i%2!=0):    
                res.append(level_vals)
            else: 
                res.append(reversed(level_vals))
                
                
            
        return res 



class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root: return 0 #base case 
        res = []
        #queue to colloct all the nodes
        queue = deque([root]) 
        i=0

        while queue:
            i+=1
            
            level_vals = [] #hold the values at the current level.
            for _ in range(len(queue)): #evalute once before execution enter the loop
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_vals.append(node.val)
            if(i%2!=0):    
                res.append(level_vals)
            else: 
                res.append(reversed(level_vals))
                
                
            
        return len(res)


max depth 
def iterative(self, root):
        if not root:
            return 0
        stack = [[root, 1]]
        h = 0
        m = 0
        while len(stack):
            top, h = stack.pop()
            if top.left: stack.append([top.left, h + 1])
            if top.right: stack.append([top.right, h + 1])
            m = max(h, m)
        return m
def recursive(self, root):
        def rec(root):
            if root:
                return 1 + max(rec(root.left), rec(root.right))
            return 0
    
        return rec(root)     


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if not root: return False
        if not root.left and not root.right and root.val==sum: return True
        x = sum-root.val
        print(x)
        return self.hasPathSum(root.left,x) or self.hasPathSum(root.right,x)        