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
  public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
      if(t1==null&&t2==null){
          return null;
      }
      
      if(t1==null){
          return t2;
      }
      
      if(t2==null){
          return t1;
      }
      
      if(t1!=null&&t2!=null){
          t1.val+=t2.val;
      }
      
      //왼쪽 순회
      TreeNode left = mergeTrees(t1.left,t2.left);
      //오른쪽 순회
      TreeNode right = mergeTrees(t1.right,t2.right);
      t1.left = left;
      t1.right = right;
      
      return t1;
  }
}