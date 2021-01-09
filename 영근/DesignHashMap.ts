interface item {
  key:number;
  value:number;
}

class MyHashMap {
  private container: item[]=[];
  constructor() {

  }

  put(key: number, value: number): void {
      if(!this.has(key)){
          this.container.push({key,value});
      }else{
          this.container.find((node)=>node.key===key).value=value;
      }
  }

  get(key: number): number {
      if(!this.has(key)){
          return -1;
      }
      
      return this.container.find((node)=>node.key===key).value;
  }
  
  has(key:number):boolean{
      return this.container.some((node)=>node.key===key);
  }

  remove(key: number): void {
      this.container = this.container.filter((node)=>node.key!==key);
  }
}

/**
* Your MyHashMap object will be instantiated and called as such:
* var obj = new MyHashMap()
* obj.put(key,value)
* var param_2 = obj.get(key)
* obj.remove(key)
*/