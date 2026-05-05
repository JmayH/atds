__author__ = "Jamie Hsieh"
__version__ = "02/17/26"
import atds
strict_mode = False
def set_strict_mode(option):
    global strict_mode
    if option==True:
        strict_mode = True
    if option==False:
        strict_mode = False
def sanitize(phrase):
    sanitized = ""
    for letter in phrase:
        if letter == " " or letter == "!" or letter == "?" or letter == "." or letter == "@" or letter == "#" or letter == ",":
            pass
        else:
            sanitized += letter
    sanitized = sanitized.lower()
    return sanitized
def is_palindrome(phrase):
    letters = atds.Deque()
    if strict_mode == False:
        phrase = sanitize(phrase)
    for letter in phrase:
        letters.add_rear(letter)
    while letters.size() > 1:
        first = letters.remove_front
        last = letters.remove_rear
        if first != last:
            return False
    return True
def main():
    print("Palindrome Checker!")
    strictmode = input("Do you want strict mode 1) on, or 2) off? --> ")
    if strictmode == "1":
        set_strict_mode(True)
    elif strictmode == "2":
        set_strict_mode(False)
    else:
        print("That was not an option. Goodbye.")
        return
    phrase = input("Phrase: ")
    if is_palindrome(phrase) == True:
        print ("Is a palindrome.")
    else:
        print("Not a palindrome.")
        
if __name__ == "__main__":
    main()