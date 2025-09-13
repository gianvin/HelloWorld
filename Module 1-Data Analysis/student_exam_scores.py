import pandas as pd
#Code for loading the data set
df = pd.read_csv(r"C:\Users\Gina S. Ong\Documents\byui\HelloWorld\Module 1-Data Analysis\student_exam_scores.csv")
print(df.head())

# #Code for showing all rows and columns
# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None )

# print("Full DataFRame:")
# print(df)

# #code for resetting back to defaults
# pd.reset_option("display max_rows")
# pd.reset_option("display_max_columns")



# #Code for data sets
# data= {
#     "student_id": ["S001", "S002", "S003", "S004", "S005", "S006"],
#     "exam_score": [47.9, 38.3, 25.0, 30.2, 48.6, 34.0,],
#     "sleep_hours":[8.0, 7.5, 8.2, 6.8, 9.0, 7.2],
#     "previous_scores": [45, 86, 71, 66, 34, 42],
   
# }
# df =pd.DataFrame(data)

# #Question 1 How many students sleep 8 hours and above?

# count_8_plus = (df["sleep_hours"] >= 8.0).sum()
# print("Number of students with 8 hours or more:", count_8_plus)

# #code for selecting the student with the highest exam score
# highest_exam_score_student = df.loc[df["exam_score"].idxmax()]
# #code for printing the student id and the score
# student_id = highest_exam_score_student["student_id"]
# score = highest_exam_score_student["exam_score"]
# print("ID:", student_id)
# print("Score:", score)
# #Question 2 What is the average sleep hours of the students?
# average_sleepHours= df["sleep_hours"].mean()
# print("Average sleep hours of students:", average_sleepHours)

# #Question 3 What is the sum of the previous scores of the students
# total_score = df["previous_scores"].sum()
# print("Total of all previous scores:", total_score)
# #Question 4