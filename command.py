L = []

for song in L:
    path = "./genius-lyrics-api-master/lib/dataset"
    print("node main.js "+song+" > "+path+"/"+song)