from car import Car
import car_utils
def main():
    cars = {}  

    while True:
        print("\nMenu:")
        print("1. Add a new car")
        print("2. View all cars")
        print("3. Drive a car")
        print("4. Paint a car")
        print("5. Exit")

        choice = input("Choose an option:\n")

        if choice == '1':
          new_car = car_utils.create_car_from_input()
          cars[new_car.car_id] = new_car
          print(new_car)
          print("Car added.")

        elif choice == '2':
          car_utils.display_cars(cars)

        elif choice == '3':
          car_id = input("Enter the car ID to drive:\n")
          miles = float(input("How many miles to drive?\n"))
          if car_id in cars:
             car = cars[car_id]
             car.drive(miles)
             print("Mileage updated.")
             print(car)
          else:
             print("Car not found.")
          
        elif choice == '4':
          car_id = input("Enter the car ID to paint:\n")
          new_color = input("Enter the new color:\n")
          if car_id in cars:
             car.change_color(new_color)
             print("Color updated.")
             print(car)
          else:
             print("Car not found.")
        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
