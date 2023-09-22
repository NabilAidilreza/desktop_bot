from Brain import *
import pygame
from time import sleep,time
# INIT PYGAME #
pygame.init()
clock = pygame.time.Clock()

# WINDOW PROPERTIES #
bgColor = (50, 50, 50) # 256 256 126
X = 320
Y = 320
window = pygame.display.set_mode((X, Y ))
center = 126
pygame.display.set_caption('DeskBot')

# Display Functions #
def drawPNG(pngObject):
    global center, window
    rect = pngObject.get_rect(center = (center, center))
    window.blit(pngObject, rect)
    
def drawGIF(gifObject):
    global center, currentFrame, window
    rect = gifObject[currentFrame].get_rect(center = (center, center))
    window.blit(gifObject[currentFrame], rect)
    currentFrame = (currentFrame + 1) % len(gifObject)

### GIF PROCESSING ###
from PIL import Image, ImageSequence
def pilImageToSurface(pilImage):
    mode, size, data = pilImage.mode, pilImage.size, pilImage.tobytes()
    return pygame.image.fromstring(data, size, mode).convert_alpha()

def loadGIF(filename):
    pilImage = Image.open(filename)
    frames = []
    if pilImage.format == 'GIF' and pilImage.is_animated:
        for frame in ImageSequence.Iterator(pilImage):
            pygameImage = pilImageToSurface(frame.convert('RGBA'))
            frames.append(pygameImage)
    else:
        frames.append(pilImageToSurface(pilImage))
    return frames
### -------------- ###

# SPRITE OBJECTS #
IDLE_PNG = pygame.image.load(r'C:\Users\Nabil\Documents\Coding\Completed_Projects\DesktopBot\Sprites\Idle.png')
MATCH_PNG = pygame.image.load(r'C:\Users\Nabil\Documents\Coding\Completed_Projects\DesktopBot\Sprites\Match.png')
ERROR_PNG = pygame.image.load(r'C:\Users\Nabil\Documents\Coding\Completed_Projects\DesktopBot\Sprites\Error.png')

# GIF OBJECTS #
SEARCHING_GIF = loadGIF(r'C:\Users\Nabil\Documents\Coding\Completed_Projects\DesktopBot\Sprites\Searching.gif')
SLEEPING_GIF = loadGIF(r'C:\Users\Nabil\Documents\Coding\Completed_Projects\DesktopBot\Sprites\Sleeping.gif')
MUSIC_GIF = loadGIF(r'C:\Users\Nabil\Documents\Coding\Completed_Projects\DesktopBot\Sprites\Music.gif')
SOUND_GIF = loadGIF(r'C:\Users\Nabil\Documents\Coding\Completed_Projects\DesktopBot\Sprites\Sound.gif')
CONFUSED_GIF = loadGIF(r'C:\Users\Nabil\Documents\Coding\Completed_Projects\DesktopBot\Sprites\Confused.gif')

MATCH_GIF = loadGIF(r'C:\Users\Nabil\Documents\Coding\Completed_Projects\DesktopBot\Sprites\Match.gif')
ERROR_GIF = loadGIF(r'C:\Users\Nabil\Documents\Coding\Completed_Projects\DesktopBot\Sprites\Error.gif')
LOADING_GIF = loadGIF(r'C:\Users\Nabil\Documents\Coding\Completed_Projects\DesktopBot\Sprites\Loading.gif')
HACK_GIF = loadGIF(r'C:\Users\Nabil\Documents\Coding\Completed_Projects\DesktopBot\Sprites\Hack.gif')

currentFrame = 0

# LABEL CLASS #
class Label(object):
    def __init__(self,string,text):
        self.string = string
        self.text = text
        self.final = ""
    def get_string(self):
        return self.string
    def set_string(self,a):
        self.string = a
    def get_text(self):
        return self.text
    def set_text(self,a):
        self.text = a
    def concat(self):
        try:
            self.final = self.string + self.text.lower()
        except:
            self.final = self.string + str(self.text)
        return self.final

