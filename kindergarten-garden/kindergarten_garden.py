PLANTS = {"C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violets"}
STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

class Garden(object):
	def __init__(self, diagram, students = None):
		self.rows = diagram.split()

		if students is None:
			self.students = STUDENTS
		else:
			self.students = sorted(students)

	def plants(self, student):
		i = self.students.index(student)

		pos = i * 2

		l = list(self.rows[0][pos:pos+2] + self.rows[1][pos:pos+2])

		plants = []

		for j in l:
			plants.append(PLANTS[j])

		return plants
