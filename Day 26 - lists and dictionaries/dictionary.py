# Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value} in dict.items()}
import random
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student: random.randint(1, 100) for student in names}

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}

# Create a dictionary called result that takes each word in the given sentence and
# calculates the number of letters in each word.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split() }

# Create a dictionary called weather_f that takes each temperature in degrees Celsius
# and converts it into degrees Fahrenheit.
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: temp * 9/5 + 32 for (day, temp) in weather_c.items()}

# Loop through pandas dataframe
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)

for (index, row) in student_df.iterrows():
    print(row.student)