import csv
import pandas

with open("weather_data.csv") as weather_file:
    data = csv.reader(weather_file)  # Use csv library rather than .readlines()
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)

#######################################################
## A more simpler way is to use the pandas library ##
data = pandas.read_csv("weather_data.csv")  # dataframe type
temp = data["temp"]  # series type

data_dict = data.to_dict()

temp_list = data["temp"].to_list()

average_temp = data["temp"].mean()
max_temp = data["temp"].max()
print(f"Average temperature: {average_temp}")
print(f"Maximum temperature: {max_temp}")

# Get data in column, can treat it as an object
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0] # Remember get 0 index of series
monday_temp_F = monday_temp * 9/5 + 32
print(f"Monday's temperature: {monday_temp_F}F")

students_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": ["54", "78", "82"]
}
data = pandas.DataFrame(students_dict)
data.to_csv("new_data.csv")