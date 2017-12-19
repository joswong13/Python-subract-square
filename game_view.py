import random
import math

class Game_State:
    ''' 
    Represents the game state.
    '''
    #######################################################################
    #The following methods were not implemented: __eq__, __repr__, __str__.
    #The above methods were not implemented because this class does not 
    #contain any information to display or be called upon.
    #__init__ was not implemented in this class because this method
    #would contain nothing to initialize due to being too general.
    #__init__ was implemented in the Subtract_Square class.
    #######################################################################
    
    def player_turn(self):
        """
        (Game_State) -> Boolean

        Keeps track of turn of players
        """

        raise ('NotImplementedError')
    
    def legal_moves(self, final_number):
        """
        (Game_State) -> list of int

        Returns set of legal moves.
        """

        raise ('NotImplementedError')
    
    def game_over(self):
        """
        (Game_State) -> Boolean

        Returns if the game is over or not.
        """

        raise ('NotImplementedError')
    
    def if_player_won (self):
        """
        (Game_State) -> Boolean

        Returns if the player won or not.
        """

        raise ('NotImplementedError')
    
class Subtract_Square(Game_State):
    ''' 
    Represents the game state for the game Subtract Square
    '''
    #######################################################################
    #The following methods were not implemented: __eq__, __repr__, __str__.
    #All the information produced in this class is shown in Game_View class
    #every turn.
    #######################################################################

    def __init__ (self):
        """
        (Game_State) -> Nonetype

        Initialize random value to start subtract square game.
        
        >>> s = Subtract_Square()
        >>> s.final_number
        165
        """

        self.final_number = random.randint(100, 500)
        self.counter = 1
        self.remainder = self.final_number
        self.remaining_moves = []

    def player_turn(self):
        """
        (Game_State) -> Boolean

        Returns whose turn it is to play the game by returning a boolean
        value.
        """        
        
        #Keeps track of player turn base on boolean values.
        
        a = (self.counter % 2 == 0)
        self.counter = self.counter + 1
        return a
    
    def random_number(self):
        """
        (Game_State) -> int

        Returns generated random number.

        >>> s = Subtract_Square()
        >>> s.random_number()
        165
        """

        return self.remainder
    
    def legal_moves(self, num):
        """
        (Game_State, int) -> list of int

        Returns a set of legal moves based on the input.

        >>> s = Subtract_Square()
        >>> s.random_number()
        165
        >>> s.legal_moves(s.random_number())
        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
        """
        
        #Determines the legal moves depending on the current value of random_number.
        
        legal_answers = []
        a = 1
        b = 1
        while a <= num:
            a = b ** 2
            if a <= num:
                legal_answers.append(a)
                b = b + 1
        self.remaining_moves = legal_answers
        return legal_answers   
    
    def subtract(self, legal_input):
        """
        (Game_State, int) -> int

        Returns the subtract value if the input was chosen from a list of legal
        moves. If the number is not from the list of legal moves, will return
        a list of legal moves and prompt user to input another number.
        
        >>> s = Subtract_square
        >>> s.random_number()
        17
        >>> s.subtract(5)
        [1, 4, 9, 16]
        'Please select one of the legal moves from the list.'
        
        >>> s = Subtract_square
        >>> s.random_number()
        50
        >>> s.subtract(4)
        46
        """

        #Determines if the number chosen is legal and subtracts the current number.
        
        a = self.legal_moves(self.random_number())
        if int(legal_input) in a:
            (self.final_number) = int(self.final_number) - int(legal_input)
            self.remainder = self.final_number
            return int(self.final_number)
        else: 
            print (self.remaining_moves)
            print ('Please select one of the legal moves from the list.')
    
    def player_move(self, player_number):
        """
        (Game_State, int) -> Boolean

        Returns if the player input number is in the set of legal numbers.
        
        >>> s = Subtract_Square()
        >>> s.random_number()
        30
        >>> s.legal_moves()
        [1, 4, 9, 16, 25]
        >>> s.player_move(22)
        False
        >>> s.player_move (16)
        True
        """
        
        return int(player_number) in self.legal_moves()
    
    def game_over(self):
        """
        (Game_State) -> Boolean

        Returns if the game is over or not.

        >>> s = Subtract_Square()
        >>> s.random_number()
        0
        >>> s.game_over()
        True
        """        
        
        #Determines the winner.
        
        if self.random_number() == 0:
            if self.counter % 2 == 0:
                print ('You won!!!')
            else:
                print ('You lose!!!')
        return self.remainder == 0
    

class Strategy:
    """
    Represents the general strategy for games.
    """
    #######################################################################
    #The following methods were not implemented: __eq__, __repr__, __str__.
    #The reason being that this class contains no behaviours or any argument
    #input.
    #__init__ was not implemented in strategy.
    #######################################################################

        
    def computer_move(self):
        """
        (Strategy) -> Int/String/List

        The computer executes a move
        """

        raise ('NotImplementedError')

