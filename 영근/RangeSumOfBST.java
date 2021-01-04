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
    public int rangeSumBST(TreeNode root, int low, int high) {
        int answer = 0;
        if(root.val>=low&&root.val<=high){
            answer = root.val;
        }
        //왼쪽 순회
        if(root.left!=null){
            answer += rangeSumBST(root.left,low,high);
        } 
        //오른쪽 순회
        if(root.right!=null){
            answer += rangeSumBST(root.right,low,high);
        }
        return answer;
    }
}