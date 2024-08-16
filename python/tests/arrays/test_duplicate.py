import pytest
from src.array_hashing.ContainsDuplicate import ContainsDuplicate

def test_correct_result():
    data_test = [1, 2, 3, 3]
    checker_duplicate = ContainsDuplicate()
    result = checker_duplicate.hasDuplicate(data_test)
    
    assert result == True