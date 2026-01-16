student={
    "Name":{"Putin","Anurag"},
    "Age":{20,21}
}
print(student["Name"])

Countries={
    "Country Name":{"India","Germany","France","Australia"},
    "Capital":{"Delhi","Berlin","Paris","Canbera"}
}
print(Countries["Country Name"])
print(Countries["Capital"])

Countries["USA"]="NEwYork"
Countries.pop("Country Name")


Student={
    
    "Balvant":67,
    "Ayush":75,
    "Anurag":89,
    "Devansh":90
    
}
print(Student.items())
print(Student.get("Anurag"))
Student.update({"putin":2})
print(Student)



