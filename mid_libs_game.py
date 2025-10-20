

def display():
    print("once upon a time in a far away land called (fill in the location), (fill in the name) was isekied into \
another world to fight vs (fill in the black) and was suprisingly (emotion felt)")
def get_info():
    hero_name = input("Enter a hero's name: ")
    location = input("Enter an adventure location: ")
    villain = input("Enter villain name: ")
    return hero_name,location,villain
def main():
    display()
    hero_name,location,villain = get_info()
    print(f"once upon a time in a far away land called {location}, {hero_name} was isekied into \
another world to fight vs {villain} and was suprisingly happy")
    
if __name__ == "__main__":
    main()
