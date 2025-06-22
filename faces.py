def convert(str):
    str= str.replace(":)", "🙂")
    str= str.replace(":(", "🙁")
    return str

def main():
    user_input=input()
    print(convert(user_input))

if __name__== "__main__":
    main()

