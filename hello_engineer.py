def greet(name: str) -> str:
    """Return a greeting. First typed function with a type hint."""
    return f"Hello, {name} . Month 1 starts now."


if __name__ == "__main__":
    message = greet("Soham")
print(message)
