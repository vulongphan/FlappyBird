dim = 30
width = 600
height = 600
import random
import os
add_library ("minim")
Player = Minim(this)
main_dir = os.getcwd() + "/images"

class Trailer: #the Trailer at the beginning of the game
    def __init__ (self):
        self.imglist = [loadImage(main_dir+"/trailer_1.jpg"),loadImage(main_dir+"/trailer_2.jpg"),loadImage(main_dir+"/trailer_3.jpg"),loadImage(main_dir+"/trailer_4.jpg"),loadImage(main_dir+"/trailer_5.jpg"),loadImage(main_dir+"/trailer_6.jpg")]
        self.frame = 0
        self.frame_nb = 15
        self.button = loadImage(main_dir+"/skip_button.jpeg") #load the skip button image
        self.button_x = 0
        self.button_y = 0
        self.button_h = 100
        self.button_w = 100

class Flappy_bird: #there will be only one object of type Fallapy bird created through out the whole game
    def __init__(self):
        self.dir = [loadImage(main_dir+'/flappy_bird_balance.jpg'),loadImage (main_dir+'/flappy_bird_down.png'), loadImage (main_dir+'/flappy_bird_up.png')]
        #load image of the flappy bird
        #remember to give the initial position of the bird
        self.x = width/2
        self.y = height/2
        self.n = 0  #used for index of the dir list
        self.xdir = 0
        self.ydir = dim
        self.jump = Player.loadFile(main_dir+"/sounds/jump.mp3")
        #to keep track of the relative position/direction of the bird 
    def move(self): #if user pressed UP key then the bird also moves upwards, otherwise the bird moves downwards
        if keyPressed:
            if keyCode == UP:
                self.n = 2
        else:
            self.n = 1
        self.x += self.xdir
        self.y += self.ydir #this is the suitable increment
        #note that the movement of the bird consists of two components : downwards, upwards and to the right
        #the default movement is downwards and to the right, move up only when there is space key pressed
    def control(self):
        global keyCode
        if keyPressed:
            if keyCode == UP:
                self.n = 2
                self.x += self.xdir
                self.y -= self.ydir *4 #this is the suitable increment 
                # self.jump.rewind()
                # self.jump.play()
        #for each press the bird will move up (ydir = negative) an equal amount

    def show_bird(self):  
        image(self.dir[self.n],self.x,self.y,dim,dim)
        
class Obstacle_1: #the obstacle in the first planet (Earth) is green cone
    def __init__(self):
        self.top = loadImage(main_dir+'/cone_top.png') #the cone from the top
        self.bottom = loadImage(main_dir+'/cone_bottom.png')
        self.width = 2*dim #width of the obstacle
        self.gap = 6*dim
        self.order = random.randint(7,12) #to randomize the height of the top and bottom obstacles whilst keeping the gap constant
        self.top_h = self.order * dim #height of the top obstacle
        self.bottom_h = height - self.gap - self.top_h #height of the bottom obstacle
        self.top_x = width-2*dim #Initial position of obstacles
        self.top_y = 0   
        self.bottom_x = width-2*dim #must be equal to self.top_x
        self.bottom_y = self.top_h+ 6*dim
        self.xdir = dim/2
        self.ydir = dim/2
    
class Obstacle_2: #the obstacle in the second planet (Moon) is rock
    def __init__(self):
        self.top = loadImage(main_dir+'/rock.png') #top image will be somethings pointy downwards
        self.width = 4*dim
        self.top_x = width-2*dim
        self.top_y = random.randint(0,13)*dim
        self.top_h = 6*dim
        self.xdir = dim/2
        self.ydir = dim/4

class Planet_1: #different modes use different object Obstacle but the same object Planet_1 
    def __init__(self):
        self.game_over = False
        self.flappy_bird = Flappy_bird () 
        #each planet object has an attribute that holds a Flappy_bird object
        self.obstacles = {1: [Obstacle_1()],2: [Obstacle_2()]} # a dictionary of obstacles, the key is the mode number that the user chooses
        self.score = 0 #the initial score is 0

    def show_score(self):
        fill(0)
        textSize(20)
        textAlign(CENTER,CENTER)
        text ("Score: "+str(self.score),width-50,15)


class Menu:  #the Menu shows two modes that the user can choose from
    def __init__ (self):
        self.mode1 = loadImage (main_dir+'/earth.png') #Earth
        self.mode1_x = width*3/20
        self.mode1_y = height/3
        self.mode1_h = height/4
        self.mode1_w = width *5/20
        self.mode2 = loadImage(main_dir+'/moon.png') #Moon
        self.mode2_x = width *12/20
        self.mode2_y = height/3
        self.mode2_h = height/4
        self.mode2_w = width * 5/20

