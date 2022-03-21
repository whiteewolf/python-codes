from cryptography.fernet import Fernet

message = input("What message should i encrypt? : ")
key = Fernet.generate_key()
fernet = Fernet(key)
encoded = fernet.encrypt(message.encode())

print(encoded)
print("Original : " + message)