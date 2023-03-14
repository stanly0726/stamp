import sys
import imgkit

title = sys.argv[1]
name = sys.argv[2]
date = sys.argv[3]
date = date[:4] + "<br>" + date[4:]

with open("template.html", "r") as file:
    template = file.read()

css = "css.css"

options = {
    "format": "png",
    "transparent": "",}
# imgkit.from_file('test.html','output.png', options=options)
imgkit.from_string(
    template.format(title=title, name=name, date=date),
    "output.png",
    options=options,
    css=css,
)
