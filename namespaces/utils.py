import inspect
import sys

def get_current_function_name():
  """Gets the name of the function this code is currently executing within."""
  # Get the current frame in the call stack
  # sys._getframe() is also an option, but inspect is generally preferred
  current_frame = inspect.currentframe()

  # Access the code object from the frame
  if current_frame:
      code_obj = current_frame.f_code

      # The name of the function is stored in the code object's __name__ attribute
      # We need to be careful not to return the name of this helper function itself
      # by looking at the frame *above* this one.
      # However, the user asked for the *current* function name where this is called.
      # If you call this helper *from* another function, you'd want the caller's name.
      # Let's adjust to get the caller's name, which is often the actual intent.

      # Get the frame object for the caller
      caller_frame = current_frame.f_back

      if caller_frame:
          caller_code_obj = caller_frame.f_code
          return caller_code_obj.co_name
      else:
          return "Could not determine caller function name"
  else:
      return "Could not determine current frame"

# Example outside of a function (in the global scope)
# get_current_function_name() # This might behave differently or raise an error in global scope

def doit(s):
    name = get_current_function_name()
    print(f'function {name} in module {__name__} being called with arg {s}')

def doit2(s):
    # Let's try getting the name directly within this function
    current_frame_here = inspect.currentframe()
    if current_frame_here:
        code_obj_here = current_frame_here.f_code
        its_own_name = code_obj_here.co_name
        print(f'function {its_own_name} in module {__name__} being called with arg {s}')

    # Now call the helper to get the caller's name (which is the module/script name here)
    caller_name_from_helper = get_current_function_name()
    print(f"Calling the helper function from here. The helper reported the caller as: {caller_name_from_helper}")
