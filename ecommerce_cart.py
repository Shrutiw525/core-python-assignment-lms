'''
You are designing the logic for an e-commerce website. Write a program to calculate the total price of items in a user's cart. If the cart contains more than 5 items, apply 10% discount.
Requirements:
- Use a function to calculate the total price.
- Handle cases where the cart is empty.
Input Example:
cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
Expected Output:
Total Price: 54000
'''
def cart_items_price(n,cart):
    if n==0:
        return 0
    sumi=sum(cart.values())
    if n>5:
        return sumi-(sumi*0.10)
    return sumi
n=int(input())
cart={}
for _ in range(n):
    item=input("Enter the item:")
    price=int(input("Enter its price:"))
    cart[item]=price
print("Total Price: ",cart_items_price(n,cart))