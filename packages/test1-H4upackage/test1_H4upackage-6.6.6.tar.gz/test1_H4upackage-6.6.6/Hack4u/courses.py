class Course:
    def __init__(self,name,duration,link):
        self.name = name
        self.duration = duration
        self.link = link

    #remember str is for a more informal representation
    #works singularly
    # def __str__(self):
    #     return(f'Course name:{self.name}, Duration:{self.duration}, Link:{self.link}')

    #Its able to work in group
    def __repr__(self):
        return(f'[{self.name}], [Duration:{self.duration}], [Link:{self.link}]')

courses = [
    Course("Linux Introduction",15,"https://hack4u.io/cursos/introduccion-a-linux/"),
    Course("Linux Personalization",3,"https://hack4u.io/cursos/personalizacion-de-entorno-en-linux/"),
    Course("Ofencive Python",35,"https://hack4u.io/cursos/python-ofensivo/"),
    Course("Hacking Introduction",53,"https://hack4u.io/cursos/introduccion-al-hacking/")
]

#using __str__
# for course in courses:
#     print(course)

#using __repr__
# print(courses[0])

def list_courses():
    for course in courses:
        print(course)

def list_courses_byname(name):
    for course in courses:
        if course.name == str(name):
            print(course)




