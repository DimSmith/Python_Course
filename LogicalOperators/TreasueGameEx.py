print(''''
         __..--.                                   _.._
    _..--''_______|-._____  ______________________|``  __``--.._
   '-.-..---..---..---..--''.---..---..---..---..---..---..---.-'
     |_::___::___::___::___::___::___::___::___::___::___::___|
     |________________________________________________________|
     '.--.':'.--.' '.--.'  '.--.'  '.--.'  '.--.' '.--.' '.--.'
      |''|.|.|''|-. |''|    |''|    |''|    |''|   |''|.|.|''|
      |''|.| |''| | |''|    |''|    |''|    |''|   |''| |.|''|
      |''|.|.|''| | |''|    |''|    |''|    |''| _,|''|.|.|''|
      |''|.| |''|.| |''|    |''|    |''|    |''|/ .|''| |.|''|
      |''|.|.|''| |_|''|`.__|''|,--'|''|``-.|''|   |''|.|.|''|
      |''|.| |''| |.|''| |  |''|  __|''|   ||''|.  |''| |.|''|
      |''|.|.|''| | |''| |  |''| |  |''|   ||''|   |''|.|.|''|
      |''|.| |''|.| |''| |  |''| |  |''|   ||''|  .|''| |.|''|
      |''|.|.|''| | |''| |__|''|_|__|''|___||''|   |''|.|.|''|
      |''|_|_|__| |.|''|'   |''|    |''|    |''|-._|''| |.|''|
      |'/  )| | ||  |''|    |''|    |''|    |''|   |''|'|.|''|
    .-'|`-' | | ||--''''----''''----''''----''''---''''---''''-.
  .'---|| | | |,''--.,-------------------.----------------------'.
 '-----|| | | /  - - - - - - - - ,---. -  /
               `--------------'--`-------'
''')
print("Welcome To Necropolis")
print("Your mission is to find the escape")
answer1 = input('Your just get up from amnesia in front of you two doors.'
                'Which You will be choose.?'
                'Type "left" or "right"').lower()
if answer1 == "left":
    answer2 = input('Your come to The Pool Of Death.'
                    'You need to get to the side other side.'
                    'Type "wait" to wait for a boat.'
                    'Type "swim to try to swim across.').lower()
    if answer2 == "wait":
        answer3 = input('The you took the boat and you on the other this of the pool.'
                        'In front of you standing giant skeleton guardian'
                        'He hands you three gems of different colors'
                        ' "You can choose only one" he said.'
                        ' "Choose Wisely!!! '
                        'For choose type : "red" or "blue" or "yellow".').lower()
        if answer3 == "red":
            print('The skeleton started to laugh loudly and said:'
                  'You chose Wrong!,'
                  'The stone become to fire and brun you to death.'
                  'Game Over')
        elif answer3 == "blue":
            print('The skeleton started to laugh loudly and said:'
                  'You chose Wrong!,'
                  'The stone become to ice and froze you to death.'
                  'Game Over')
        elif answer3 == "yellow":
            print('The stone began to emit a strong and bright light.'
                  'You teleported to your home.'
                  'You win!')
        else:
            print('The skeleton started to laugh loudly and said:'
                  'You chose Wrong!,'
                  'He crushed you with his leg'
                  'Game Over')
    else:
        print('Your soul was taken by the dead.'
              'Game Over.')
else:
    print('You fell in to Endless Hole.'
          'Game Over')
