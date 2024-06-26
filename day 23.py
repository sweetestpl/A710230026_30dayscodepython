class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0  # Default speed is 0

    def accelerate(self, increment):
        self.speed += increment

    def brake(self, decrement):
        self.speed -= decrement

    def display_speed(self):
        print(f"The {self.color} {self.brand} {self.model}'s current speed is {self.speed} km/h")


# Contoh penggunaan kelas Car
if __name__ == "__main__":
    # Membuat objek mobil pertama
    car1 = Car("Toyota", "Camry", "Red")
    
    # Mengakselerasi mobil pertama
    car1.accelerate(30)
    car1.display_speed()  # Output: The Red Toyota Camry's current speed is 30 km/h
    
    # Membuat objek mobil kedua
    car2 = Car("Honda", "Accord", "Blue")
    
    # Mengakselerasi mobil kedua
    car2.accelerate(20)
    car2.display_speed()  # Output: The Blue Honda Accord's current speed is 20 km/h
    
    # Mengurangi kecepatan mobil pertama
    car1.brake(10)
    car1.display_speed()  # Output: The Red Toyota Camry's current speed is 20 km/h
