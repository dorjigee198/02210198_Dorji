import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('students.xml')
root = tree.getroot()

# List of new students to add
new_students = [
    {"id": "3", "name": "Sonam Choden", "course": "Computer Science", "year": "2"},
    {"id": "4", "name": "Karma Dorji", "course": "Information Technology", "year": "1"},
    {"id": "5", "name": "Pema Lhamo", "course": "Computer Engineering", "year": "4"},
    {"id": "6", "name": "Tashi Phuntsho", "course": "Software Engineering", "year": "3"},
    {"id": "7", "name": "Choki Wangmo", "course": "Data Science", "year": "2"}
]

# Add new students to the root
for student in new_students:
    student_elem = ET.Element("student")
    
    id_elem = ET.SubElement(student_elem, "id")
    id_elem.text = student["id"]
    
    name_elem = ET.SubElement(student_elem, "name")
    name_elem.text = student["name"]
    
    course_elem = ET.SubElement(student_elem, "course")
    course_elem.text = student["course"]
    
    year_elem = ET.SubElement(student_elem, "year")
    year_elem.text = student["year"]
    
    root.append(student_elem)

# Save the updated XML back to file
tree.write("students.xml", encoding="utf-8", xml_declaration=True)
