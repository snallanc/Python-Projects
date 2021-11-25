"""
Namespace:
Deals with object scoping. There are 4 levels of scoping.
1. Local scope
2. Functional scope
3. Global/module level scope
4. Builtins scope

EXAMPLE:
"""

def name_test():
    def local_():
        name = "local"     # Innermost/local scope -the value doesn't persist beyond this scope

    def nonlocal_():
        nonlocal name
        name = "nonlocal"  # Functional scope - the value persists beyond this scope

    def global_():
        global name
        name = "global"    # Global scope - the value persists beyond the functional scope within the module

    name = "unassigned"
    local_()
    print(name) # unassigned
    nonlocal_()
    print(name) # nonlocal
    global_()
    print(name) # nonlocal

name_test()
print(name) # global