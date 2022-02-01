feeling = 0
kindness = 0
print ('Hi! I am an unnamed chatbot.')
print ('Say anything to start conversation')
usrmsg = input ('Say something: ')
if str('안녕' in usrmsg) == 'True':
    category = 'greeting'
    kindness = kindness + 1
if category == 'greeting':
    feeling = feeling + kindness
    if feeling > 0:
        botmsg = '안녕!'
print (botmsg)