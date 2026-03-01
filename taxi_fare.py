'''A taxi service calculates fares based on the following rates: 
- **Base fare**: $50 
- **Distance fare**: $10/km 
Write a program to calculate the total fare for multiple trips.
Requirements:
- Use a function to calculate fare for each trip.
Input Example:
```python
trips = [5, 10, 3]  # Distances in km
```
Expected Output:
```
Trip 1: $100
Trip 2: $150
Trip 3: $80
Total Fare: $330
'''
def fare(trips,res):
    for i in trips:
        res.append(50+(i*10))
    return res
trips = [5, 10, 3]
res=[]
p=fare(trips,res)
for i in range(len(p)):
    print(f"Trip{i+1}: ${p[i]}")
print(f"Total Fare: ${sum(p)}")