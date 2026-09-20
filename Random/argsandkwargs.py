# *args  = collects any number of POSITIONAL arguments
#          and stores them as a TUPLE
#
# **kwargs = collects any number of KEYWORD arguments
#            and stores them as a DICTIONARY



def student_info(*args, **kwargs):

    # *args collects normal/positional values
    # Example: "Math", "Python", "OOP"
    print("ARGS:", args)

    # **kwargs collects key=value arguments
    # Example: name="Amrit", age=19
    print("KWARGS:", kwargs)


# Calling the function
student_info(
    "Math",          # positional argument → *args
    "Python",        # positional argument → *args
    "OOP",           # positional argument → *args

    name="Amrit",    # keyword argument → **kwargs
    age=19,          # keyword argument → **kwargs
    branch="CSE"     # keyword argument → **kwargs
)


# OUTPUT:
#
# ARGS: ('Math', 'Python', 'OOP')
#
# KWARGS: {
#     'name': 'Amrit',
#     'age': 19,
#     'branch': 'CSE'
# }
#
# Remember:
# *args   → positional arguments → TUPLE
# **kwargs → keyword arguments → DICTIONARY


# They’re special keywords in Python used in function definitions to 
# accept a flexible number of arguments
# Now you always don’t have to use Args and Kwargs the main 
# thing is * , ** you can use any names in front of them.
# so *args are used for multiple positional arguments, and **kwargs 
# are used for multiple key word arguments.
# And the *args becomes a tuple and **kwargs becomes a 
# dictionary
# The use case is grea
# You don’t need to know how many inputs you'll get
# Helps in building flexible functions, decorators, APIs, and 
# more.