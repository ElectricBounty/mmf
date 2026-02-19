import pandas

# test

all_names = ["rat","cat","dog","stoat","possum"]

movie_dict = {
    "Name": all_names
}

frame = pandas.DataFrame(movie_dict)

print(frame)

print(movie_dict["Name"])