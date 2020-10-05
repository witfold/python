def custom_string_upper(str):
    return ' '.join(custom_word_upper(s) for s in str.split())


def custom_word_upper(str):
    return str[0].upper() + str[1:]


print(custom_string_upper(input('Type words: ')))
