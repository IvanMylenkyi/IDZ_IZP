import pytest
from main import is_palindrome

def test_is_palindrome_true():
    assert is_palindrome("А роза упала на лапу Азора") is True
    assert is_palindrome("Radar") is True
    assert is_palindrome("12321") is True

def test_is_palindrome_false():
    assert is_palindrome("Python") is False
    assert is_palindrome("12345") is False

def test_is_palindrome_empty_raises_error():
    with pytest.raises(ValueError, match="Текст не може бути порожнім!"):
        is_palindrome("")
        
    with pytest.raises(ValueError, match="Текст не може бути порожнім!"):
        is_palindrome("   ")

def test_is_palindrome_no_alphanum_raises_error():
    with pytest.raises(ValueError, match="Текст не містить букв або цифр для перевірки!"):
        is_palindrome("!!! ???")