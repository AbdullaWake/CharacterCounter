import pprint

message = input('Enter a prompt:')


count = {} # 'r' : 12

for character in message.upper():
    count.setdefault(character, 0)
    count [character] = count[character] + 1




rjtext = pprint.pformat(count)

print(rjtext)
