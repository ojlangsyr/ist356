def cleanup(input:str) -> str:
    ##remove ?,.!
    ##strip white space from ends
    ##return in lowercase
    
    input=input.replace("?","")
    input=input.replace(",","")
    input=input.replace("!","")
    input=input.replace(".","")

    input=input.strip()

    input=input.lower()
    return input


message=input("please enter a message: ")
cleaned_message= cleanup(message)
print(cleaned_message)