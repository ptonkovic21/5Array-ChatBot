from rag import ask


print('\n\n\n')
print("5Array: " + "Hello, my name is 5Array and I'm here to help you. Ask me anything you want!")
print('\n')

while True:
    prompt = input("User: ")
    
    if prompt.strip().lower() == "/exit" or prompt.strip().lower() == "/quit" or prompt.strip().lower() == 'bye':
        print("5Array: Goodbye!")
        break
    
    print("\n5Array: " + ask(prompt) + "\n")
