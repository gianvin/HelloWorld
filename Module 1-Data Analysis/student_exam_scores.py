import pandas as pd
#Code for loading the data set
df = pd.read_csv(r"C:\Users\Gina S. Ong\Documents\byui\HelloWorld\Module 1-Data Analysis\student_exam_scores.csv")
print(df.head())

#Code for printing the entire dataframe
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None )

print(df)

#Question 1 How many students sleep 8 hours and above?

