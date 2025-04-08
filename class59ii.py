import os
import pickle
with open("data.pkl","rb") as file:
    loaded_data=pickle.load(file)#'rb' = read binary
    print(loaded_data)