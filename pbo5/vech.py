from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "The car is driving on the road."

class Bicycle(Vehicle):
    def move(self):
        return "The bicycle is being pedaled along the path."

class Boat(Vehicle):
    def move(self):
        return "The boat is sailing on the water."

class Authenticator(ABC):
    @abstractmethod
    def login(self):
        pass

class EmailPasswordAuth(Authenticator):
    def login(self):
        return "Logging in with email and password."

class GoogleAuth(Authenticator):
    def login(self):
        return "Logging in with Google authentication."

class FingerprintAuth(Authenticator):
    def login(self):
        return "Logging in with fingerprint authentication."

vehicles = [Car(), Bicycle(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())

auth_methods = [EmailPasswordAuth(), GoogleAuth(), FingerprintAuth()]
for auth in auth_methods:
    print(auth.login())
