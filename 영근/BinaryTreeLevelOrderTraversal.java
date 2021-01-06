class Solution {
    
  public List<List<Integer>> levelOrder(TreeNode root) {
      List<List<Integer>> ans = new LinkedList<>();
      run(root,ans,0);
      return ans;
  }
  
  public void run(TreeNode root,List<List<Integer>> list,int level){
      if(root==null){
          return;
      }
      
      if(list.size()<=level){
          list.add(new LinkedList<Integer>());
      }
      
      List<Integer> levelList=list.get(level);
      levelList.add(root.val);
      run(root.left,list,level+1);
      run(root.right,list,level+1);
  }
}
