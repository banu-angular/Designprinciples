# Open-Closed Principle: Imagine you have a class that calculates discounts for different customer types, like "Regular" and "VIP". If you want to add a new customer type, like "Premium", you'd have to go in and modify the existing class. This violates the principle because the class should be open for extension, but closed for modification. Can you suggest a design that allows for adding new types without changing the original code?
# To adhere to the Open-Closed Principle, we can use inheritance or composition to allow for new customer types without modifying the existing code. Below is an example using inheritance:```python

class Customer:
    def __init__(self, name):
        self.name = name
    def get_discount(self):
        return 0  # Default discount for regular customers   
class VIPCustomer(Customer):
    def get_discount(self):
        return 0.1  # 10% discount for VIP customers
class PremiumCustomer(Customer):
    def get_discount(self):
        return 0.2  # 20% discount for Premium customers
# Example usage:
if __name__ == "__main__":  
    regular_customer = Customer("John Doe")
    vip_customer = VIPCustomer("Jane Smith")
    premium_customer = PremiumCustomer("Bob Johnson")   
    print(f"{regular_customer.name} gets a discount of {regular_customer.get_discount() * 100}%")
    print(f"{vip_customer.name} gets a discount of {vip_customer.get_discount() *
    100}%")
    print(f"{premium_customer.name} gets a discount of {premium_customer.get_discount() * 100}%")
# In this design:
# - The `Customer` class is the base class with a default discount method.
# - The `VIPCustomer` and `PremiumCustomer` classes inherit from `Customer` and
#   override the `get_discount` method to provide specific discount rates.
# This way, we can add new customer types by simply creating new classes that inherit from `Customer`, without modifying the existing code, thus adhering to the Open-Closed Principle. 