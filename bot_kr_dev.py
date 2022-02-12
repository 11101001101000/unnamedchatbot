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
        fchat = 1
    usrmsg = input ('Say something: ')
    # Use the code below to add message(s)
    # if str ('' in usrmsg) == 'True':
    #     kindness = kindness
    #     feeling = feeling + kindness
    #     print ('')
    #
    # message: greeting
    if str ('안녕' in usrmsg) == 'True':
        if str ('안녕!' in usrmsg) == 'True':
            kindness = kindness + 3
            print ('안녕!!!')
        else:
            kindness = kindness + 1
            feeling = feeling + kindness
            if feeling >= 0:
                print ('안녕!')
            else:
                print ('어 그래')
    # message: quit
    if str ('가야' in usrmsg and '돼' in usrmsg) == 'True':
        if feeling > 0:
            quit = input ('진짜 가야 돼? ')
            if str ('어' in quit or '응' in quit or '맞아' in quit) == 'True':
                print ('대화 재밌었어. 잘 가!')
                end = 1
                exit()
        else:
            print ('그래')
            end = 1
            exit()
