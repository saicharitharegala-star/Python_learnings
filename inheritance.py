class vehicle:
    company = "TATA"
    def __init__(self,n_wheels,seats,mileage):
        print("init of vehicle class")
        self.n_wheels = n_wheels
        self.seats = seats
        self.mileage = mileage 
    
    def get_details(self):
        return f"Number of wheels: {self.n_wheels}, Number of seats: {self.seats}, Mileage: {self.mileage} km/l"
    
#v1 = vehicle(4,5,15)
#print(v1.get_details())

class car(vehicle):
    print("init of car class")
    def __init__(self, car_type , drive_type, n_wheels,seats,mileage):
        self.car_type = car_type
        self.drive_type = drive_type
        super().__init__(n_wheels,seats,mileage) #super() is used to call the parent class constructor
    
    def car_details(self):
        print(f"Car type: {self.car_type}, Drive type: {self.drive_type}")

class electric_car(car):
    print("init of electric car class")
    def __init__(self, battery_capacity,distance_range, car_type , drive_type, n_wheels,seats,mileage):
        self.battery_capacity = battery_capacity
        self.distance_range = distance_range
        super().__init__(car_type , drive_type, n_wheels,seats,mileage)
    
    def charge(self):
        print(f"Charging the electric car with battery capacity: {self.battery_capacity} kWh")


ec1 = electric_car(100, 400, "Sedan", "manual", 4, 5, 35)

print(ec1.__dict__)