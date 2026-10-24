# Week 4 Python Assignment: Mutability and Memory Management

**Student:** Walid Abdulkadir

## Assignment overview

This assignment explores how Python handles mutable and immutable objects, variables that refer to the same object, and memory management.

## Brief explanations

- **Mutable and immutable objects:** Lists can be changed after creation, while strings and other immutable objects cannot. Updating an immutable value creates a new value.
- **Identity and equality:** `is` checks whether two variables refer to the same object; `==` checks whether their values are equal.
- **Shared references and copying:** When two variables refer to the same list, a change through either variable affects that list. Copying a list creates a separate list.
- **Functions and mutable objects:** A function can modify a mutable object passed to it. Making a copy inside the function avoids changing the original.
- **Memory management:** Removing a variable name with `del` does not necessarily remove the object if another reference still exists. Python reclaims objects that are no longer reachable.

## Project reflection

Working through these examples helped me understand the difference between changing an object and reassigning a variable. I also learned why two variables can display the same list after a change, and how copying a list can prevent unintended modifications. The memory-management examples clarified that deleting a name does not automatically delete an object while other references remain.

## Files

- `questions.py` contains the assignment explanations and runnable code examples.
- `student_marks_manager.py` 

## Requirements

- Python 3
- No third-party packages are required.

## Run the program

Open PowerShell or Command Prompt, change to this project directory, and run:

```powershell
py questions.py
```

If the `py` command is unavailable, use:

```powershell
python questions.py
```
