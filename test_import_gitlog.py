#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Description     : Unittest for the import file
# Author          : Barry Sheppard - Student Number 10387786
# Date            : 20181017
# Version         : 0.2
# Notes           : For CA4
# Python version  : 3.6.5
###############################################################################

import unittest
import pandas as pd
from import_gitlog import get_commits, read_file, convert_to_dataframe


class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.log')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))
        self.assertEqual('Thomas', commits[0].author)
        self.assertEqual('Jimmy', commits[420].author)
        self.assertEqual(['FTRPC-500: Frontier Android || Inconsistencey in My Activity screen',
                         'Client used systemAttribute name="Creation-Date" instead of versionCreated as version created.'],
                         commits[24].comment)
        self.assertEqual(['M /cloud/personal/client-international/android/branches/android-15.2-solutions/libs/model/src/com/biscay/client/android/model/util/sync/dv/SyncAdapter.java'],
                         commits[20].changed_path)

    def test_return_as_dictionary(self):
        ''' Commit class objects can return varabiles as dictionary object '''
        commits = get_commits(self.data)
        # Assertion that returned object is a dictionary
        self.assertTrue(isinstance(commits[0].as_dict(), dict))

    def test_convert_to_dataframe(self):
        ''' Function takes in list of commit objects and returns dataframe '''
        commits = get_commits(self.data)
        df_commits = convert_to_dataframe(commits)
        ''' Checks that returned object is a pandas dataframe '''
        self.assertTrue(isinstance(df_commits, pd.DataFrame))


if __name__ == '__main__':
    unittest.main()
