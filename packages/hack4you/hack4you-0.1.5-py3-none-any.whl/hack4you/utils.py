from .courses import courses


def total_durations():
    total = 0
    for course in courses:
        total += course.duration
    return total