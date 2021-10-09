import pandas as pd
import csv
import statistics

df = pd.read_csv('kaggle.html')
thin1_list = df[''].to_list()
thin2_list = df[''].to_list()
thin3_list = df[''].to_list()

thin1_mean = statistics.mean(thin1_list)
thin2_mean = statistics.mean(thin2_list)
thin3_mean = statistics.mean(thin3_list)

thin1_median = statistics.median(thin1_list)
thin2_median = statistics.median(thin2_list)
thin3_mean = statistics.mean(thin3_list)

thin1_mode = statistics.mode(thin1_list)
thin2_mode = statistics.mode(thin1_list)
thin3_mean = statistics.mean(thin3_list)

thin1_std_div = statistics.stdev(thin1_list)
thin2_std_div = statistics.stdev(thin2_list)
thin3_std_div = statistics.stdev(thin3_list)

thin1_stdev_start,thin1_first_stdev_end = thin1_mean - thin1_std_div,thin1_mean + thin1_std_div
thin1_first = [result for result in thin1_list if(result > thin1_stdev_start and result < thin1_first_stdev_end)]
percent = len(thin1_first)*100/len(thin1_list)
print(percent)

thin2_first_stdev_start,thin2_first_stdev_end = thin2_mean - thin2_std_div,thin2_mean + thin2_std_div
thin2_first = [result for result in thin2_list if(result > thin2_first_stdev_start and result < thin2_first_stdev_end)]
percent2 = len(thin2_first)*100/len(thin2_list)
print(percent2)

thin3_second_stdev_start,thin3_second_stdev_end = thin3_mean - (2*thin3_std_div),thin3_mean + (2*thin3_std_div)
thin3_second = [result for result in thin3_list if(result > thin3_second_stdev_start and result < thin3_second_stdev_end)]
percent3 = len(thin3_second)*100/len(thin3_list)
print(percent3)

