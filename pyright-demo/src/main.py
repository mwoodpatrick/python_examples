def greet(name: str) -> str:
    return "Hello, " + name

print(greet("Pyright"))
print(greet(42))  # This should trigger a type error

