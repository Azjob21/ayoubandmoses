def greet(name):
    """Greets the user."""
    print(f"Hello, {name}!")

# Main function
def main():
    user_name = input("Enter your name: ")
    greet(user_name)

if __name__ == "__main__":
    main()
