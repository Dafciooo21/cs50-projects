def convert():
    new_text = text.replace(":)","🙂").replace(":(","🙁")
    print(new_text)

text = input("Provide some text: ")
convert()
