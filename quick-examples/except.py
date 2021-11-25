"""
Exception handling

EXAMPLE:
"""

try:
    filename = "test_file.txt"
    f = None
    f = open(filename, "r")
except FileNotFoundError as e: # This executes only when an exception is thrown by try block
    print("File {0} doesn't exist!".format(filename))
else: # This executes only when no exceptions are thrown by try block
    print("File {0} exists".format(filename))
finally: # This executes in all cases before try block execution completes
    if f:
        print("Closing file {0}".format(filename))
        f.close()