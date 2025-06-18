from ConnectFour import *
from PyGamePlayer import *
from TerminalPlayer import TerminalPlayer
from StudentPlayer import StudentPlayer
from WillPlayer import WillPlayer
from levandovsky import levandovsky

myGame = ConnectFour(render=True)  

levandovskyPlayer = levandovsky()
willsPlayer = WillPlayer()
playerA  = StudentPlayer()    #random bot
playerB = TerminalPlayer()
playerC2  = PyGamePlayer(myGame)

myGame.playGame(playerC2, levandovskyPlayer)
