import pytest

class BaaLearn:
    def test_main1(self):
        print('\ntest1')

    def test_main2(self, all_fixture, cus_fixture):
        print('\ntest2')

        print('\nparam: ' + str(cus_fixture))