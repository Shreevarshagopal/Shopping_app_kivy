from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle

class ShoppingCartApp(App):
    def build(self):
        self.products = {'Product 1': {'price': 100, 'image': 'img1.jpg'},
                         'Product 2': {'price': 200, 'image': 'img2.jpg'},
                         'Product 3': {'price': 300, 'image': 'img3.jpg'}}

        self.shopping_cart = {}

        main_layout = BoxLayout(orientation='vertical')

        with main_layout.canvas.before:
            Color(1, 1, 1, 1)  
            self.rect = Rectangle(size=main_layout.size, pos=main_layout.pos)

        scroll_view = ScrollView()

        product_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        for product, details in self.products.items():
            product_box = BoxLayout(orientation='horizontal', spacing=10)
            image = AsyncImage(source=details['image'], size_hint=(0.3, None), height=200, width=300)
            
            product_label = Label(text=f"{product}: ₹{details['price']}", size_hint=(0.4, None), height=100)
            
            quantity_label = Label(text="Quantity: 0", size_hint=(0.1, None), height=100)
            
            add_button = Button(text="Add", size_hint=(0.2, None), height=100, on_press=self.add_to_cart)
            add_button.product = product
            
        
            self.shopping_cart[product] = {'price': details['price'], 'quantity': 0}
            
            product_box.add_widget(image)
            product_box.add_widget(product_label)
            product_box.add_widget(quantity_label)
            product_box.add_widget(add_button)
            product_layout.add_widget(product_box)

        scroll_view.add_widget(product_layout)
        main_layout.add_widget(scroll_view)

        self.total_label = Label(text="Total: ₹0", size_hint_y=None, height=50)
        main_layout.add_widget(self.total_label)

        return main_layout

    def add_to_cart(self, instance):
        product = instance.product
        self.shopping_cart[product]['quantity'] += 1
        total_cost = sum(self.shopping_cart[product]['price'] * self.shopping_cart[product]['quantity']
                         for product in self.shopping_cart)
        self.total_label.text = f"Total: ₹{total_cost}" 

        for widget in instance.parent.children:
            if isinstance(widget, Label) and widget.text.startswith("Quantity"):
                widget.text = f"Quantity: {self.shopping_cart[product]['quantity']}"

if __name__== '__main__':
    ShoppingCartApp().run()
