'''
A company collects customer feedback in the form of ratings (1-5). Write a program to calculate the **percentage of positive feedback** (4 or 5).
Requirements:
- Use a function to calculate the positive feedback percentage.
- Handle cases where no ratings are available.
Input Example:
```python
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
```
Expected Output:
Positive Feedback: 62.5%
'''
def percen(ratings):
    sumi=0
    for i in ratings:
        if i==4 or i==5:
            sumi+=1
    return (sumi/len(ratings))*(100)
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(f"Positive Feedback: {percen(ratings)}%")