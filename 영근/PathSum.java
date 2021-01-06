/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
  public boolean hasPathSum(TreeNode root, int sum) {
      if(root==null){
          return false;
      }
      
      return sum(root,sum,0);
  }
  
  public boolean sum(TreeNode root,int sum,int acc){
      if(root==null){
          return false;
      }
      if(root.left==null&&root.right==null){
          return sum == acc+root.val;
      }
      boolean flag=false;
      flag = sum(root.left,sum,acc+root.val);
      flag = flag ? flag:sum(root.right,sum,acc+root.val);
      return flag;
  }
}