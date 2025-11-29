# write your solution here
def info(s_file: str, e_file: str):
    names = {}
    exercises = {}
    with open(s_file) as sf, open(e_file) as ef:
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
            exercises[parts[0]] = sum(list(map(int,parts[1:])))


    for pic, name in names.items():
        if pic in exercises:
            total_exercises = exercises[pic]
            print(f"{name} {total_exercises}")
        else:
            print(f"{name} 0")



s_info_file = input("Student information: ")
e_info_file = input("Exercises completed: ")

info(s_info_file, e_info_file)
