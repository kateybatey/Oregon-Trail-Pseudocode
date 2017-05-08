def get_menu_choice():
    """Print a menu and asks the user to make a choice.
    Arguments:
      None
    Returns:
      int: the user's menu choice
    """
    print '\n    You May:'
    print '    1 - Travel the trail '
    print '    2 - Learn about the trail'
    print '    3 - End'
    print '\n  '

    choice = int(raw_input('What is your choice: '))

    return choice

get_menu_choice()

def travel_the_trail():
    """Travel the trail allows the user to begin his/her journey. 
    Arguments:
        None
    Returns:
        Menu for user to choose their identity in game.
    """
    print 'Many kinds of people made the trip to Oregon.'
    print '\n    You May:'
    print '    1 - Be a banker from Boston '
    print '    2 - Be a carpenter from Ohio'
    print '    3 - Be a farmer from Illinois'
    print '\n  '

    choice = int(raw_input('What is your choice: '))

    return choice

travel_the_trail()

def learn_about_the_trail():
    """Travel the trail allows the user to begin his/her journey. 
    Arguments:
        None
    Returns:
        Information about the game and the Oregon Trail Journey
    """
    print 'Learn a little bit about Oregon Trail the game'
    print 'Try taking a journey by covered wagon across 200 miles of plains,rivers,and mountains. Try! On the plains, will you slosh your oxen through mud and water-filled ruts or will you plod through dust six inches deep?'
    print 'How will you cross the rivers? If you have money, you might take a ferry. Or you can ford the river and hope you and your wagon are not swallowed alive!'
    print 'What about supplies? Well, if you are low on food you can hunt. You might get a buffalo...you might. And there are bear in the mountains.'
    print 'If for some reason you do not survive -- your wagon burns, or theives steal your oxen, or you run out of provisions, or you die of cholera  -- do not give up! Try again..and again...'
    print '\n  '


learn_about_the_trail()