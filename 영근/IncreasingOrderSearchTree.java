class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public TreeNode increasingBST(TreeNode root) {
        if(root == null){
            return null;
        }
        TreeNode answer = root;
        TreeNode left = increasingBST(root.left);
        TreeNode right = increasingBST(root.right);
        
        answer.left=null;
        answer.right=null;
        
        if(right!=null){
            answer.right=right;
        }
        
        if(left!=null){
            TreeNode leftTail=left;
            while(leftTail.right!=null){
                leftTail=leftTail.right;
            }
            leftTail.right=answer;
            answer=left;
        }
        
        return answer;
    }
}