class Simple_Strategy (Strategy):
    '''
    Represents the strategy of randomly picking a number on the computer turn.
    '''
    #######################################################################
    #The following methods were not implemented: __eq__, __repr__, __str__.
    #The reason being that this class only has one method to choose one
    #int from the list from Subtract_Square.
    #######################################################################
    
    def __init__(self):
        """
        (Strategy) -> NoneType
        Initialize simple strategy.
        """

        self.comp_move = []
        
    
    def computer_move(self, num):
        """
        (Strategy, int) -> int

        Returns a legal number chosen from the list of legal numbers.
        
        >>> a = Subtract_Square()
        >>> b = Simple_Strategy()
        >>> a.random_number()
        30
        >>> a.legal_moves()
        [1, 4, 9, 16, 25]
        >>> b.computer_move(a.random_number())
        16
        """
        
        #Picks from sample of number from list.
        
        a = Subtract_Square().legal_moves(num)
        self.comp_move = random.sample(a, 1)
        return sum(self.comp_move)

class Game_View:
    '''
    Represents the the class that calls on subtract square game and simple strategy
    for the computer.
    '''
    #######################################################################
    #The following methods were not implemented: __eq__, __repr__, __str__.
    #The reason being that this class lists all data to the player every
    #turn, such as the current number, legal moves, and the computer 
    #turns.
    #######################################################################    
    
    def __init__(self):
        '''
        (Game_View) -> Nonetype
        
        Initialize Subtract_Square and Simple_Strategy.
        '''
        #Call on Subtract_Square and Simple_Strategy class.
        
        self.a = Subtract_Square()
        self.b = Simple_Strategy()
        
    def ask_player(self):
        '''
        (Game_View) -> Nonetype

        Ask for legal move from player and display legal moves.
        '''
        
        #Displays the current number and legal moves. 
        #Then asks for user to input a number from the legal moves list.
        #After number has been chosen from list, will subtract from current value.
        
        print ('The current number is {}.'.format(self.a.random_number()))
        print (self.a.legal_moves(self.a.random_number()))
        legal_num = input('Please select a move from the list: ')
        while legal_num.isnumeric() == False:
            print ('The current number is {}.'.format(self.a.random_number()))
            print (self.a.legal_moves(self.a.random_number()))
            legal_num = input('Please select a move from the list: ')            
        while not int(legal_num) in (self.a.legal_moves(self.a.random_number())):
            print ('The current number is {}.'.format(self.a.random_number()))
            print (self.a.legal_moves(self.a.random_number()))
            legal_num = input('Please select a move from the list: ')          
        display_num = self.a.subtract(int(legal_num))
        print ('You chose {} and the remaining number is {}.' \
                   .format(legal_num, display_num))

            
    def comp_turn(self):
        '''
        (Game_View) -> Nonetype
        
        Initialize computer strategy to play subtract square.
        '''
        
        #Computer picks number and subtracts from current value.
        
        comp_num = self.b.computer_move(self.a.random_number())
        display_num = self.a.subtract(comp_num) 
        print ('The computer chose {}. \n'
               'The remaining is {}.' \
               .format(comp_num, display_num))
        
    def main_game(self):
        '''
        (Game_View) -> Nonetype
        
        Starts the game and determines if game is over. If game is over,
        will prompt user to play again.
        '''
        #Determines if game is over, if not, runs the subtract square game.
        
        print ('How to play:')
        print ('The player whose turn it is chooses some square of a positive ' \
               'whole number (such as 1, 4, 9, 16, . . . ) to subtract from the ' \
               'value, provided the chosen square is not larger. After ' \
               'subtracting, we have a new value and the next player chooses a ' \
               'square to subtract from it.')
        print ('How to win:')
        print ('Play continues to alternate between the two players until no ' \
               'moves are possible. Whoever is about to play at that point loses.')
        
        while not self.a.random_number() == 0:
            if self.a.player_turn() == True:
                self.comp_turn()
            else:
                self.ask_player()
        if self.a.random_number() == 0:
            self.a.game_over()
        
        #After game over has been initiated, will ask player to play again.
        
        again = input('Would you like to play again? Please enter yes or no: ')
        if again == 'yes':
            self.__init__()
            self.main_game()
    
    def choose_game(self):
        '''
        (Game_View) -> Nonetype

        Asks player to input game and starts the game by calling main_game.
        '''
        
        #Asks user to input game name to play.
        #Currently only accepts one game name as input, but more games
        #will be added to the input list.
        
        game = input('Please select a game. (Eg. subtract square): ')
        while not game.lower().strip() == 'subtract square':
            game = input('Please select a game. (Eg. subtract square): ')
        self.main_game()   
                
    

if __name__ == '__main__':
    start = Game_View()
    start.choose_game()
