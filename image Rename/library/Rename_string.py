import re

def clean_string(input_string):
    cleaned_string = re.sub(r'[^A-Za-z0-9Ååä\s]', '', input_string)
    cleaned_string = cleaned_string.replace(' ', '_')
    cleaned_string = cleaned_string.replace('Å', 'A').replace('å', 'a').replace('ä', 'a')
    return cleaned_string


# input_str = "This is Å test Åå with special characters! Oppigårds"
# cleaned_str = clean_string(input_str)
# print(cleaned_str)
