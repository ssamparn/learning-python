"""
The difference between static typing and dynamic typing lies in when and how
a programming language checks and enforces the types of variables.

🧊 Static Typing:
    1. Type is checked at compile time.
    2. Variables must be declared with a type.
    3. Errors are caught early, before the program runs.
    4. Common in languages like Java, C, C++, and Go.

  e.g: Java
    int age = 30;
    String name = "Sashank";

✅ Pros:
    1. Early error detection: It helps catch type-related issues early, during the compilation process.
    2. Better performance: Programs often perform better at run-time because there's no need for the interpreter to figure out the types of variables.
    3. Easier to refactor large codebases

❌ Cons:
    1. More verbose
    2. Slower prototyping
    3. Can be felt a bit stricter and restrictive, which can slow down the development due to all the type declarations.


🔥 Dynamic Typing:
    1. Type is checked at runtime. You don't need to declare the type of variables.
       Instead, the type is tied to the value assigned to the variable at runtime.
    2. Variables can hold any type, and types can change.
    3. Common in languages like Python, JavaScript, and Ruby.

Example (Python):
age = 30
age = "thirty"  # This is allowed

✅ Pros:
    1. Faster to write and test because of the flexibility dynamic typing offers.
    2. More flexible and concise

❌ Cons:
    1. Type-related bugs may appear at runtime.
    2. Harder to maintain in large codebases, as these errors are often harder to catch, leading to debugging challenges.

🧪 Python Example to Illustrate:

def add(a, b):
    return a + b

print(add(5, 3))       # 8
print(add("5", "3"))   # "53"
print(add(5, "3"))     # TypeError at runtime

In a statically typed language, the last line would be caught before running the program, but not during compile time.

Type Annotations:

Type annotations in Python help you explicitly declare the expected data types of variables, function arguments, and return values.
While Python remains dynamically typed, these annotations improve code clarity, tooling support, and error detection.

✅ Benefits of Type Annotations:
    1. Improved Readability: Makes it clear what type of data is expected.
    def greet(name: str) -> str:
    return f"Hello, {name}"

    2. Better Tooling: IDEs like VS Code or PyCharm can provide autocomplete, type hints, and warnings.
       Static type checkers like mypy or pyright can catch bugs before runtime.

    3. Documentation: Acts as inline documentation for developers and teams.
    4. Refactoring Safety: Helps ensure changes don’t break type expectations across large codebases.
    5. Optional and Gradual: You can add them incrementally without breaking existing code.

🧪 Example with and without Type Annotations

    Without annotations:
    def add(a, b):
        return a + b


    With annotations:
    def add(a: int, b: int) -> int:
        return a + b

🧰 Advanced Typing Features:

    1. Union types (Python 3.10+):
    def handle(value: int | str) -> None:
    ...

    2. Optional values:
    from typing import Optional
    def get_name(user_id: int) -> Optional[str]:
    ...

    3. Generic types:
    from typing import List

    def average(numbers: List[float]) -> float:
        return sum(numbers) / len(numbers)
"""