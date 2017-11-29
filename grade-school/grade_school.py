from collections import OrderedDict


class School(object):

    def __init__(self, name):
        self.grade_list = {str(i): [] for i in range(1, 10)}

    def add(self, student, grade):
        try:
            self.grade_list[str(grade)].append(student)
        except:
            raise ValueError('%i not a valid grade' % grade)

    def grade(self, grade):
        return self.grade_list[str(grade)]

    def sort(self):
        return {x: sorted(self.grade_list[x]) for x in self.grade_list.keys()}
