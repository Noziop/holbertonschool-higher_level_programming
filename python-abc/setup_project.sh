#!/bin/bash

# Create directory
mkdir -p python-abc
cd python-abc

# Create README.md
cat << EOF > README.md
# Python ABC (Abstract Base Classes) Exercises

This project contains exercises focusing on Object-Oriented Programming (OOP) concepts in Python, including abstract classes, interfaces, duck typing, and subclassing standard base classes.

## Files

1. task_00_abc.py - Abstract Animal Class and its Subclasses
2. task_01_duck_typing.py - Shapes, Interfaces, and Duck Typing
3. task_02_verboselist.py - Extending the Python List with Notifications
4. task_03_countediterator.py - CountedIterator - Keeping Track of Iteration
5. task_04_flyingfish.py - The Enigmatic FlyingFish - Exploring Multiple Inheritance
6. task_05_dragon.py - The Mystical Dragon - Mastering Mixins

Each task file has a corresponding main file for testing.

## Usage

To run each exercise, use the following command:

python3 main_XX_filename.py


Replace XX with the task number and filename with the corresponding file name.

## Learning Objectives

- Understand and apply abstract classes
- Grasp the concept of interfaces and duck typing
- Learn to extend standard base classes
- Employ method overriding
- Understand and apply multiple inheritance
- Utilize mixins to compose behavior across unrelated classes

EOF

# Create exercise files with shebang
for i in {00..05}; do
    echo '#!/usr/bin/python3' > task_${i}_*.py
done

# Create main files with their contents
cat << EOF > main_00_abc.py
#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()
print(bobby.sound())
print(garfield.sound())

animal = Animal()
print(animal.sound())
EOF

cat << EOF > main_01_duck_typing.py
#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)
EOF

cat << EOF > main_02_verboselist.py
#!/usr/bin/env python3
from task_02_verboselist import VerboseList

vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)
EOF

cat << EOF > main_03_countediterator.py
#!/usr/bin/env python3
from task_03_countediterator import CountedIterator

data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")
EOF

cat << EOF > main_04_flyingfish.py
#!/usr/bin/env python3
from task_04_flyingfish import Fish, FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()
EOF

cat << EOF > main_05_dragon.py
#!/usr/bin/env python3
from task_05_dragon import Dragon

dragon = Dragon()
dragon.swim()  # Outputs: The creature swims!
dragon.fly()   # Outputs: The creature flies!
dragon.roar()  # Outputs: The dragon roars!
EOF

echo "All files have been created successfully in the python-abc directory."