# pickle
#  pickle is a built-in Python module used for serializing and deserializing Python objects — in simple words,
# it lets you save Python data to a file and load it back later.
# Pickling: Converting a Python object into a byte stream (to save to a file or send over a network).
# import pickle

# data = {"name": "Alice", "age": 25, "marks": [85, 90, 95]}

# with open("data.pkl", "wb") as f:  # 'wb' = write binary
#     pickle.dump(data, f)

# Unpickling: Converting the byte stream back to the original Python object.
# with open("data.pkl", "rb") as f:  # 'rb' = read binary
#     loaded_data = pickle.load(f)

# print(loaded_data)
# # Output: {'name': 'Alice', 'age': 25, 'marks': [85, 90, 95]}
import pickle
data={"name": "Alice", "age": 25, "marks": [85, 90, 95]}
with open("data.pkl","wb")as file:#'wb' = write binary
    pickle.dump(data,file)
  