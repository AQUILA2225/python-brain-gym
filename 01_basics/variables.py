Topic: Variables in Python

** What is a Variable?
---------------------------------------
A variable is a name given to a memory location used to store data.
* In simple words Variable is a container that holds data
* In Python, you do not need to declare the data type explicitly.
* The value stored in a variable can change during program execution.

Example:
x = 10
Here,
x → variable name
10 → value stored in memory
---------------------------------------
Why do we use Variables?
- To store data
- To reuse values
- To make code readable and manageable
---------------------------------------
Rules for Naming Variables
1. Must start with a letter (a-z, A-Z) or underscore (_)
2. Cannot start with a number
3. Cannot use keywords (like if, else, for, etc.)
4. Case-sensitive (age and Age are different)
---------------------------------------
Examples:

# Example 1: Storing integer
a = 10
print("Value of a:", a)

# Example 2: Storing string
name = "Aquila"
print("Name:", name)

# Example 3: Multiple variables
x, y, z = 1, 2, 3
print("Values:", x, y, z)

# Example 4: Same value to multiple variables
p = q = r = 100
print("Same values:", p, q, r)
---------------------------------------
** Dynamic Typing in Python
Python allows changing the type of variable

Example:
var = 10
print("Before:", var, type(var))
var = "Hello"
print("After:", var, type(var))
---------------------------------------
** Type Checking
Use type() function
num = 25
print("Type of num:", type(num))
---------------------------------------
Type Casting
Converting one data type to another

a = "10"
b = int(a)
print("Converted to integer:", b, type(b))

---------------------------------------
Conclusion
Variables are the basic building blocks of any program.
They help store and manipulate data efficiently.

