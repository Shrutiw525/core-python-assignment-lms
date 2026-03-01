'''Scenario:A teacher wants to track student performance. Write a program to calculate the **average marks** of students and identify the **top performer**.
Requirements:
- Use a function to calculate the average marks.
- Identify the student with the highest average.
- Optional: Implement a `Student` class to handle this logic.
Input Example:
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
Expected Output:
Average Marks: {"John": 85, "Alice": 87.33, "Bob": 75}
Top Performer: "Alice"
'''
def avg_marks(students):
    average_marks={}
    for name,grades in students.items():
        avg=sum(grades)/len(grades)
        average_marks[name]=round(avg,2)
    return average_marks
def top_perf(average_marks):
    return max(average_marks, key=average_marks.get)
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
p=avg_marks(students)
print("Average Marks: ",p)
print("Top Performer: ",top_perf(p))