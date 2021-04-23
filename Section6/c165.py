def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """Print a string centred, with ** either side.

    :param text: the string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and the right edges.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: if supplied string is too long to fit.
    """
    if len(text) > screen_width - 4:
        raise ValueError("String '{0}' is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)
