def greeting_user(name = "User"):
    return "Hello, " + name + " !!"

print(greeting_user("Alice")) # Output: Hello, Alice !!
print(greeting_user())        # Output: Hello, User !!