# we need only to have two tables : one for the keyword 
# and the other for the logic operators because they are a subsets from the
# superset created with the regex () indentifier.
# the other cases like if the word is an operator or a separator we test it 
# by the state we are in so it only needs an if else statement
 
keywords = ["programm", "var", "function", "double", "bool", "integer", "if", "then", "else", "while", "do", "begin", "end", "true", "false"]

logic_operator = ["and", "or", "not", "xor"]

word_chars = []
word_list = []

with open("program.txt", encoding="utf-8") as f:
    while True:
        ch = f.read(1)
        if ch == "" or ch.isspace():
            if word_chars:
                word = "".join(word_chars)
                word_list.append(word)
                word_chars = []

            #don't break till the EOF
            if ch == "":
                break
        else:
            word_chars.append(ch)

print(word_list)


 
            
