# write your solution here
def grade(p: int):
    if 0 <= p <= 14:
        return 0
    elif 15 <= p <= 17:
        return 1
    elif 18 <= p <= 20:
        return 2
    elif 21 <= p <= 23:
        return 3
    elif 24 <= p <= 27:
        return 4
    elif 28 <= p:
        return 5


def info(s_file: str, e_file: str, ep_file: str):
    names = {}
    exercises = {}
    total_points = {}
    with open(s_file) as sf, open(e_file) as ef, open(ep_file) as epf:
        for line in sf:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            names[parts[0]] = f"{parts[1]} {parts[2]}"

        for line in ef:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            exercises[parts[0]] = sum(list(map(int,parts[1:]))) // 4
       
        for line in epf:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            total_points[parts[0]] = exercises[parts[0]] + sum(list(map(int, parts[1:])))
            


    for pic, name in names.items():
        if pic in total_points:
            points = total_points[pic]
            g = grade(points)
            print(f"{name} {g}")
        else:
            print(f"{name} 0")
            
            
            



s_info_file = input("Student information: ")
e_info_file = input("Exercises completed: ")
exam_points_file = input("Exam points: ")

info(s_info_file, e_info_file, exam_points_file)
