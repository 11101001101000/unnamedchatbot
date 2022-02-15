end = 0
feeling = 0
kindness = 0
botmsgsrc = '안녕!가야 돼?잘가!그래'
print ('')
while end == 0:
    botmsg = ''
    usrmsg = input ('say something. write(don\'t \'say\'): ')
    if str ('안녕' in usrmsg) == 'True':
        kindness = kindness + feeling / 2 + 1
        feeling = feeling + kindness
        botmsg = botmsg + botmsgsrc[1]
