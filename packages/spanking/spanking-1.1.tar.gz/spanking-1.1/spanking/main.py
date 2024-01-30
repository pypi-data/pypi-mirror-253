import json
from .llm import generate

def booty():
  print("🍑🫲")

class FunctionBuilder:
    def __init__(self):
        # Store function names and instructions
        self.functions = {}
        # Load previously saved functions
        self.load_functions()

    def create(self, function_name, instructions):
        # Store the instructions
        self.functions[function_name] = instructions

        # Define the dynamic function
        def dynamic_function(msg):
            response = generate(msg, instructions)
            print(response)

        # Assign the dynamic function to this instance
        setattr(self, function_name, dynamic_function)
    
    def publish(self, function_name):
        # Save the function to a file
        if function_name in self.functions:
            with open('functions.json', 'w') as f:
                json.dump(self.functions, f)

    def load_functions(self):
        # Load functions from a file
        try:
            with open('functions.json', 'r') as f:
                saved_functions = json.load(f)
                for name, instructions in saved_functions.items():
                    self.create(name, instructions)
        except FileNotFoundError:
            pass  # No previously saved functions