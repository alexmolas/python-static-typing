def headline(text, align=True):
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


x = headline("Hello World", align=True)
print(x)

x = headline("Hello World", align=False)
print(x)

x = headline("Hello World", "center")
print(x)

x = headline(1, align=False)
print(x)
