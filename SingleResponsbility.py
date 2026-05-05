# You're working on an e-commerce site. When an order comes in, you need to calculate the total price, save the order to the database, and send a confirmation email to the customer. Right now, all of this is handled by a single Python class, which violates the Single Responsibility Principle. Your task is to refactor this code into separate classes, giving each one a single responsibility. Can you write the Python code for that?-->Sure! Below is an example of how you can refactor the code into separate classes, each with a single responsibility:```python
class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item['price'] for item in self.items)   

class OrderRepository:
    def save_order(self, order):
        # Code to save the order to the database
        print("Order saved to the database.")
        # ...
        pass 
class EmailService:
    def send_confirmation_email(self, customer_email, order):
        # Code to send a confirmation email to the customer
        print(f"Confirmation email sent to {customer_email}.")
        # ...
        pass
# Example usage:
if __name__ == "__main__":  
    items = [{'name': 'Laptop', 'price': 999.99}, {'name': 'Mouse', 'price': 49.99}]
    order = Order(items)
    
    total_price = order.calculate_total()
    print(f"Total price: ${total_price:.2f}")
    
    order_repository = OrderRepository()
    order_repository.save_order(order)
    
    email_service = EmailService()
    email_service.send_confirmation_email("customer@example.com", order)    
    
# In this refactored code:
# - The `Order` class is responsible for managing the order and calculating the total price.  
# - The `OrderRepository` class is responsible for saving the order to the database.
# - The `EmailService` class is responsible for sending the confirmation email to the customer.
# This way, each class has a single responsibility, adhering to the Single Responsibility Principle.