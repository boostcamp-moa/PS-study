class Solution {
  public boolean isValid(String s) {
      Stack<Character> st = new Stack<>();
      for(int i=0;i<s.length();i++){
          char c = s.charAt(i);
          if(isOpenParentheses(c)){
              st.add(c);
          }else{
              if(!isCorrectParentheses(c,st)){
                  return false;
              }else{
                  st.pop();
              }
          }
      }
      
      if(st.isEmpty()){
          return true;
      }
      
      return false;
  }
  
  public boolean isOpenParentheses(char c){
      if(c=='(' || c=='[' || c=='{'){
          return true;
      }
      return false;
  }
  
  
  public boolean isCorrectParentheses(char c,Stack<Character> st){
      if(isOpenParentheses(c)){
          return false;
      }
      
      if(st.isEmpty()){
          return false;
      }
      char peek = st.peek();
      if(peek=='(' && c==')'){
          return true;
      }else if(peek=='[' && c==']'){
          return true;
      }else if(peek=='{' && c=='}'){
          return true;
      }
      
      return false;
  }
}