class Actions:
    def __init__(self):
        self.player1Input = ''
        self.player2Input = ''
        self.valueList = [0, 0 ,0 , 0, 0, 0, 0, 0, 0]
        self.ticTacToe = f"""  
          A B C 
        A {self.valueList[0]} {self.valueList[1]} {self.valueList[2]} 
        B {self.valueList[3]} {self.valueList[4]} {self.valueList[5]}  
        C {self.valueList[6]} {self.valueList[7]} {self.valueList[8]}"""
        self.winnerExist = True

        
    def printMenu(self):
        print("Please select the option where you want to type")
        print(self.ticTacToe)
    
    def validateInputs(self, inputPlayer1, inputPlayer2):
        positions = {
            'aa': 0,
            'ab': 1,
            'ac': 2,
            'ba': 3,
            'bb': 4,
            'bc': 5,
            'ca': 6,
            'cb': 7,
            'cc': 8
        }
        if inputPlayer1 == inputPlayer2:
            print("Players cannot have the same input, please choose again")
        elif inputPlayer1 != inputPlayer2:
            for inputPlayer, marker in [(inputPlayer1, 'X'), (inputPlayer2, 'Y')]:
                position = positions.get(str(inputPlayer).lower())
                if position is not None:
                    self.valueList[position] = marker
            self.setMenu(self.valueList)
            self.checkWinner(self.valueList)
        else:
            self.setWinnerExist(False)
    
    def check_horizontal(valueList, symbol):
        for i in range(0, len(valueList), 3):
            if valueList[i:i+3] == [symbol] * 3:
                return True
        return False

    def check_vertical(valueList, symbol):
        for i in range(3):
            if valueList[i] == valueList[i+3] == valueList[i+6] == symbol:
                return True
        return False

    def check_diagonal(valueList, symbol):
        if valueList[0] == valueList[4] == valueList[8] == symbol:
            return True
        if valueList[2] == valueList[4] == valueList[6] == symbol:
            return True
        return False
            
    def checkWinner(self, valueList):
        pass

    def setMenu(self, updatedList):
        self.ticTacToe = f"""  
          A B C 
        A {updatedList[0]} {updatedList[1]} {updatedList[2]} 
        B {updatedList[3]} {updatedList[4]} {updatedList[5]}  
        C {updatedList[6]} {updatedList[7]} {updatedList[8]}"""
        
    def getWinnerExist(self):
        return self.winnerExist
    
    def setWinnerExist(self, value):
        self.winnerExist = value
        
    def getPlayer1input(self):
        return self.player1Input
        
    def setPlayer1input(self):
        print("Player 1 please type your input")
        self.player1Input = input()
        self.player1Input.upper()
        
    def getPlayer2input(self):
        return self.player2Input
        
    def setPlayer2input(self):    
        print("Player 2 please type your input")
        self.player2Input = input()
        self.player1Input.upper()
    
