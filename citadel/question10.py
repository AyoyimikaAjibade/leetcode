# 3. Special Nodes

# Given a tree with N nodes, a node is called special if it is an end-point of any of the diameters of the tree. 
# For all the nodes of the tree, find if it is special or not. Thus, return a binary array, where the ith value of the array will be 1, 
# in case the ith node is special. Else, the ith value of the array will be 0.

# Note: The diameter of a tree is defined as the number of edges in the longest path of the tree.

# For example, consider the tree given below:


# We can see that this tree has only one diameter, which is the unique path between nodes 1 and 3. The length of the diameter is 2.
# The end-points of the diameter are 1 and 3. Hence, nodes 1 and 3 are considered special, while node 2 is not considered a special node of the tree.
# Function Description
# Complete the function isSpecial in the editor below.
# isSpecial has the following parameter(s): tree_nodes: The number of nodes in the
# tree.
# tree_from: The nodes from which the edge is incident onto the other node tree_to: The nodes on which the edge is incident

# Return
# int[n]: an integer array of size N, where the ith value of the array is 1, in case the th node is special. Else, the value will be 0.
