import textwrap

def smart_collect():
    text = input('Please Enter a text: ')
    dedented_text = textwrap.dedent(text).strip()
    wrap_text = textwrap.wrap(dedented_text, width=160)
    return wrap_text



list_strings = smart_collect()
max_page = len(list_strings)
for i in range(0, max_page):
    print(f'{list_strings[i]} ({i+1}/{max_page})')
