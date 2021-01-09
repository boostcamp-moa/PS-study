class MyHashSet {
  private container: number[] = [];

  constructor() {}

  add(key: number): void {
      if(!this.contains(key)){
          this.container.push(key);
      }
  }

  remove(key: number): void {
      this.container = this.container.filter((number)=>number!==key);
  }

  contains(key: number): boolean {
      return this.container.some((number)=>number===key);
  }
}

/**
* Your MyHashSet object will be instantiated and called as such:
* var obj = new MyHashSet()
* obj.add(key)
* obj.remove(key)
* var param_3 = obj.contains(key)
*/