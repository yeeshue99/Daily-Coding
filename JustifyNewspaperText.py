def justifyNewspaperText(lines, aligns, width):
    newsPaper = []
    newsPaper.append("*" * (width + 2))
    # I forget how to do double var python for loop
    for i in range(len(lines)):
        CalculateNewspaper(newsPaper, lines[i], aligns[i], width)
    # Do stuff
    newsPaper.append("*" * (width + 2))
    return newsPaper


def CalculateNewspaper(newsPaper, line, align, width):
    paperLine = "*"
    rightString = []
    for word in line:
        if align == "LEFT":
            if len(paperLine) - 2 + len(word) <= width:
                paperLine += word + " "
            else:
                paperLine += " " * (width - len(paperLine) - 2)
                paperLine += "*"
                newsPaper.append(paperLine)
                paperLine = "*"
        elif align == "RIGHT":
            if len(paperLine) - 2 + len(word) + len(rightString) <= width:
                rightString.append(word)
            else:
                rightString = " ".join(rightString)
                paperLine = (
                    paperLine + " " * (width - len(paperLine) - 2) + rightString + "*"
                )
                newsPaper.append(paperLine)
                paperLine = "*"
    if align == "LEFT":
        paperLine += " " * (width - len(paperLine) - 1) + "*"
    elif align == "RIGHT":
        paperLine = (
            paperLine
            + (" " * (width - len(paperLine) - 2))
            + " ".join(rightString)
            + "*"
        )
    newsPaper.append(paperLine)


lines = [
    ["hello", "world"],
    ["How", "areYou", "doing"],
    ["Please look", "and align", "to right"],
]
aligns = ["LEFT", "RIGHT", "RIGHT"]
width = 16
temp = justifyNewspaperText(lines, aligns, width)
for i in temp:
    print(i)
