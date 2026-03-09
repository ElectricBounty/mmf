# define filename
from datetime import datetime

file_name = "write_test"
formatted_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
write_to  = "{}_{}.txt".format(file_name, formatted_time)

text_file = open(write_to, "w+")

# things to write to our file
heading = "// This is a header! //"
content = "hello world"
foo = "bar"

# list of strings
to_write = [heading, content, foo]

# print to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")