# A simple compiler for pascal language 
# we need only to have two tables : one for the keyword 
# and the other for the logic operators because they are a subsets from the
# superset created with the regex () indentifier.
# the other cases like if the word is an operator or a separator we test it 
# by the state we are in so it only needs an if else statement

# macros
keywords = ["programm",
            "var",
            "function",
            "double",
            "bool",
            "integer",
            "if",
            "then",
            "else",
            "while",
            "do",
            "begin",
            "end",
            "true",
            "false"]

logic_operator = ["and",
                  "or",
                  "not",
                  "xor"]
# gloabas
tokens = []

# definitions
def send(token_type, word):
    tokens.append(token_type, word) 

def error(message):
    # later todo : find a way to manipulate errors using this one function
    print("lexical error:", message)
    raise SystemExit

def state_identifier(ch, word_chars, f):
    word_chars.append(ch)
    ch = f.read(1)

    if ch.isalnum() or ch == "_":
         return state_identifier(ch, word_chars, f)

    if ch == "" or ch.isspace():
        word = "".join(word_chars)

        if word in keywords:
            send("keyword", word)
        elif word in logic_operator:
            send("indentifier", word)

        else:
            send("indentifier", word)

    else:
        word = "".join(word_chars)
        error(f"illegal character '{ch}' after '{word}'")

# main    

with open("program.txt", encoding="utf-8") as f:
    while True:
        ch = f.read(1)

        if ch == "":
            break
        elif ch.isspace():
            continue

        elif ch.isalpha() or ch == "_":
            state_identifier(ch, [], f)

        # elif condition 
        #     state_X

        else: 
            error(f"unexpected character '{ch}'")

print(tokens) 

            


           
