from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Passed " + str(time_elapsed.total_seconds()) + " seconds")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 1000):
        pass

@execution_time
def plus(a: int, b:int) -> int:
    return a + b

@execution_time
def greeting(name="Diego"):
    print("Hi " + name)

random_func()
plus(5, 5)
greeting("Ingrid")