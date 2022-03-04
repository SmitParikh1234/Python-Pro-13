import statistics
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("performance.csv")
score = df["reading score"].tolist();
mean = statistics.mean(score)
median = statistics.median(score)
mode = statistics.mode(score)
stdDev = statistics.stdev(score)
print("THE MEAN OF THE FOLLOWING DATA IS AS FOLLOWS :-",mean)
print("THE MEDIAN OF THE FOLLOWING DATA IS AS FOLLOWS :-",median)
print("THE MODE OF THE FOLLOWING DATA IS AS FOLLOWS :-",mode)
print("THE STANDARD DEVIATION OF THE FOLLOWING DATA IS AS FOLLOWS :-",stdDev)

fig = ff.create_distplot([score], ["Result"], show_hist=False)
fig.show();



first_std_deviation_start, first_std_deviation_end = mean-stdDev, mean+stdDev
second_std_deviation_start, second_std_deviation_end = mean-(2*stdDev), mean+(2*stdDev)
third_std_deviation_start, third_std_deviation_end = mean-(3*stdDev), mean+(3*stdDev)

list_of_data_within_1_std_deviation = [result for result in score if result > first_std_deviation_start and result < first_std_deviation_end] 
list_of_data_within_2_std_deviation = [result for result in score if result > second_std_deviation_start and result < second_std_deviation_end] 
list_of_data_within_3_std_deviation = [result for result in score if result > third_std_deviation_start and result < third_std_deviation_end]


print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(score)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(score)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(score)))



