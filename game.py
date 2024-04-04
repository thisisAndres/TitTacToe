from actions import Actions
a = Actions()

while a.getWinnerExist():
    a.printMenu()
    a.setPlayer1input()
    a.setPlayer2input()
    a.validateInputs(a.getPlayer1input(), a.getPlayer2input())
    
