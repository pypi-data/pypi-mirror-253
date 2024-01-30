from .courses import *

def total_duration():
    print(sum(course.duration for course in courses))

