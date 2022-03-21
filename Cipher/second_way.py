message = input('Message to encode : ')

dict = {
 # do it yourself bozo
}

num = message[::-1]

for i in dict: 
    num = num.replace(i, dict[i])
    print(f"{num}bozo")