import os
directory = './'

files = list()

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    if os.path.isfile(f):
        files.append(f)

def läs(file):
    lines = []

    for line in f:

        if len(line) < 6: continue

        new_line = line.split("\t")
        new_line[5] = new_line[5][:-2]
        lines.append(new_line)

    return lines 

contents = list()

for file in files[:-1]:

    with open(file, 'r') as f:
        contents.append(läs(f))

for content in contents[1:3]:
    total_temp_diff = 0.0

    for temp in content:
        total_temp_diff += float(temp[5]) - float(temp[3])

    medel_temp_diff = total_temp_diff / len(content)
    print(medel_temp_diff)

for content in [contents[0], contents[3]]:
    total_temp_diff = 0.0
    
    for temp in content:
        total_temp_diff += float(temp[3]) - float(temp[4])

    medel_temp_diff = total_temp_diff / len(content)
    print(medel_temp_diff)