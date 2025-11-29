# Write your solution here
def recipes_list(res_file: str):
    read_file = []
    with open(res_file) as rfile:
        for line in rfile:
            read_file.append(line.strip())
    return read_file

def create_book(r_list: list):
    recipes = {}
    key = r_list[0]
    recipes[key] = []

    for i in range(len(r_list)):
        if r_list[i] == '':
            key = r_list[i + 1]
            recipes[key] = []
            continue

        if r_list[i] == key:
            continue

        recipes[key].append(r_list[i])

    return recipes


def search_by_name(res_file: str, name: str):
    r_list = recipes_list(res_file)
    book = create_book(r_list)
    
    found = []
    for key, recipe in book.items():
        if name.lower() in key.lower():
            found.append(key)
    
    return found

def search_by_time(res_file: str, time: int):
    r_list = recipes_list(res_file)
    book = create_book(r_list)
    
    found = []
    for key, recipe in book.items():
        t = int(recipe[0])
        if time >= t:
            found.append(f"{key}, preparation time {t} min")
    
    return found
    

def search_by_ingredient(res_file: str, ingredient: str):
    r_list = recipes_list(res_file)
    book = create_book(r_list)
    
    found = []
    for key, recipe in book.items():
        t = int(recipe[0])
        if ingredient in recipe:
            found.append(f"{key}, preparation time {t} min")
    
    
    return found
    


        

if __name__ == "__main__":
   found_recipes = search_by_time("recipes1.txt", 20)

   for recipe in found_recipes:
       print(recipe)
