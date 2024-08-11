import csv

# CSV Files
file_list = ['temp1.csv', 'temp2.csv', 'temp3.csv']

def map_files(input_files: list):
    mapped_data = []
    for file in input_files:
        with open(file, "r") as temperature_file:
            reader = csv.reader(temperature_file)
            next(reader)
            for line in reader:
                if len(line) == 2:
                    city, temp = line
                    city = city.strip()
                    temp = temp.strip()
                    try:
                        temp = int(temp)
                        mapped_data.append((city, temp))
                    except ValueError:
                        continue
    return mapped_data

def reduce(mapped_file):
    reduced_data = {}
    output = 'highest_temperature.csv'
    with open(output, 'w', newline='') as highest_file:
      writer = csv.writer(highest_file)
      writer.writerow(["City", "Temperature"])
      for city, temp in mapped_file:
          if city in reduced_data:
              if reduced_data[city] < temp:
                reduced_data[city] = temp
          else:
              reduced_data[city] = temp
      for city, temp in reduced_data.items():
          writer.writerow([city, temp])
    return reduced_data


mapped_data = map_files(file_list)
highest_temp = reduce(mapped_data)
print(highest_temp)
