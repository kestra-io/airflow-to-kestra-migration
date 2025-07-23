def _print_astronaut_craft(person_in_space: dict, greeting: str = "Hello!"):
    craft = person_in_space["craft"]
    name = person_in_space["name"]

    print(f"{name} is currently in space flying on the {craft}! {greeting}")
