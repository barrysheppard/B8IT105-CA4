# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # Description     : This is the main file for the program
# # Author          : Barry Sheppard - Student Number 10387786
# # Date            : 20181017
# # Version         : 0.1
# # Notes           : For CA4
# # Python version  : 3.6.5
# ###############################################################################

from import_gitlog import get_commits, read_file, convert_to_dataframe

# open the file - and read all of the lines.
changes_file = 'changes_python.log'
data = read_file(changes_file)
# Change the lines to commit objects
commits = get_commits(data)
# Change the commits to a dataframe
df_commits = convert_to_dataframe(commits)


# Print a single row
# print(df_commits.iloc[2])

# Get the sum of the deletes per user
print('The total number of Deletes per User')
print(df_commits.groupby('Author')['Deleted'].sum())

# Get the sum of the adds per user
print('The total number of Added per User')
print(df_commits.groupby('Author')['Added'].sum())

# Get the sum of the modifed per user
print('The total number of Modifications per User')
print(df_commits.groupby('Author')['Modified'].sum())