########################################################################## - BOT CLASS - ##########################################################################
class Bot(object):
    # Initiailization #
    def __init__(self):
        # IDLE, MATCH, ERROR, SEARCHING, SLEEPING, MUSIC, SOUND, CONFUSED, HaCk
        self.state = "SLEEPING"
        self.previous_state = self.state
        self.reply = ""
        self.questions = []
        self.keywords = []
        self.allowedsoftware = ["steam","python","spotify","{folder}"]
        self.setupmodes = ['default','code']

    def get_allowedsoftware(self):
        return self.allowedsoftware
    def get_desk_modes(self):
        return self.setupmodes
    # State Functions #S
    def get_state(self):
        return self.state
    def set_state(self,a):
        self.previous_state = self.state
        self.state = a
    def check_state_change(self):
        if self.state == self.previous_state:
            return False
        else:
            return True
    def state_auto(self,b=Label):
        if self.check_state_change() == True:
            self.previous_state = self.state
            b.set_text(self.state)
            

    # Reply Functions #
    def get_reply(self):
        return self.reply
    def set_reply(self,a,b=Label):
        self.reply = a
        b.set_text(a)

    # Keywords Functions #
    def get_keywords(self):
        return self.keywords
    
    def add_keyword(self,a):
        self.keywords.append(a.lower())

    def reset_keywords(self):
        self.keywords = []

    # Question Functions #    
    def get_questions(self):
        return self.questions

    def determine_questions(self):
        # Returns a set of qns to satisfy the action function #
        if self.keywords[0] == "search":
            self.questions = ['What are you searching for?',"On which search engine / site do I search this?"]
        elif self.keywords[0] == "reset":
            self.questions = ["Bot reset completed"] 
        elif self.keywords[0] in self.allowedsoftware:
            self.questions = ["Opening software..." + str(self.keywords[0])]
        else:
            self.questions = ["??? I dont know how to do that ???"]
            self.set_state("CONFUSED")

    # Action Functions #
    def determine_action(self):
        # Carries out a certain action based on the current query collected #
        global currentFrame
        # For every action, set correct state and action -> Reset keywords when done #
        if self.keywords[0] == "search":
            self.set_state("MATCH") # State
            SEARCH(self.keywords[1:]) # Action
            self.reset_keywords() # Reset
        elif self.keywords[0] == "reset":
            self.set_state("SLEEPING") # State
            self.reset_keywords() # Reset
        elif self.keywords[0] in self.allowedsoftware:
            self.set_state("MATCH") # State
            SOFTWARE(self.keywords) # Action
            self.reset_keywords() # Reset
        elif self.keywords[0] in self.setupmodes:
            if self.keywords[0] == "default":
                self.set_state("IDLE") # State
            else:
                self.set_state("HACK") # State
            SETUP(self.keywords) # Action
            self.reset_keywords() # Reset

        currentFrame=0

########################################################################## - BOT CLASS - ##########################################################################

### BOT ###
DesktopBot = Bot()
CycleQn = -1
### --- ###

### INPUT BOX ###
# Font Settings #
base_font = pygame.font.Font(None, 20)
user_text = ''


# Input Box Rect Settings #
inp_x = 10
inp_y = 200
inp_len = 200
inp_wid = 20
input_rect = pygame.Rect(inp_x,inp_y,inp_len,inp_wid)

# Input Box Main Settings #
max_len = 27
  
# Color Coding for Selection #
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color_red = pygame.Color('red')
color = color_passive 
active = False
### --------- ###

### ONSCREEN TEXT ###
ONSCREEN_INPUT = Label("INPUT: ","")
ONSCREEN_REPLY = Label("REPLY: ","WAITING")
ONSCREEN_STATE = Label("STATE: ","SLEEPING")
sub_font = pygame.font.Font(None, 12)

ONSCREEN_RUNTIME = Label("RUNTIME: ","")


### ------------- ###
### BOX SETUPS ###
### QUICK LINKS ###
software_lookup_list = []
for i,app in enumerate(DesktopBot.get_allowedsoftware()):
    minp_x = 265
    minp_y = 30
    software_lookup_list.append([app,pygame.Rect(minp_x,minp_y+(i * 25),50,20)])

### QUICK SETUP ###
modes_lookup_list = []
for i,app in enumerate(DesktopBot.get_desk_modes()):
    minp_x = 265
    minp_y = 200
    modes_lookup_list.append([app,pygame.Rect(minp_x,minp_y+(i * 25),50,20)])

### RESET BOX ###
reset_label = 'Reset'
reset_rect = pygame.Rect(275,295,40,20)

