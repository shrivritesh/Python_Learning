"""
what is scope?
--> Scope means the area of a program where a variable can be accessed.

Scope variable:
Scope of var means where we can access the variable.

2. Local Scope

A variable created inside a function has local scope.

3. Global Scope

A variable created outside a function has global scope.

nonlocal is used with nested functions when you want the inner function to modify a variable belonging to the outer function.
"""

x = 10

def test():
    x = 20
    print(x)

test() # 20
print(x) #10

# Reading Global
name = "Ritesh"

def greet():
    print(name)

greet() # Ritesh


# Global
count = 10

def update():
    global count
    count += 5

update()

print(count)

# Nested Scope
x = "Global"

def outer():
    x = "Outer"

    def inner():
        print(x)

    inner()

outer() 
# Outer

# LEGB
x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)

    inner()

outer()
# local

# x = 10

# def test():
#     print(x)
#     x = 20

# test()



x = 10

def test():
    global x
    print(x)
    x = 20

test()
print(x)