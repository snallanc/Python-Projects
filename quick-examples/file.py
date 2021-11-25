"""
FILE handling

EXAMPLE:
Open a text file for writing and reading, add some content, reset file object's position and dump its content.
"""
import json
input="""Test file content
Line 1.
Line 2.
"""
with open('test_file1.txt', 'w+') as f:
    print("Wrote {0} bytes. File object is at position {1}.".format(f.write(input),f.tell()))
    # Reset File Object position
    f.seek(0)
    print("\nDumping the file content in text format:\n")
    for line in f:
        print(line)

"""
FILE handling with json

EXAMPLE:
Serialize and de-serialize the file data using json.
"""
with open('test_file2.txt', 'w') as f1:
    d = {1:"one", 2:"two", 3:"three"}
    # serialize the dict items into a json string
    print("\nEncoding python datatype into a json string:")
    json.dump(d, f1)

with open("test_file2.txt", 'r') as f1:
    print("\nDecoding the json string back to a python datatype:\n")
    # de-serialize back the json string to a dict
    print(json.load(f1))

