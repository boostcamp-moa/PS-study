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
  public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
      List<List<Integer>> list = new LinkedList<>();
      run(root,0,list);
      
      return list;
  }
  
  public void run(TreeNode root,int level,List<List<Integer>> list){
      if(root==null){
          return;
      }
      
      if(list.size()<=level){
          list.add(new LinkedList<Integer>());
      }
      if((level%2)==0){
          list.get(level).add(root.val);
      }else{
          list.get(level).add(0,root.val);
      }
      run(root.left,level+1,list);
      run(root.right,level+1,list);
  }
}