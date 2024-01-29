from .llm import generate

def booty():
  print("🍑🫲")

class FunctionBuilder:
    def __init__(self):
        # Store function names and instructions
        self.functions = {}

    def create(self, function_name, instructions):
        # Store the instructions
        self.functions[function_name] = instructions

        # Define the dynamic function
        def dynamic_function(msg):
            response = generate(msg, instructions)
            print(response)

        # Assign the dynamic function to this instance
        setattr(self, function_name, dynamic_function)