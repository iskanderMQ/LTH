# we need only to have two tables : one for the keyword 
# and the other for the logic operators because they are a subsets from the
# superset created with the regex () indentifier.
# the other cases like if the word is an operator or a separator we test it 
# by the state we are in so it only needs an if else statement
 
keywords = ["programm", "int", "var", "function", "double", "bool", "integer", "if", "then", "else", "while", "do", "begin", "end", "true", "false"]

logic_operator = ["and", "or", "not", "xor"]

# replaces your word_list: it now stores (type, text) pairs, not just words
tokens = []


# --- placeholders, to be replaced by the real versions later -------------

def send(token_type, word):
    # for now: just store the finished token
    tokens.append((token_type, word))

def error(message):
    # for now: print and stop the whole program (your "stop at first error")
    print("lexical error:", message)
    raise SystemExit


# --- the identifier state --------------------------------------------------
# In Python a function must be defined BEFORE the line that calls it runs,
# so all the state functions go above the main loop.

def state_identifier(ch, word_chars, f):
    word_chars.append(ch)             # keep the current character
    ch = f.read(1)                    # read the NEXT character

    if ch.isalnum() or ch == "_":     # still inside the word
        # call ourselves again, passing word_chars so the next call
        # remembers the letters collected so far
        return state_identifier(ch, word_chars, f)

    elif ch == "" or ch.isspace():    # EOF or whitespace = the word is complete
        word = "".join(word_chars)
        if word in keywords:
            send("keyword", word)
        elif word in logic_operator:
            send("logic_operator", word)
        else:
            send("identifier", word)

    else:                             # any other character glued to the word
        word = "".join(word_chars)
        error(f"illegal character '{ch}' after '{word}'")


# --- main loop: now only the "beginning" state_0 ---------------------------

with open("program.txt", encoding="utf-8") as f:
    while True:
        ch = f.read(1)

        if ch == "":                  # end of file: nothing left to read
            break

        elif ch.isspace():            # spaces between words: just skip them
            continue                  # "continue" = jump to the next loop turn

        elif ch.isalpha() or ch == "_":
            # first character is a letter: hand it to the identifier state,
            # starting with an EMPTY list of collected characters.
            # The state reads the rest of the word AND the space after it,
            # so when it returns we are ready for the next word.
            state_identifier(ch, [], f)

        # elif ch.isdigit():
        #     state_number(ch, [], f)     # <- your next state goes here

        else:
            # for now digits also land here, because the number state
            # does not exist yet
            error(f"unexpected character '{ch}' at the start of a word")

print(tokens)
