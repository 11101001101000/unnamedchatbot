feeling = 0
kindness = 0
end = 0
fchat = 0
category = 0
greeting = ''
stop = ''
unknown = ''
while end == 0:
    if fchat == 0:
        # greeting
        print ('안녕! 나는 이름없는 챗봇이야.')
        print ('대화를 시작하려면 아무 거나 말해 봐. 아, 들을 수는 없으니까 아무 말이나 써 봐.')
    usrmsg = input ('Say something: ')
    if str ('' in usrmsg) == 'True':
        kindness = kindness
        feeling = feeling + kindness
        print ('')