class Course:
    
    def __init__(self, name, duration, link):
        self.name = name
        self.duration = duration
        self.link = link

    
    def __str__(self):
        return f"{self.name} - {self.duration} - {self.link}"
    
    # def __repr__(self):
    #     return f"{self.nombre} - {self.duration} - {self.link}"


courses = [
    Course("Introduccion a linux", 15, "link1"),
    Course("Personalización de linux", 3, "link2"),
    Course("Introducción al hacking", 53, "link3")
]

def list_course():
    for c in courses:
        print(c)



def search_course_by_name(name):
    for c in courses:
        if c.name == name:
            return c