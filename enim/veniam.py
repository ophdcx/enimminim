try:
    # Code that might raise an exception
    some_function_that_may_raise_error()
except SomeException as e:
    # Handle the exception or log it
    print(f"An error occurred: {e}")
    # Re-raise the original exception
    raise
