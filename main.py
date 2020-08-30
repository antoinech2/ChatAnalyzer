import datetime


input_file = open("input.csv", "r")
output_file = open("output.txt", "w")
data = input_file.readlines()
separator = '","'

text = ""
for line in data:
    text += line
    if text[-4:] == '"";\n':
        try:
            clusters = text.split(separator)
            #print(clusters)
            #name = clusters[0].split(",")
            date = clusters[1]
            print(text)
            time_object = datetime.datetime.strptime(date, '"%d-%b-%y %I:%M %p"')
            time = time_object.strftime("%d.%M.%y, %H:%M:00")
            output_file.write("{}: {}: {}\n".format(time, clusters[0], clusters[2]))
        except:
            continue
        text = ""
    else:
        text = text[:-2]
