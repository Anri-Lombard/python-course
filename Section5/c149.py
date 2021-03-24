def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("EEK!!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = f"**{text.center(screen_width - 4)}**"
        print(output_string)


banner_text("*")
banner_text("This is my name")
banner_text("...ANRI...")
banner_text("And this is seriously a passionate person!")
banner_text("*")
print("Hey")
