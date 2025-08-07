import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('student.xml')
root = tree.getroot()

# Create new student element
new_student = ET.Element("student")

ET.SubElement(new_student, "id").text = "2"
ET.SubElement(new_student, "name").text = "Pema Choden"
ET.SubElement(new_student, "course").text = "IT"
ET.SubElement(new_student, "year").text = "2"

# Add new student to root
root.append(new_student)

# Write back to the file
tree.write('student.xml', encoding='utf-8', xml_declaration=True)

print("New student added to student.xml")
