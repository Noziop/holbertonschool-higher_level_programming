## Introduction

Python's object mutability is a fundamental concept that every developer must grasp. Let's dive into how Python handles different types of objects in memory and how this affects our code behavior.

## ID and Type in Python

In Python, every object has two essential characteristics: its identity (ID) and type. The ID is a unique identifier representing the object's memory address, while the type defines its properties and available operations.

```python
# Example of ID and type
x = 42
y = x
print(f"ID of x: {id(x)}")  # Same memory address
print(f"Type of x: {type(x)}")
print(f"ID of y: {id(y)}")  # Same as x
```

## Mutable Objects

Mutable objects can be modified after creation. The most common mutable objects in Python are lists, dictionaries, and sets.

```python
# List example
my_list = [1, 2, 3]
print(f"Original list: {my_list}")
my_list.append(4)
print(f"Modified list: {my_list}")

# Dictionary example
my_dict = {'name': 'Alice'}
my_dict['age'] = 25
print(f"Dictionary after modification: {my_dict}")
```

## Immutable Objects

Immutable objects cannot be modified after creation. When you perform operations on immutable objects, Python creates new objects instead.

```python
# String example
name = "Alice"
print(f"Original string ID: {id(name)}")
name = name + " Smith"
print(f"New string ID: {id(name)}")  # Different ID!

# Tuple example
my_tuple = (1, 2, 3)
# my_tuple[0] = 4  # This raises TypeError
```

## Memory Management and Performance

Understanding mutability is crucial for memory management and performance optimization. Python treats mutable and immutable objects differently in memory:

```python
# Immutable behavior
x = 5
y = 5
print(id(x) == id(y))  # True due to integer caching

# Mutable behavior
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1) == id(list2))  # False - separate objects
```

## Function Arguments and Object Behavior

Python uses a "pass-by-object-reference" mechanism, which behaves differently for mutable and immutable objects:

```python
def modify_objects(immutable, mutable):
    immutable += 1  # Creates new object
    mutable.append(4)  # Modifies existing object
    print(f"Inside function - immutable: {immutable}, mutable: {mutable}")

number = 42
my_list = [1, 2, 3]
print(f"Before: number = {number}, list = {my_list}")
modify_objects(number, my_list)
print(f"After: number = {number}, list = {my_list}")
```

