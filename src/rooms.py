import csv

# Columns
# room,type,min_width,max_width,min_depth,max_depth,exists,floor,doors,window_width,window_height,objects,light_sources,activities


def load(data):
    with open(data, newline='') as csvfile:
        model_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in model_reader:
            print(row)


def sort(data):
    print(data)
