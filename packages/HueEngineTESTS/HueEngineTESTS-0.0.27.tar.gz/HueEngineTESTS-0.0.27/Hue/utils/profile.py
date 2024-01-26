#  Hue Engine
#  2023-2024 Setoichi Yumaden <setoichi.dev@gmail.com>
#
#  This software is provided 'as-is', without any express or implied
#  warranty.  In no event will the authors be held liable for any damages
#  arising from the use of this software.
#
#  Permission is granted to anyone to use this software for any purpose,
#  including commercial applications, and to alter it and redistribute it
#  freely, subject to the following restrictions:
#
#  1. The origin of this software must not be misrepresented; you must not
#     claim that you wrote the original software. If you use this software
#     in a product, an acknowledgment in the product documentation would be
#     appreciated but is not required.
#  2. Altered source versions must be plainly marked as such, and must not be
#     misrepresented as being the original software.
#  3. This notice may not be removed or altered from any source distribution.

import functools, time, psutil

SYSTIMES = {
    'Rendering': 0,
    'Physics': 0
}

def SystemHealth() -> None:
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    #print(f"CPU Usage: {cpu_usage}%")
    #print(f"Memory Usage: {memory_usage}%")
    return f"<CPU> | {cpu_usage}% | <MEM> | {memory_usage}%"

# SI ( System Impact )
def ReportSystemImpact() -> None:
    total_time = sum(SYSTIMES.values())
    for system, time_spent in SYSTIMES.items():
        if total_time > 0:
            percentage = (time_spent / total_time) * 100
            #print(f"{system.title()} System Impact: {percentage:.2f}%")
            return f"<{system.title()}> SI | {percentage:.2f}%"
        else:
            #print(f"{system.title()} System Impact: No data")
            return f"<{system.title()}> SI | No data"

def ErrorCatch(func, *args, **kwargs) -> None:
    """
    Executes a function safely with given arguments, catching and handling common exceptions.

    Parameters:
    func (callable): The function to be executed.
    *args: Variable length argument list for the function.
    **kwargs: Keyworded, variable-length argument dictionary for the function.
    """
    try:
        return func(*args, **kwargs)
    except ValueError as ve:
        print("\n🚫 ValueError Encountered:")
        print(f"    Description: {ve}\n")
    except TypeError as te:
        print("\n🚫 TypeError Encountered:")
        print(f"    Description: {te}\n")
    except IOError as ie:
        print("\n🚫 IOError Encountered:")
        print(f"    Description: {ie}\n")
    except ZeroDivisionError as zde:
        print("\n🚫 ZeroDivisionError Encountered:")
        print(f"    Description: {zde}\n")
    except IndexError as ie:
        print("\n🚫 IndexError Encountered:")
        print(f"    Description: {ie}\n")
    except KeyError as ke:
        print("\n🚫 KeyError Encountered:")
        print(f"    Description: {ke}\n")
    except AttributeError as ae:
        print("\n🚫 AttributeError Encountered:")
        print(f"    Description: {ae}\n")
    except ImportError as imp:
        print("\n🚫 ImportError Encountered:")
        print(f"    Description: {imp}\n")
    except NameError as ne:
        print("\n🚫 NameError Encountered:")
        print(f"    Description: {ne}\n")
    except SyntaxError as se:
        print("\n🚫 SyntaxError Encountered:")
        print(f"    Description: {se}\n")
    except Exception as e:
        print("\n🚫 Unexpected Error Encountered:")
        print(f"    Description: {e}\n")

def RunTest(func):
    def wrapper(*args, **kwargs):
        print(f"\n~|\tEntering {func.__name__}")
        result = func(*args, **kwargs)
        print(f"\n~|\tExiting {func.__name__}")
        return result
    return wrapper

def OutputReturn(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"\n~| Function {func.__name__} returned:\n{result}\n")
        return result
    return wrapper

def ProfileExec(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"\n~|\tEXECUTION PROFILER\n________\nMETHOD: {func.__name__} | TIME: {end_time - start_time:.3f}s\n")
        return result
    return wrapper

def ProfileSystem(system_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            SYSTIMES[system_name] += end_time - start_time
            return result
        return wrapper
    return decorator
