# write your solution here
def read_fruits():
    fruits = {}
    with open("src/fruits.csv") as fruits_file:
        for line in fruits_file:
            line = line.strip()
            fruit_price = line.split(";")
            fruits[fruit_price[0]] = float(fruit_price[1])

    return fruits
        

if __name__ == "__main__":
    print(read_fruits())
    
    
    