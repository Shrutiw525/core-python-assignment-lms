'''
A hospital needs a system to manage patient records. Write a program to store patient data, including **name, age, and disease**, and allow the admin to search for patients by disease.
Requirements:
- Store patient records in a list of dictionaries.
- Allow searching for patients based on disease.
- Optional: Use a `Patient` class to manage records.
Input Example:
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_disease = "Flu"
Expected Output:
Patients with Flu: ["Alice", "Charlie"]
'''
def disease(patients,search_disease):
    res=[]
    for i in patients:
        if i["Disease"]==search_disease:
            res.append(i["Name"])
    return res
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_disease = "Flu"
print(f"Patients with {search_disease}: ",disease(patients,search_disease))
search_disease = "Flu"