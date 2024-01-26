class CheckString:
    @staticmethod
    def is_palindrome(sequence: str, strict: bool = True, exceptions: list[str] = None) -> bool:
        """
        Check if a given sequence is a palindrome, with options for strict or flexible checking.

        A palindrome is a sequence that reads the same forwards and backwards. The function can
        perform a strict check (exact match) or a flexible check where specified characters
        (like punctuation and spaces) can be ignored.

        Parameters:
        sequence (str): The sequence to be checked. It should be a string.
        strict (bool, optional): If True, the function performs a strict palindrome check. If False,
                    the function ignores characters specified in the exceptions list or
                    a default set of characters: [",", ".", "–", "?", "!", ":", " "]
                    Default is True.
        exceptions (list[str], optional): A list of characters to ignore during the check. This parameter
                            is considered only if 'strict' is False. If 'exceptions' is None,
                            a default set of punctuation marks and spaces is ignored.
                            Default is None.

        Returns:
        bool: True if the sequence is a palindrome according to the specified mode, False otherwise.
        """

        default_exceptions = [",", ".", "–", "?", "!", ":", " "]

        if strict:
            return sequence == sequence[::-1]
        if not exceptions:
            exceptions = default_exceptions

        cleaned_sequence = ''.join(char.lower() for char in sequence if char.lower() not in exceptions)
        return cleaned_sequence == cleaned_sequence[::-1]


class CheckStrings:
    @staticmethod
    def __clean_string(input_string: str, exceptions: list[str]) -> str:
        """
        Cleans the input string by removing all characters specified in exceptions
        and converts the string to lowercase.

        This private method is used internally by the is_anagram method to prepare
        the strings for comparison if strict parameter is False.

        Parameters:
            input_string (str): The string to be cleaned.
            exceptions (list[str]): A list of characters to be removed from the string.

        Returns:
            str: A cleaned version of the input string, with all specified exceptions
            removed and converted to lowercase.

        Example:
            __clean_string("Hello, World!", [",", "!"]) -> "hello world"
        """
        return ''.join(char.lower() for char in input_string if char.lower() not in exceptions)

    @staticmethod
    def is_anagram(s1: str, s2: str, strict: bool = True, exceptions: list[str] = None) -> bool:
        """
        Determines if two strings are anagrams of each other, considering optional
        strictness and exceptions.

        In strict mode, the method compares the strings directly. In non-strict mode,
        it first cleans the strings by removing specified exceptions and converting
        to lowercase, then compares them.

        Parameters:
            s1 (str): The first string to compare.
            s2 (str): The second string to compare.
            strict (bool, optional): If True, compares the strings directly. Defaults to True.
            exceptions (list[str], optional): Characters to ignore in non-strict mode. Defaults to
                standard punctuation and whitespace.

        Returns:
            bool: True if the strings are anagrams of each other, False otherwise.

        Examples:
            is_anagram("Listen", "Silent", strict=True) -> False
            is_anagram("Listen", "Silent", strict=False) -> True
        """
        default_exceptions = [",", ".", "–", "?", "!", ":", " "]

        if strict:
            return sorted(s1) == sorted(s2)

        if not exceptions:
            exceptions = default_exceptions

        cleaned_s1 = CheckStrings.__clean_string(s1, exceptions)
        cleaned_s2 = CheckStrings.__clean_string(s2, exceptions)

        return sorted(cleaned_s1) == sorted(cleaned_s2)

print(all([True, True, True, True]) == all([True, True, True]))