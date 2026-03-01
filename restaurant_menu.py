'''
You are managing a restaurant's menu. Write a program to update the menu by adding or removing items and allow users to check if a particular item is available.
Requirements:
- Use functions for adding, removing, and checking menu items.
- Handle cases where the item to be removed does not exist.
Input Example:
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"
Expected Output:
Updated menu: ["Pizza", "Burger", "Pasta", "Tacos"]
Availability: "Pizza is available"
'''
def add_menu(initial_menu,add):
    if add not in initial_menu:
        initial_menu.append(add)
def remove_menu(initial_menu,remove):
    if remove in initial_menu:
        initial_menu.remove(remove)
    else:
        print("Item is not available to remove")
def check_menu(initial_menu,check):
    if check in initial_menu:
        print(f"Availability:{check} is available")
    else:
        print(f"Availability:{check} is not available")
def rest_menu(initial_menu,add,remove,check):
    add_menu(initial_menu,add)
    remove_menu(initial_menu,remove)
    print("Updated menu: ",initial_menu)
    check_menu(initial_menu,check)
initial_menu = list(map(str,input().split()))
add=input("Which item to add:")
remove=input("Which item to remove:")
check=input("Which item to check:")
rest_menu(initial_menu,add,remove,check)