### MANUAL BOX ###
manual_label = 'Manual'
minp_x = 220
minp_y = 295
minp_len = 50
minp_wid = 20
manual_rect = pygame.Rect(minp_x,minp_y,minp_len,minp_wid)
### --------- ###
internal_timer = 0
### MAIN LOOP ###
run = True
while run:
    # Set Frame Rate #
    clock.tick(7)
    # Set Background #
    window.fill(bgColor)

    # Event Management #
    for event in pygame.event.get():
        internal_timer=0
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        # Detect Object Selection #
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Input Box #
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
            # Reset Box #
            if reset_rect.collidepoint(event.pos):
                DesktopBot.reset_keywords()
                DesktopBot.add_keyword('reset')
            # Quick Link #
            for app,rect in software_lookup_list:
                if rect.collidepoint(event.pos):
                    DesktopBot.reset_keywords()
                    DesktopBot.add_keyword(app)
                    DesktopBot.determine_action()
            # Quick Setup #
            for app,rect in modes_lookup_list:
                if rect.collidepoint(event.pos):
                    DesktopBot.reset_keywords()
                    DesktopBot.add_keyword(app)
                    DesktopBot.determine_action()
        if event.type == pygame.KEYDOWN:
            # If Input Box Selected #
            if active:
                # Programme BACKSPACE #
                if event.key == pygame.K_BACKSPACE:
                    # Backspace Input Text #
                    user_text = user_text[:-1]
                # Programme ENTER #
                elif event.key == pygame.K_RETURN:
                    ONSCREEN_INPUT.set_text(user_text)
                    DesktopBot.add_keyword(user_text)
                    CycleQn += 1
                    user_text = ""
                else:
                    # Add letter to input text string #
                    user_text += event.unicode
                    if len(user_text) > max_len:
                        user_text = user_text[:max_len]
    # Check Inactive #
    if internal_timer > 15:
        DesktopBot.reset_keywords()
        DesktopBot.add_keyword('reset')
    ONSCREEN_RUNTIME.set_text(round(internal_timer,2))
    internal_timer += 0.1

    # BOT PROCESSING #
    if DesktopBot.get_keywords() != []:
        # Sets the questions based on keyword if exist #
        DesktopBot.determine_questions()  
        if len(DesktopBot.get_questions()) == 1:
            # Set UI #
            DesktopBot.set_reply(DesktopBot.get_questions()[0],ONSCREEN_REPLY)
            # Wait for player input #
            DesktopBot.determine_action()
            currentFrame = 0
        else:
            if CycleQn < len(DesktopBot.get_questions()):
                DesktopBot.set_state("SEARCHING")
                qn = DesktopBot.get_questions()[CycleQn]
                DesktopBot.set_reply(qn,ONSCREEN_REPLY)
            else:
                DesktopBot.determine_action()
                act = "Retrieving first result from keyword"
                DesktopBot.set_reply(act,ONSCREEN_REPLY)
                currentFrame = 0

    # Check for change for UI #       
    DesktopBot.state_auto(ONSCREEN_STATE)

        
                
    # Debugging Tool #
    if active:
        color = color_active
    else:
        color = color_passive

        
    ### DISPLAY ###
    # Draw Quick Setups #
    mtext_surface = base_font.render('Quick Setups', True, (255, 255, 255))
    window.blit(mtext_surface, (reset_rect.x-50, reset_rect.y-115))
    for app,rect in modes_lookup_list:
        pygame.draw.rect(window, color_passive, rect)
        mtext_surface = base_font.render(app, True, (255, 255, 255))
        window.blit(mtext_surface, (rect.x+2, rect.y+3))
    # Draw Quick Links #
    mtext_surface = base_font.render('Quick Links', True, (255, 255, 255))
    window.blit(mtext_surface, (reset_rect.x-50, reset_rect.y-285))
    for app,rect in software_lookup_list:
        pygame.draw.rect(window, color_passive, rect)
        mtext_surface = base_font.render(app, True, (255, 255, 255))
        window.blit(mtext_surface, (rect.x+2, rect.y+3))
    # Draw Manual Box #
    pygame.draw.rect(window, color_passive, manual_rect)
    mtext_surface = base_font.render(manual_label, True, (255, 255, 255))
    window.blit(mtext_surface, (manual_rect.x+2, manual_rect.y+3))
    # Draw Reset Box #
    pygame.draw.rect(window, color_red, reset_rect)
    mtext_surface = base_font.render(reset_label, True, (255, 255, 255))
    window.blit(mtext_surface, (reset_rect.x+2, reset_rect.y+3))
    # Draw Input Box #
    pygame.draw.rect(window, color, input_rect)
    # Render and Draw Input Text #
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    window.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    # Draw Onscreen Label #
    ate_text_surface = sub_font.render(ONSCREEN_STATE.concat(), True, (255, 255, 255))
    window.blit(ate_text_surface, (10,190))
    inp_text_surface = sub_font.render(ONSCREEN_INPUT.concat(), True, (255, 255, 255))
    window.blit(inp_text_surface, (10,225))
    sta_text_surface = sub_font.render(ONSCREEN_REPLY.concat(), True, (255, 255, 255))
    window.blit(sta_text_surface, (10,240))

    run_text_surface = sub_font.render(ONSCREEN_RUNTIME.concat(), True, (255, 255, 255))
    window.blit(run_text_surface, (130,190))

    # Desk Bot Animation Manager #
    if DesktopBot.get_state() == "IDLE":
        #drawPNG(IDLE_PNG)
        drawGIF(LOADING_GIF)
    elif DesktopBot.get_state() == "MATCH":
        #drawPNG(MATCH_PNG)
        drawGIF(MATCH_GIF)
    elif DesktopBot.get_state() == "ERROR":
        #drawPNG(ERROR_PNG)
        drawGIF(ERROR_GIF)
    elif DesktopBot.get_state() == "SEARCHING":
        drawGIF(SEARCHING_GIF)
    elif DesktopBot.get_state() == "CONFUSED":
        drawGIF(CONFUSED_GIF)
    elif DesktopBot.get_state() == "MUSIC":
        drawGIF(MUSIC_GIF)
    elif DesktopBot.get_state() == "SOUND":
        drawGIF(SOUND_GIF)
    elif DesktopBot.get_state() == "SLEEPING":
        drawGIF(SLEEPING_GIF)
    elif DesktopBot.get_state() == "HACK":
        drawGIF(HACK_GIF)
    

    pygame.display.update()
