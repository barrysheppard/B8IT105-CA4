# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # Description     : This is the main file for the program
# # Author          : Barry Sheppard - Student Number 10387786
# # Date            : 20181018
# # Version         : 0.3
# # Notes           : For CA4
# # Python version  : 3.6.5
# ###############################################################################

from import_gitlog import GitLogCommits
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from heatmap import custom_heatmap # To display time series data as a heatmap

# Create a GitlogCommits object
# open the file - and read all of the lines.
commits = GitLogCommits('changes_python.log')
# Change the commits to a dataframe
df_commits = commits.convert_to_dataframe()
# Save as csv to check
commits.save_as_csv('gitlog.csv')

# Print a single row
# print(df_commits.iloc[2])

# # Get the sum of the deletes per user
# print('The total number of Deletes per User')
# print(df_commits.groupby('Author')['Deleted'].sum())
#
# # Get the sum of the adds per user
# print('The total number of Added per User')
# print(df_commits.groupby('Author')['Added'].sum())
#
# # Get the sum of the modifed per user
# print('The total number of Modifications per User')
# print(df_commits.groupby('Author')['Modified'].sum())

# Plot with Seaborn
# ax = sns.countplot(x="Author", data=df_commits)
# plt.show()

# # Check when the first date and last commit dates were
# print(df_commits['Date'].min())
# print(df_commits['Date'].max())
#
#
#
# Print a plot for every author

# for i in range(10):
#     plt.figure(i+1) #to let the index start at 1
#     plt.plot(t, signal())
# plt.show()

i = 1
authors = df_commits['Author'].unique()
for author in authors:
    custom_heatmap(df_commits, author)
    plt.show()

# custom_heatmap(df_commits)
# plt.show()


# author = 'Vincent'
# df_filtered = df_commits.query('Author=="%s"'% (author))
# df_heatmap = df_filtered.set_index('Date').groupby(pd.Grouper(freq='D'))['Added'].count()
# df_heatmap.plot()
#
# author = 'Thomas'
# df_filtered = df_commits.query('Author=="%s"'% (author))
# df_heatmap = df_filtered.set_index('Date').groupby(pd.Grouper(freq='D'))['Added'].count()
# df_heatmap.plot()
#
# # Show
# plt.show()