class MainGame(): #this is the main game that controls the flow and catches events that happen in the game
    def __init__(self):
        self.trailer = Trailer()
        self.menu = Menu()
        self.planet_nb = 0
        self.planet_1 = Planet_1()
        #to differentiate between the conditions in which the show function of which window will be run, we use attributes and assign them values respectively
        #such as add_score, open_menu and show_trailer
        self.add_score = False
        self.open_menu = False #should be False when the game first shows the trailer
        self.show_trailer = True
        self.entername = EnterName()
        self.scoreboard = ScoreBoard()
        self.bglist = [loadImage(main_dir+"/earth_bg.jpg"),loadImage(main_dir+"/moon_bg.jpg")] #list of background images
        # self.crash = Player.loadFile(main_dir+"/sounds/crash.mp3")
        # self.music_1 = Player.loadFile(main_dir+"/sounds/music_1.mp3")
        # self.music_2 = Player.loadFile(main_dir+"/sounds/music_2.mp3")

    def show_gametrailer(self): #show the game trailer at the beginning
        self.trailer.frame +=1
        for i in range(len(self.trailer.imglist)):
            if i*self.trailer.frame_nb < self.trailer.frame < (i+1)*self.trailer.frame_nb:
                image(self.trailer.imglist[i],0,0,width,height)
        image(self.trailer.button,self.trailer.button_x,self.trailer.button_y,self.trailer.button_w,self.trailer.button_h)
        if self.trailer.frame == len(self.trailer.imglist) * self.trailer.frame_nb: #when the number of frames reaches a certain number, the show function of another window will be executed 
            self.show_trailer = False
            self.open_menu = True

    def show_menu(self): #to show the menu after the trailer
        if self.open_menu == True:
            fill(0)
            textAlign(CENTER,CENTER)
            textSize (40)
            text ('MAIN MENU',width/2,height/7)
            textSize(20)
            text ('Click on the mode you want to play',width/2,height/5)
            image (self.menu.mode1, self.menu.mode1_x, self.menu.mode1_y, self.menu.mode1_w, self.menu. mode1_h)
            image (self.menu.mode2, self.menu.mode2_x, self.menu.mode2_y, self.menu.mode2_w, self.menu.mode2_h)
    
    def show_background(self): #to show the background for each mode
        if self.planet_nb == 1:
            image (self.bglist[0],0,0,width,height)
        elif self.planet_nb == 2:
            image (self.bglist[1],0,0,width,height)

    def obstacle_move(self): #the obstacle moves to the left one by onw creates the impression that the flappy bird is moving to the right
        for i in range(len(self.planet_1.obstacles[self.planet_nb])):
            if self.planet_nb == 1: #for the 1st mode
                self.planet_1.obstacles[self.planet_nb][i].top_x -= self.planet_1.obstacles[self.planet_nb][i].xdir #set the pace of the movement of the obstacles
                self.planet_1.obstacles[self.planet_nb][i].bottom_x -= self.planet_1.obstacles[self.planet_nb][i].xdir
                if self.planet_1.obstacles[self.planet_nb][i].top_x == width - 8*dim and self.planet_1.obstacles[self.planet_nb][i].bottom_x == width - 8*dim:
                    self.planet_1.obstacles[self.planet_nb].append(Obstacle_1()) 
            elif self.planet_nb == 2: #for the second mode
                if self.planet_1.obstacles[self.planet_nb][i].top_y +self.planet_1.obstacles[self.planet_nb][i].top_h+self.planet_1.obstacles[self.planet_nb][i].ydir <= height: 
                    self.planet_1.obstacles[self.planet_nb][i].top_y += self.planet_1.obstacles[self.planet_nb][i].ydir                
                self.planet_1.obstacles[self.planet_nb][i].top_x -= self.planet_1.obstacles[self.planet_nb][i].xdir #set the pace of the movement of the obstacles
            #the gap between each obstacle is 8*dim
                if self.planet_1.obstacles[self.planet_nb][i].top_x == width - 8*dim: 
                    self.planet_1.obstacles[self.planet_nb].append(Obstacle_2()) 
            if self.planet_1.obstacles[self.planet_nb][i].top_x == width - 6*dim:
                self.planet_1.score = i #the score equals to the number of obstacles that have moved through a specific location
    
    def show_obstacle(self): #each time an obstacle passes through a specific location, an Obstacle of the same type is added to the list and shown
        for i in range(len(self.planet_1.obstacles[self.planet_nb])):
            if self. planet_nb == 1:
                image (self.planet_1.obstacles[self.planet_nb][i].top,self.planet_1.obstacles[self.planet_nb][i].top_x ,self.planet_1.obstacles[self.planet_nb][i].top_y,self.planet_1.obstacles[self.planet_nb][i].width,self.planet_1.obstacles[self.planet_nb][i].top_h) #note the dimension of the obstacles and the resultant gap
                image (self.planet_1.obstacles[self.planet_nb][i].bottom,self.planet_1.obstacles[self.planet_nb][i].bottom_x,self.planet_1.obstacles[self.planet_nb][i].bottom_y,self.planet_1.obstacles[self.planet_nb][i].width,self.planet_1.obstacles[self.planet_nb][i].bottom_h)
            elif self.planet_nb == 2:
                image (self.planet_1.obstacles[self.planet_nb][i].top,self.planet_1.obstacles[self.planet_nb][i].top_x ,self.planet_1.obstacles[self.planet_nb][i].top_y,self.planet_1.obstacles[self.planet_nb][i].width,self.planet_1.obstacles[self.planet_nb][i].top_h) #note the dimension of the obstacles and the resultant gap

    def end_game(self): 
        # if the flappy_bird hits the obstacles - its x and y coordinates
        for i in range(len(self.planet_1.obstacles[self.planet_nb])):
            #gotta change this condition later once a new type of obstacle is introduced
            if self.planet_nb == 1:
                if self.planet_1.flappy_bird.x > self.planet_1.obstacles[self.planet_nb][i].top_x - dim and self.planet_1.flappy_bird.x < self.planet_1.obstacles[self.planet_nb][i].top_x + self.planet_1.obstacles[self.planet_nb][i].width and self.planet_1.flappy_bird.y - dim < self.planet_1.obstacles[self.planet_nb][i].top_y+self.planet_1.obstacles[self.planet_nb][i].top_h:
                    self.planet_1.game_over = True
                    # self.crash.rewind()
                    # self.crash.play()
                if self.planet_1.flappy_bird.x > self.planet_1.obstacles[self.planet_nb][i].top_x - dim and self.planet_1.flappy_bird.x < self.planet_1.obstacles[self.planet_nb][i].top_x+self.planet_1.obstacles[self.planet_nb][i].width-dim and self.planet_1.flappy_bird.y > self.planet_1.obstacles[self.planet_nb][i].bottom_y-dim:
                    self.planet_1.game_over = True
                    # self.crash.rewind()
                    # self.crash.play()
            elif self.planet_nb == 2:
                if self.planet_1.obstacles[self.planet_nb][i].top_x - dim < self.planet_1.flappy_bird.x < self.planet_1.obstacles[self.planet_nb][i].top_x + self.planet_1.obstacles[self.planet_nb][i].width:
                    if self.planet_1.obstacles[self.planet_nb][i].top_y - dim < self.planet_1.flappy_bird.y < self.planet_1.obstacles[self.planet_nb][i].top_y + self.planet_1.obstacles[self.planet_nb][i].top_h:   
                        self.planet_1.game_over = True
                        # self.crash.rewind()
                        # self.crash.play()
                if self.planet_1.flappy_bird.y < 0 or self.planet_1.flappy_bird.y > height - dim:
                    self.planet_1.game_over = True
                    # self.crash.rewind()
                    # self.crash.play()

    def show_gameover(self): #show game over window
        if self.planet_1.game_over == True:
            fill(0)
            textAlign(CENTER,CENTER)
            textSize (40)
            text ('GAME OVER',width/2,height/3)
            textSize(20)
            text ('Press R to restart the current mode',width/2,height*7/12)
            text ('Press A to add score',width/2,height*8/12)
            text ('Press M to open the Main Menu',width/2,height*9/12)
            if keyPressed: #Handle Key Pressed
                if key == 'r':
                    self.planet_1 = Planet_1()
                elif key == 'a':
                    self.add_score = True
                elif key == 'm':
                    self.open_menu = True

    def show_scoreboard(self): #to show the scoreboard
        if self.entername.open_scoreboard == True:
            if len(self.scoreboard.player_list) == self.entername.enter_times - 1 and len(self.scoreboard.score_list)==self.entername.enter_times - 1:
                self.scoreboard.player_list.append(self.entername.name)
                self.scoreboard.score_list.append(self.planet_1.score)
            text ("Score Board"+"\n"*2,width/2,height/3 )
            for i in range(len(self.scoreboard.score_list)):
                text (self.scoreboard.player_list[i][:-1]+' : '+str(self.scoreboard.score_list[i]),width/2,height/3+dim*(i+1))
            text ("Press R to restart the current mode", width/2,height/3+dim*(len(self.scoreboard.score_list)+3))
            text ("Press M to go back to Main Menu", width/2,height/3+dim*(len(self.scoreboard.score_list)+5))

            if keyPressed:#to handle key pressed events
                if key == 'r':
                    self.planet_1 = Planet_1()
                    self.entername.open_scoreboard = False
                    self.entername.name = ''
                    self.add_score = False
                elif key == 'm':
                    self.open_menu = True
                    self.entername.open_scoreboard = False
                    self.add_score = False
                    self.entername.name = ''

