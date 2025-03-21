from tenacity import retry, wait_random_exponential, stop_after_attempt


class ManagerTools:
    RETRY = lambda: retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))

    @classmethod
    def debugger_exception_decorator(cls, func):
        """Wrap the function in a try flow, where the Exception is printed."""
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"{func.__name__} Error: {e}")
        return wrapper
        
    # @debugger_exception_decorator
    async def debugger_sleeper(duration: int) -> None:
        """
        Implement time.sleep function to test purposes.
        
        Args:
            duration (int): Duration in seconds to sleep.
        """
        import time
        print("Sleeping...")
        time.sleep(duration)
        
    # @debugger_exception_decorator
    def debugger_print(*args):
        """
        Print debugging information.
        
        Args:
            *args: Variable number of arguments to print.
        """
        message = ' '.join(map(str, args))
        print(message)


    def logger_print(self):
        print(self.__class__.__name__)