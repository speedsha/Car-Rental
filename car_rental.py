from datetime import datetime

class CarRental:

    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        print(f"\nWe currently have {self.stock} cars available for rent.\n")
        return self.stock

    def rent_hourly(self, num_cars):
        if num_cars <= 0:
            print("Number of cars must be positive.")
            return None
        if num_cars > self.stock:
            print(f"Sorry! Only {self.stock} cars available.")
            return None

        rental_time = datetime.now()
        self.stock -= num_cars
        print(f"\nYou rented {num_cars} car(s) hourly at {rental_time}")
        return rental_time

    def rent_daily(self, num_cars):
        if num_cars <= 0:
            print("Number of cars must be positive.")
            return None
        if num_cars > self.stock:
            print(f"Sorry! Only {self.stock} cars available.")
            return None

        rental_time = datetime.now()
        self.stock -= num_cars
        print(f"\nYou rented {num_cars} car(s) daily at {rental_time}")
        return rental_time

    def rent_weekly(self, num_cars):
        if num_cars <= 0:
            print("Number of cars must be positive.")
            return None
        if num_cars > self.stock:
            print(f"Sorry! Only {self.stock} cars available.")
            return None

        rental_time = datetime.now()
        self.stock -= num_cars
        print(f"\nYou rented {num_cars} car(s) weekly at {rental_time}")
        return rental_time

    def return_cars(self, request):
        rental_time, rental_mode, num_cars = request

        if rental_time and rental_mode and num_cars:
            self.stock += num_cars

            now = datetime.now()
            rental_period = now - rental_time
            hours = rental_period.total_seconds() / 3600

            hourly_rate = 10
            daily_rate = 50
            weekly_rate = 200

            if rental_mode == 1:
                bill = hours * hourly_rate * num_cars
            elif rental_mode == 2:
                bill = (hours / 24) * daily_rate * num_cars
            else:
                bill = (hours / (24 * 7)) * weekly_rate * num_cars

            bill = round(bill, 2)

            print("\n----- BILL -----")
            print(f"Cars Returned: {num_cars}")
            print(f"Rental Duration: {rental_period}")
            print(f"Total Bill: ${bill}")
            print("----------------\n")

            return bill
        else:
            print("Invalid return request.")
            return None


class Customer:

    def __init__(self):
        self.cars = 0
        self.rental_time = None
        self.rental_mode = None

    def request_cars(self):
        try:
            cars = int(input("How many cars do you want? "))
        except:
            print("Enter a valid number.")
            return None

        if cars <= 0:
            print("Number must be greater than zero.")
            return None

        self.cars = cars
        return self.cars

    def return_cars(self):
        if self.rental_time and self.rental_mode and self.cars:
            return self.rental_time, self.rental_mode, self.cars

        print("You have no active rentals.")
        return None
