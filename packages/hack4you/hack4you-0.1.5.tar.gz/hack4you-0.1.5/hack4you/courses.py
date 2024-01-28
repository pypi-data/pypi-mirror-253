class Course:
    def __init__(self, name, duration, link):
    	self.name = name
    	self.duration = duration
    	self.link = link

    def __repr__(self):
	    return f"El curso {self.name} dura [{self.duration}] horas y se encuentra en ({self.link})"


courses = [
	Course("Introducción al Hacking", 53, "https://hack4u.io/cursos/introduccion-al-hacking/"), 
	Course("Introducción a Linux", 15, "https://hack4u.io/cursos/introduccion-a-linux/"),
	Course("Personalización de nuestro entorno", 3, "https://hack4u.io/cursos/personalizacion-de-entorno-en-linux/"),
	Course("Python ofensivo", 35, "https://hack4u.io/cursos/python-ofensivo/"),
]

def list_courses():
    for course in courses:
        print(course)

def search_course_by_name(name):
	for course in courses:
		if course.name == name:
			return course
	return None
