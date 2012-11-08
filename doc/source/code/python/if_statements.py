if 2 == 3:
    print "equal"

if 2 != 3:
    print "not equal"

temperature = 3
if temperature == 0:
    print "Temperature is zero"
elif temperature < 0:
    print "Temperature is below zero"
else:
    print "Temperature is above zero"

story = {'prince': True,
         'princess': False,
         'horse_color': 'black'}
if story['prince'] and not story['horse_color'] == 'white':
    print "You need a white horse to rescue the princess."

if story['prince'] or story['princess']:
    print "We have a prince or princess, so it is a fairy tale."
