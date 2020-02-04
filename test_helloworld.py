'''
This is the testing module for helloworld.py
'''
import helloworld

def test_answer():
    '''
    test for helloworld.py
    '''
    assert helloworld.func(3) == 5