class ScoreBoard: #Score board object holds 2 atrributes which are the list of players that choose to add score and the score list
    def __init__ (self):
        self.player_list = []
        self.score_list = []

class EnterName: 
    def __init__ (self,name = ""):
        self.name = name
        self.open_scoreboard = False
        self.enter_times = 0
        self.name_char_nb = 0
    def show_entername(self): #to open the window that asks for the name of the player to enter their name
        textSize(20)
        text ("Please enter your name"+"\n"+"Press LEFT button to delete"+"\n"+"Then press ENTER to save:"+'\n'+self.name, width/2,height/3)
        if keyPressed: #Handle key pressed events
            self.name_char_nb+=1 
            if self.name_char_nb>1:
                if not key == CODED:#the keys pressed are only appended to the name variable after the first press (unwanted letter 'a')
                    self.name+= key
                else:
                    if keyCode == LEFT:
                        self.name = self.name[:-1]
                if key == ENTER:
                    self.open_scoreboard = True
                    self.enter_times += 1

main_game = MainGame()

def setup():
    size(width,height)
    background(255)
    frameRate(30)

def draw():
    if frameCount%5 == 0: #this is the suitable framerate
        background(255)
        #Note here that I use different values (True and False) for these attributes in order to differentiate the conditions in which the show function of each window is run
        #this is only run in the trailer windoew at the beginning
        if main_game.show_trailer == True and main_game.open_menu == False and main_game.add_score == False and main_game.entername.open_scoreboard == False:
            main_game.show_gametrailer()
        #this is only run in the main menu window
        if main_game.show_trailer == False and main_game.open_menu == True and main_game.add_score == False and main_game.entername.open_scoreboard == False:
            main_game.show_menu()
        #this is only run when the game is over
        if main_game.show_trailer == False and main_game.open_menu == False and main_game.add_score == False and main_game.entername.open_scoreboard == False:
            main_game.show_gameover()
        #this is only run when the user chooses to add score
        if main_game.show_trailer == False and main_game.open_menu == False and main_game.add_score == True and main_game.entername.open_scoreboard == False:
            main_game.entername.show_entername()
        #this is only run when the scoreboard shows
        if main_game.show_trailer == False and main_game.open_menu == False and main_game.add_score == True and main_game.entername.open_scoreboard == True:
            main_game.show_scoreboard()
        #this is only run when the game has not ended yet
        if main_game.show_trailer == False and main_game.open_menu == False and main_game.planet_1.game_over == False and main_game.entername.open_scoreboard == False and main_game.add_score == False :
            main_game.show_background()
            main_game.planet_1.flappy_bird.control()
            main_game.end_game()
            main_game.planet_1.flappy_bird.show_bird()
            main_game.planet_1.show_score()
            main_game.show_obstacle()
            main_game.obstacle_move()
            main_game.planet_1.flappy_bird.move()

