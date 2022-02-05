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
    # user's messages
    # category: greeting
    if str ('안녕' in usrmsg) == 'True':
        category = 'greeting'
        kindness = kindness + 1
    if str ('안녕!' in usrmsg) == 'True':
        category = 'greeting'
        kindness = kindness + 3
    # category: stop
    if str ('가야' in usrmsg) and str ('돼' in usrmsg) == 'True':
        if str ('가야가' in usrmsg or '가야로' in usrmsg or '가야의' in usrmsg or '가야인' in usrmsg or '가야에' in usrmsg or '안돼' in usrmsg or '안 돼' in usrmsg) == 'False':
            category = 'stop'
            kindness = 0
    # if category is none
    if category == 0:
        category = 'unknown'
        kindness = kindness - 5
        feeling = feeling - 10
    # responses
    feeling = feeling + kindness
    # category: greeting
    if category == 'greeting':
        if feeling > 0 and feeling < 5:
            greeting = '안녕!'
        if feeling >= 5 and feeling < 15:
            greeting = '안녕!!!'
        if feeling >= 15:
            greeting = '안녕' + '!' * feeling
    # category: stop
    if category == 'stop':
        if feeling >= 20:
            stop = '대화 재밌었어.\n잘 가!!'
        if feeling < 20 and feeling >= 0:
            stop = '알겠어.\n잘 가!'
        if feeling < 0:
            stop = '그래'
        end = 1
    # category: unknown
    if category == 'unknown':
        if feeling < 10:
            unknown = '뭐라는 거야\n난 못 알아듣겠어.'
        else:
            unknown = '무슨 말인지 잘 못 들었어.\n이해하기 쉽게 다시 말해 줄 수 있어?'
    print (str(greeting) + str(stop) + str(unknown))
    category = 0
    if fchat == 0:
        fchat = 1
