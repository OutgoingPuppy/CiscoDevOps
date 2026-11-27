def greet(name: str = "World") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    name = input("Enter your name: ").strip()
    print(greet(name or "World"))
