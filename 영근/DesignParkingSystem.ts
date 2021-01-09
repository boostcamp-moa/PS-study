class ParkingSystem {
  private parkingSpace = [0,0,0];
  private parkingSpaceSize:[number,number,number];
  constructor(big: number, medium: number, small: number) {
      this.parkingSpaceSize = [big,medium,small];
  }

  addCar(carType: number): boolean {
      if(carType<1&&carType>3){
          return false;
      }
      
      const parkingNumber = carType-1;
      if(this.parkingSpace[parkingNumber]<this.parkingSpaceSize[parkingNumber]){
          this.parkingSpace[parkingNumber]++;
          return true;
      }
      
      return false;
  }
}

/**
* Your ParkingSystem object will be instantiated and called as such:
* var obj = new ParkingSystem(big, medium, small)
* var param_1 = obj.addCar(carType)
*/