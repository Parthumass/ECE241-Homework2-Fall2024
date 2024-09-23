### Changes to this file is NOT allowed!
### Submission of this file will be IGNROED by the autograder!

class StudentNode(object):
    def __init__(self, name, student_id, height, dorm):
        if not isinstance(student_id, int):
            raise ValueError('student_id must be an integer')
        if not isinstance(height, int):
            raise ValueError('height must be an integer')
        if not isinstance(dorm, int):
            raise ValueError('dorm must be an integer')

        self.name = name
        self.student_id = student_id
        self.height = height
        self.dorm = dorm
        self.next = None

    def getNext(self):
        return self.next

    def setNext(self, new_next):
        self.next = new_next

