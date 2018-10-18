#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Description     : Unittest for the import file
# Author          : Barry Sheppard - Student Number 10387786
# Date            : 20181017
# Version         : 0.3
# Notes           : For CA4
# Python version  : 3.6.5
###############################################################################

import unittest
import pandas as pd
from import_gitlog import GitLogCommits


class TestCommits(unittest.TestCase):

    def setUp(self):
        self.GitLog = GitLogCommits('changes_python.log')

    def test_number_of_commits(self):
        self.assertEqual(422, len(self.GitLog.commits))
        self.assertEqual('Thomas', self.GitLog.commits[0].author)
        self.assertEqual('Jimmy', self.GitLog.commits[420].author)
        self.assertEqual(['FTRPC-500: Frontier Android || Inconsistencey in My Activity screen',
                         'Client used systemAttribute name="Creation-Date" instead of versionCreated as version created.'],
                         self.GitLog.commits[24].comment)
        self.assertEqual(['M /cloud/personal/client-international/android/branches/android-15.2-solutions/libs/model/src/com/biscay/client/android/model/util/sync/dv/SyncAdapter.java'],
                         self.GitLog.commits[20].changed_path)

    def test_return_as_dictionary(self):
        # Assertion that returned object is a dictionary
        self.assertTrue(isinstance(self.GitLog.commits[0].as_dict(), dict))

    def test_convert_to_dataframe(self):
        ''' Function takes in list of commit objects and returns dataframe '''
        df_commits = self.GitLog.convert_to_dataframe()
        ''' Checks that returned object is a pandas dataframe '''
        self.assertTrue(isinstance(df_commits, pd.DataFrame))


if __name__ == '__main__':
    unittest.main()
