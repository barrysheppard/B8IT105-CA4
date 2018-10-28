#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Description     : Importing the Git log file
# Author          : Barry Sheppard - Student Number 10387786
# Date            : 20181018
# Version         : 0.3
# Notes           : For CA4
# Python version  : 3.6.5
###############################################################################

import pandas as pd


class Commit(object):
    ''' Used to store git commit logs'''
    def __init__(self, revision, author, date, num_of_lines,
                 changed_path=[], changed_files=[], comment=[]):
        self.revision = revision
        self.author = author
        self.date = date
        self.num_of_lines = num_of_lines
        self.changed_path = changed_path
        self.changed_files = changed_files
        self.comment = comment
        self.modified = 0
        self.added = 0
        self.deleted = 0

    def __repr__(self):
        return self.revision + ',' + self.author + \
            ',' + self.date + ',' + \
            str(self.num_of_lines) + \
            ',' + ' '.join(self.comment) + '\n'

    def as_dict(self):
        ''' This function returns the object as a dictionary'''
        return {'Revision': self.revision,
                'Author': self.author,
                'Date': self.date,
                'Number of Lines': self.num_of_lines,
                'Comment': self.comment,
                'Changed Path': self.changed_path,
                'Changed Files': self.changed_files,
                'Added': self.added,
                'Modified': self.modified,
                'Deleted': self.deleted
                }


class GitLogCommits(object):
    ''' Used to store a full git log '''

    def __init__(self, git_file_name):
        # Read the file in and convert to a list of commit objects
        self.commits = self.__get_commits(self.__read_file(git_file_name))

    def __get_commits(self, data):
        ''' Parses a git commit log into a list of individual commits'''
        # Each commit starts with a line of 72 dashes
        sep = 72*'-'
        # Make a blank commit list to start storing them into
        commits = []
        # While loop will start at 0 and go through the data list
        index = 0
        while index < len(data):
            try:
                # parse each of the commits and put them into a list of commits
                details = data[index + 1].split('|')
                # Handle the date a little better, we want the first two parts
                # for the date time. Example format is below
                # 2015-07-15 13:48:45 +0100 (Wed, 15 Jul 2015)
                # This changes it into
                # 2015-07-15 13:48:45
                date = details[2].strip().split(' ')[0] + ' ' + \
                    details[2].strip().split(' ')[1]
                num_of_lines = int(details[3].strip().split(' ')[0])
                # create Commit object
                commit = Commit(revision=details[0].strip(),
                                author=details[1].strip(),
                                date=date,
                                num_of_lines=num_of_lines)
                # Update the index based on the lines
                change_file_end_index = data.index('', index + 1)
                # change_path and comment both include multiple lines into one
                commit.changed_path = data[index + 3: change_file_end_index]
                commit.comment = data[change_file_end_index + 1:
                                      change_file_end_index + 1 +
                                      commit.num_of_lines]
                # Work out the number of files Added, Modified, and Deleted
                for path in commit.changed_path:
                    path = path.split(' ')
                    if path[0] == 'M':
                        commit.modified += 1
                    if path[0] == 'A':
                        commit.added += 1
                    if path[0] == 'D':
                        commit.deleted += 1
                # Work out the file names split it up based on / and then
                # take the last item [-1] which should be the file name
                for path in commit.changed_path:
                    path = path.split('/')
                    file_name = path[-1]
                    commit.changed_files.append(file_name)
                # add details of the commit to the list of commits
                commits.append(commit)
                index = data.index(sep, index + 1)
            except IndexError:
                index = len(data)
        # object returned is a list of Commit objects
        return commits

    def __read_file(self, any_file):
        ''' Opens file returns text contents as list of trimmed text'''
        # Open file in read online mode
        input_file = open(any_file, 'r')
        # use strip to remove spaces and trim the line
        data = [line.strip() for line in input_file]
        # Close the file to avoid memory issues
        input_file.close()
        # return the data from the file
        return data

    def save_as_csv(self, file_name):
        ''' Saves list into a csv file '''
        # Create Pandas object
        df_to_save = self.convert_to_dataframe()
        # Paths and Files are too big for CSV and as such are dropped
        df_to_save = df_to_save.drop(columns=['Changed Path', 'Changed Files'])
        # Save the data frame as csv file
        df_to_save.to_csv(file_name)

    def convert_to_dataframe(self):
        ''' Takes in a list of commits and returns a dataframe object '''
        df = pd.DataFrame([x.as_dict() for x in self.commits])
        # The date field is still in a text format, we want to change that to
        # a datetime format that pandas will recognise
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')
        return df
