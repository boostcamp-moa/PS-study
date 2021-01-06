
public /**
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
   long MIN = Long.MIN_VALUE;
   long MAX = Long.MAX_VALUE;
   public boolean isValidBST(TreeNode root) {
       return run(root,MIN,MAX);
   }
   
   public boolean run(TreeNode root,long min,long max){
       if(root==null){
           return true;
       }
       
       if(root.val<=min){
           return false;
       }
       
       if(root.val>=max){
           return false;
       }
       
       return run(root.left,min,root.val) && run(root.right,root.val,max);
   }
}