from frontend import board



class Player:
    def __init__(self,pat):
        self.chances = [21,21,21]
        self.pat = pat
    def push(self,co):
        _ = self.chances.pop(0)
        self.chances.append(co)

class Game:
    guide_b = [[1,2,3],[4,5,6],[7,8,9]]
    def __init__(self):
        self.board = board()
        self.player1 = Player(1)
        self.player2 = Player(-1)
        self.board.on_move_callback = self.Loop
    
    
    def cord_ch(self,num):
        match(num):
            case 1: return 8
            case 2: return 1
            case 3: return 6
            case 4: return 3
            case 5: return 5
            case 6: return 7
            case 7: return 4
            case 8: return 9
            case 9: return 2

    def win_check(self,i):
        if i==0:
            if sum(self.player1.chances) == 15:
                return True
            else:
                return False

        else:
            if sum(self.player2.chances) == 15:
                return True
            else:
                return False

    def Loop(self):
        checking = [x for x in range(1,10)]    
        i = self.board.turn%2
        numm = int(self.board.cord[-1])
        corr = self.cord_ch(numm)
        if i==0:
            self.player1.push(corr)
        else:
            self.player2.push(corr)
        c = self.win_check(i)
        if self.board.turn ==1 or c:  
            if c:
                self.board.chance_txt.set(f"Player {i + 1} Winnss!")
                self.board.b1.config(state='disabled')
                self.board.b2.config(state='disabled')
                self.board.b3.config(state='disabled')
                self.board.b4.config(state='disabled')
                self.board.b5.config(state='disabled')
                self.board.b6.config(state='disabled')
                self.board.b7.config(state='disabled')
                self.board.b8.config(state='disabled')
                self.board.b9.config(state='disabled')
                self.board.root.update()

            elif self.board.cord.sort() == checking and c is False:
                self.board.chance_txt.set("Its a Tie")
game = Game()
if __name__ =='__main__':
    game.board.run()