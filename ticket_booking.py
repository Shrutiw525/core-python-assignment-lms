'''
A cinema hall wants to manage ticket bookings. Write a program to keep track of **available** and **booked seats**. Allow users to **book** or **cancel** a seat.
Requirements:
- Use functions to handle seat booking and cancellation.
- Prevent booking an already booked seat.
Input Example:
total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5
Expected Output:
Available seats: [1, 4, 6, 8, 9, 10]
'''
total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5
li=[]
for i in range(1,total_seats+1):
    if i not in booked_seats and i!=book_seat and i!=cancel_seat:
        li.append(i)
print(li)