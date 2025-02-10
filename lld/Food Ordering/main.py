from typing import List


class Restaurant:
    def __init__(self, name, address, phone):
        self.id = None
        self.name = name
        self.address = address
        self.phone = phone
        self.menu: List[FoodItem] = []
        self.ratings = []  # Stores all ratings to compute average
        self.avg_rating = 0.0
    
    def update_menu(self, menu):
        self.menu = menu
        
    def search_menu(self, item_name):
        for item in self.menu:
            if item.name == item_name:
                return item
        return None
    
    def get_menu(self):
        return self.menu
    
    def update_rating(self, rating):
        self.ratings.append(rating)
        self.avg_rating = round(sum(self.ratings) / len(self.ratings), 1)  # Compute average rating
        

class FoodItem:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        
    def update_price(self, price):
        self.price = price
        
        
class Order:
    def __init__(self, id, items, restaurant: Restaurant):
        self.id = id
        self.items: List[int] = items
        self.status = "open"
        self.restaurant = restaurant  # Store the restaurant object
        
    def add_item(self, item_id):
        self.items.append(item_id)
        
    def remove_item(self, item_id):
        self.items.remove(item_id)
        
    def close(self):
        self.status = "closed"
        
    def get_restaurant(self):
        return self.restaurant
    

class OrderRating:
    def __init__(self, order: Order, rating, comment):
        self.order = order  # Store the order object
        self.rating = rating
        self.comment = comment
        self.update_restaurant_rating()

    def update_restaurant_rating(self):
        """Updates the rating in the associated restaurant."""
        restaurant = self.order.get_restaurant()
        if restaurant:
            restaurant.update_rating(self.rating)