def mouseClicked():
    global main_game
    if main_game.open_menu == True: #To handle mouse clicked events when the player choose which mode they want to play
        if main_game.menu.mode1_x < mouseX < main_game.menu.mode1_x + main_game.menu.mode1_w:
            if main_game.menu.mode1_y < mouseY < main_game.menu.mode1_y + main_game.menu.mode1_h:
                main_game.planet_nb = 1
                main_game.open_menu = False
                main_game.planet_1 = Planet_1()
                # main_game.music_1.play()

        elif main_game.menu.mode2_x < mouseX < main_game.menu.mode2_x + main_game.menu.mode2_w:
            if main_game.menu.mode2_y < mouseY < main_game.menu.mode2_y + main_game.menu.mode2_h:
                main_game.planet_nb = 2
                main_game.open_menu = False
                main_game.planet_1 = Planet_1()
                # main_game.music_2.play()
    if main_game.show_trailer == True: #to handle mouse event when the player decided to click on the skip button
        if main_game.trailer.button_x < mouseX < main_game.trailer.button_y + main_game.trailer.button_w:
            if main_game.trailer.button_y < mouseY < main_game.trailer.button_y + main_game.trailer.button_h:
                main_game.trailer.frame = len(main_game.trailer.imglist) * main_game.trailer.frame_nb
                main_game.show_trailer = False
                main_game.open_menu = True
        

        
    
        
