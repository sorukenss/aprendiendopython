
#cilos - loops

# while - mientras Q

count = 0
while count < 5:
    print(count)
    count += 1
#prints from 0 to 4

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# for- para
language = 'Python'
for letter in language:
    print(letter)


# for i in range(len(language)):
#     print(language[i])