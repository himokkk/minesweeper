import random
map = [' ' for _ in range(49)] #visiual map

class Game:
    def __init__(self):
        self.visiual_map = [' ' for _ in range(49)] #visiual map
        self.map_size = 7
        self.mines = int(self.map_size*self.map_size/8) 
        self.map = [i for i in range(49)] #logic map
        self.temp = 0
        self.mines_coordinates = random.sample(range(0, self.map_size*self.map_size), self.mines)
        for x in self.mines_coordinates:
            self.map[x] = -1
        for x in range(len(self.map)):            
            if self.map[x]!= -1:
                result = 0
                size = self.map_size
                if(x>size):
                    if(x%size!=0):
                        if(self.map[x-size-1]==-1):
                            result+=1
                    if(self.map[x-size]==-1):
                        result+=1
                    if((x+1)%size!=0):
                        if(self.map[x-size+1]==-1):
                            result+=1
                if((x+1)%size!=0):
                    if(self.map[x+1]==-1):
                        result+=1
                if(x%size!=0):        
                    if(self.map[x-1]==-1):
                        result+=1
                if(x<=size*(size-1)-1):
                    if(x%size!=0):
                        if(self.map[x+size-1]==-1):
                            result+=1
                    if(self.map[x+size]==-1):
                        result+=1
                    if((x+1)%size!=0):
                        if(self.map[x+size+1]==-1):
                            result+=1
                self.map[x] = result

    def start(self):
        self.__init__()
        self.available_moves_function()
        while(len(self.available_moves)!=0):
            self.move()
            self.available_moves_function()
            self.print_map(self.visiual_map)

    def print_map(self, map):
        index_map = [i for i in range(self.map_size)]
        map_string = [str(i)+'  ' for i in index_map]
        print('   ', *map_string)
        print('  ','-'*self.map_size*4)
        for y in range(self.map_size):
            print('', end="")
            print(y, end="")
            for x in range(self.map_size):                
                print(' |', map[x+y*self.map_size], end="")
            print(" |")
        print("Insert coordinates x,y:")
        

    def available_moves_function(self):
        self.available_moves = []
        for index, item in enumerate(self.visiual_map):
            if item == ' ':
                self.available_moves.append(index)

    def move(self):
        coordinates = input()
        x, y = [int(i) for i in coordinates.split(',')]
        index = x+y*self.map_size
        self.available_moves_function()
        print(len(self.available_moves))
        if index in self.available_moves:
            if self.map[index] == -1:
                print("Game over!\n\n\n")
                self.start()
            else:
                self.move_map(index) 
        if len(self.available_moves)-1-self.mines == 0:
            print("You won the game\n\n")

    def move_map(self, x):
        if self.map[x] == 0: 
            self.map[x] = 10        
            self.visiual_map[x] = 0
            size = self.map_size
            if(x>size):
                if(x%size!=0):
                    self.move_map(x-size-1)
                self.move_map(x-size)
                if((x+1)%size!=0):
                    self.move_map(x-size+1)
            if((x+1)%size!=0):
                self.move_map(x+1)
            if(x%size!=0):        
                self.move_map(x-1)
            if(x<=size*(size-1)-1):
                if(x%size!=0):
                    self.move_map(x+size-1)
                self.move_map(x+size)
                if((x+1)%size!=0):
                    self.move_map(x+size+1)      
        elif self.map[x]!= 0 and self.map[x]!=10:
            self.visiual_map[x] = self.map[x]


        
                
            
                        

game = Game()
game.start()
game.print_map(map)