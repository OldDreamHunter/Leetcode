# Binary Tree

* 生成二叉树

* 遍历二叉树

  * 前中后序遍历

    **Binary Tree Preorder Traversal**
    前序遍历就是先遍历根节点，再依次压入不为空的右节点和左节点到堆栈中

    

    **Binary Tree Inorder Traversal**
    中序遍历就是一直遍历根节点的左节点，压入堆栈，直到左节点为None，然后pop，再看pop的节点有没有右节点，如果有，则按根节点的遍历方式遍历，直到遍历完

    

    **Binary Tree Inorder Traversal**
    后序遍历一个二叉树, iterative的方式是按前序遍历root -> left-> right改为 root ->right->left，然后再逆序输出
    
    
  
  * 层次遍历
  
    **Binary Tree Level Order Traversal** 
    层序遍历，每一层上的数据按照从左到右的顺序排列。 
    递归、迭代
  
    
  
    **Binary Tree Level Order Traversal II** 
    层序遍历，这次是从最下层输出到根节点 
    递归、迭代
  
    
  
    **Binary Tree Zigzag Level Order Traversal** 
    按之字形遍历二叉树（一正一反） 
    递归、迭代
  
    
  
    **Path Sum** 
    给定一个数和一棵树，求能否有一条路径上所有叶子结点数值加起来等于给定的数 
    递归
  
    
  
    **Path Sum II** 
    将根到叶子的路径和为sum的路径都枚举出来。 