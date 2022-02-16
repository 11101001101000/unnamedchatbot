feeling = 0
kindness = 0
end = 0
print ('안녕! 나는 이름없는 챗봇이야.\n대화를 시작하려면 아무 거나 말해 봐. 아, 들을 수는 없으니까 아무 말이나 써 봐.')
while end == 0:
    category = ''
    botmsg = ''
    usrmsg = input ('Say something: ')
    # user's messages
    # category: greeting
    if str ('안녕' in usrmsg) == 'True':
        category = category + 'greeting'
        kindness = kindness + 1
    if str ('안녕!' in usrmsg) == 'True':
        category = category + 'greeting'
        kindness = kindness + 3
    # category: stop
    if str ('가야' in usrmsg) and str ('돼' in usrmsg) == 'True':
        if str ('가야가' in usrmsg or '가야로' in usrmsg or '가야의' in usrmsg or '가야인' in usrmsg or '가야에' in usrmsg or '안돼' in usrmsg or '안 돼' in usrmsg) == 'False':
            category = category + 'stop'
            kindness = kindness + 0
    # if category is none
    if category == '':
        category = 'unknown'
        kindness = kindness - 5
        feeling = feeling - 10
    # responses
    feeling = feeling + kindness
    # category: greeting
    if str (greeting in category) == 'True':
        if feeling >= 15:
            botmsg = botmsg + '안녕' + '!' * feeling
        else:
            if feeling >= 5
                botmsg = botmsg + '안녕!!!'
            else:
                if feeling > 0
                    botmsg = botmsg + '안녕!'

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
