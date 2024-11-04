class Chatbot:
    def __init__(self):
        self.welcome_message = "Hello! Welcome to [Your Store Name]! How can I assist you today?"
        
    def greet(self, user_input):
        greetings = ["hi", "hello", "hey"]
        if user_input.lower() in greetings:
            return "Hi there! How can I help you today? You can ask about products, check your order status, or get our contact details."
        else:
            return "I'm here to help! Let me know how I can assist you."

    def product_info(self, product_name):
        # Sample products data
        products = {
            "shirt": "$20 - Available in sizes S, M, L",
            "jeans": "$40 - Available in sizes 30-40",
            "sneakers": "$60 - Available in sizes 7-12"
        }
        return products.get(product_name.lower(), "Sorry, we don't have information on that product.")

    def order_status(self, order_id):
        # Simulated order status
        orders = {
            "123": "Shipped - Expected delivery in 3 days.",
            "456": "Processing - Will be shipped soon.",
            "789": "Delivered - Thank you for your purchase!"
        }
        return orders.get(order_id, "Sorry, I couldn't find an order with that ID. Please check and try again.")

    def contact_info(self):
        return "You can reach us at support@yourstore.com or call us at +1 (800) 555-1234."

    def handle_user_input(self, user_input):
        if "product" in user_input.lower():
            product_name = input("Please enter the product name: ")
            return self.product_info(product_name)
        elif "order" in user_input.lower():
            order_id = input("Please enter your order ID: ")
            return self.order_status(order_id)
        elif "contact" in user_input.lower():
            return self.contact_info()
        else:
            return self.greet(user_input)

# Sample interaction
chatbot = Chatbot()
print(chatbot.welcome_message)

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Thank you for visiting! Have a great day!")
        break
    response = chatbot.handle_user_input(user_input)
    print(f"Chatbot: {response}")
