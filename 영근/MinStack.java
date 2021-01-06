class MinStack {
  private int defaultSize = 5;
  private int[] container = new int[defaultSize];
  private int pointer = -1;
  /** initialize your data structure here. */
  public MinStack() {
      
  }
  
  public void push(int x) {
      resize();
      container[++pointer]=x;
  }
  
  public void pop() {
      resize();
      pointer--;
  }
  
  public int top() {
      return container[pointer];
  }
  
  public int getMin() {
      int min=Integer.MAX_VALUE;
      for(int i=0;i<pointer+1;i++){
          min = Math.min(container[i],min);
      }
      return min;
  }
  
  private void resize(){
      if(pointer+1<container.length){
          return;
      }
      
      int[] temp = new int[container.length];
      
      for(int i=0;i<container.length;i++){
          temp[i]=container[i];
      }
      
      defaultSize*=2;
      container = new int[defaultSize];
      
      for(int i = 0;i<temp.length;i++){
          container[i]=temp[i];
      }
  }
}

/**
* Your MinStack object will be instantiated and called as such:
* MinStack obj = new MinStack();
* obj.push(x);
* obj.pop();
* int param_3 = obj.top();
* int param_4 = obj.getMin();
*/