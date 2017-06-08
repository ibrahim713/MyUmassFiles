def golfsucks():
    data = input('How many players to add??: ',)
    file = open('golf.txt', 'w')
    for i in range(1, data + 1):
       print 'Enter player', i, '\'s name: ',
       name = raw_input()
       print 'Enter player', i, '\'s score: ',
       score = raw_input()
       file.write(name)
       file.write('\n')
       file.write(score)
       file.write('\n')
golfsucks()
