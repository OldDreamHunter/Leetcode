class solution(object):
    def __init__(self):
        pass

    def _sameNode(self,node1,node2):
        if node1 == None and node2 == None:
            return True
        elif node1 != None and node2 != None:
            if node1.val == node2.val:
                return True
            else:
                return False
        else:
            return False

    def sameTree(self,root1,root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        else:
            return self.sameTree(root1.left,root2.left) and \
                   self.sameTree(root1.right,root2.right)



