import os
import sentry_sdk


sentry_sdk.init(
    dsn="https://4934ef3d630239bc7eede2e8fe38f06d@o4511281230577664.ingest.de.sentry.io/4511325632594000",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

def is_palindrome(text: str) -> bool:
    # doctests
    """
    Перевіряє, чи є переданий рядок паліндромом.
    Ігнорує пробіли, розділові знаки та регістр.
    
    >>> is_palindrome("А роза упала на лапу Азора")
    True
    >>> is_palindrome("Hello World")
    False
    >>> is_palindrome("12321")
    True
    """
    if not text or not text.strip():
        raise ValueError("Помилка: Текст не може бути порожнім!")

    # Очищуємо рядок та зводимо до нижнього регістру
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Якщо після очищення рядок порожній 
    if not cleaned_text:
        raise ValueError("Помилка: Текст не містить букв або цифр для перевірки!")

    return cleaned_text == cleaned_text[::-1]

def main():
    try:
        user_input = input("Введіть текст для перевірки на паліндром: ")
        if is_palindrome(user_input):
            print("Результат: Це паліндром!")
        else:
            print("Результат: Це не паліндром.")
    except ValueError as e:
        print(e)
        sentry_sdk.capture_exception(e) # Відправляємо помилку в Sentry
    except Exception as e:
        print("Сталася непередбачена помилка.")
        sentry_sdk.capture_exception(e)

if __name__ == "__main__":
    main()