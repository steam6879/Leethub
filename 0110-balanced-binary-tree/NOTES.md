# ​Explanation
We can use a depth-first search (DFS) traversal algorithm to solve this problem recursively.

We use a global variable ans, to keep track of our balanced status. It is initially set to True.

We are given that —

>_a binary tree in which the left and right subtrees of every node differ in height by no more than 1._

Therefore, we traverse all nodes in the tree and find the heights of every node’s left and right subtrees.

If the absolute difference between them is greater than one, we can say that our binary tree is not balanced. So , we update ans to False.

Finally, we return ans.

## Time and Space Complexity
Since we are visiting all nodes in the tree a constant number of times, we can say that our algorithm requires a linear amount of time to run.

Also, the recursion stack could be storing all nodes in the tree in case of a really skewed tree (like a linked list). So, we assume the space complexity to be linear in the worst case.

Thus, if n is the number of nodes in the given binary tree,

* Time Complexity: O(n)

* Space Complexity: O(n)
