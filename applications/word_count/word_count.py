def word_count(s):
    # Your code here
    lowercase = s.lower()
    whitespace = '\n \t \r'.split(' ')
    # whitespace_to_space
    for i in whitespace:
        lowercase = lowercase.replace(i, ' ')
    chars = ' " : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(' ')
    # remove_chars
    for i in chars:
        lowercase = lowercase.replace(i, '')
    strings = lowercase.split(' ')
    seen = {}
    for string in strings:
        if string == '':
            continue
        if string in seen:
            seen[string] += 1
        else:
            seen[string] = 1

    return seen


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('a a\ra\na\ta \t\r\n'))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
