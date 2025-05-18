# This is my_module.py

if __name__ == "__main__":
    print(f'The script {__name__} is being run directly.')
else:
    print(f'The script {__name__} is being imported as a module.')

# Define a variable
greeting = f'Hello from {__name__}!'

# Define a function
def greet(name):
  """This function greets the person passed in as a parameter."""
  return f"Hello, {name}!"

# You can also have some code that runs when the module is imported
print("my_module is being imported!")

# A function that might be intended for internal use
def _internal_helper():
  print("This is an internal helper function.")
