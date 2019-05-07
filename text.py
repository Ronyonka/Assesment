import textwrap  # importing the textwrap module which is used in wrapping and formatting of plain text

def text_display():
    value = input('Please Enter a text: ')
    dedented = textwrap.dedent(value).strip() # dedent is used to remove any common leading whitespace from every line in the input text.
    wrapped = textwrap.wrap(dedented, width=160) # wrap function wraps the input paragraph such that each line in the paragraph is at most 160 characters long.
    return wrapped # returns a value once the function is carried out

lists = text_display() # assigns the returned value from the text_display function a variable to be stored in for simple refrence
pages = len(lists)  # calculates the number of pages
for i in range(0, pages):
    print("") # empty line for aesthetic
    print(f'{lists[i]} ({i+1}/{pages})') # displays the information/texts
