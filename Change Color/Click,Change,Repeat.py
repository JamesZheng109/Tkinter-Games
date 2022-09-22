#Imports
from random import randint
from tkinter import Tk,Button,Frame,PhotoImage,Label
from tkinter.ttk import Notebook
#Window stuff
window=Tk()
window['background']='thistle'
window.title('Click, Change, Repeat')
window.iconbitmap('Gif//Click_Change_Repeat_icon.ico')
window.maxsize(912,500)
window.minsize(912,500)
#Tab stuff
tab=Notebook(window,width=410,height=300)
#Frames
color=Frame(tab,bg='bisque',bd=5,relief='ridge')
animation=Frame(tab,bg='grey30',bd=5,relief='ridge')
hint=Frame(tab,bd=5,relief='ridge')
hint.pack(fill='both',expand=1)
#Add Frames to Tabs
tab.add(color,text='Colors')
tab.add(animation,text='Animations')
tab.add(hint,text='Things To Note')
tab.place(x=500,y=0)
tab.select(tab_id=2)
#List
##Compare
##Don't Touch
istrue=[]
###Unlock Colors
Red=['Red','Red','Red']
Blue=['Blue','Blue','Blue']
Yellow=['Yellow','Yellow','Yellow']
Orange=['Orange','Orange','Orange']
Green=['Green','Green','Green']
Purple=['Purple','Purple','Purple']
Pink=['Pink','Pink','Pink']
Brown=['Brown','Brown','Brown']
Black=['Black','Black','Black']
White=['White','White','White']
###Play Gifs
Rainbow=['Red','Orange','Yellow','Green','Blue','Purple']
Bears=['Black','White','Brown']
ZebraCoffee=['Black','White','Black','White']
Love=['Purple','Pink','Red','White']
Bee=['Yellow','Black','Yellow','Black']
Outdoor=['Green','Yellow','Blue','Pink','Red','Purple']
Political=['Blue','White','Red']
RGB=['Red','Green','Blue']
Royal=['Purple','Yellow','White','Black']
Bobby=['Blue','Orange','Brown','Black','Yellow']
##Gifs
rainbow=[PhotoImage(file='Gif//Rainbow.gif',format='gif -index 0'),PhotoImage(file='Gif//Rainbow.gif',format='gif -index 1'),PhotoImage(file='Gif//Rainbow.gif',format='gif -index 2'),
         PhotoImage(file='Gif//Rainbow.gif',format='gif -index 3'),PhotoImage(file='Gif//Rainbow.gif',format='gif -index 4')]
bear=[PhotoImage(file='Gif//Bears.gif',format='gif -index 0'),PhotoImage(file='Gif//Bears.gif',format='gif -index 1'),PhotoImage(file='Gif//Bears.gif',format='gif -index 2'),
      PhotoImage(file='Gif//Bears.gif',format='gif -index 3'),PhotoImage(file='Gif//Bears.gif',format='gif -index 4'),PhotoImage(file='Gif//Bears.gif',format='gif -index 5'),
      PhotoImage(file='Gif//Bears.gif',format='gif -index 6'),PhotoImage(file='Gif//Bears.gif',format='gif -index 7')]
zebracoffee=[PhotoImage(file='Gif//Zebra+Coffee.gif',format='gif -index 0'),PhotoImage(file='Gif//Zebra+Coffee.gif',format='gif -index 1'),PhotoImage(file='Gif//Zebra+Coffee.gif',format='gif -index 2'),
             PhotoImage(file='Gif//Zebra+Coffee.gif',format='gif -index 1'),PhotoImage(file='Gif//Zebra+Coffee.gif',format='gif -index 0')]
love=[PhotoImage(file='Gif//Handholding.gif',format='gif -index 0'),PhotoImage(file='Gif//Handholding.gif',format='gif -index 1'),PhotoImage(file='Gif//Handholding.gif',format='gif -index 2'),
      PhotoImage(file='Gif//Handholding.gif',format='gif -index 3'),PhotoImage(file='Gif//Handholding.gif',format='gif -index 4'),PhotoImage(file='Gif//Handholding.gif',format='gif -index 5'),
      PhotoImage(file='Gif//Handholding.gif',format='gif -index 6'),PhotoImage(file='Gif//Handholding.gif',format='gif -index 7'),PhotoImage(file='Gif//Handholding.gif',format='gif -index 8')]
bee=[PhotoImage(file='Gif//Bee.gif',format='gif -index 0'),PhotoImage(file='Gif//Bee.gif',format='gif -index 1'),PhotoImage(file='Gif//Bee.gif',format='gif -index 2'),
     PhotoImage(file='Gif//Bee.gif',format='gif -index 1')]
outdoor=[PhotoImage(file='Gif//TouchGrass.gif',format='gif -index 0'),PhotoImage(file='Gif//TouchGrass.gif',format='gif -index 1'),PhotoImage(file='Gif//TouchGrass.gif',format='gif -index 2'),
         PhotoImage(file='Gif//TouchGrass.gif',format='gif -index 3'),PhotoImage(file='Gif//TouchGrass.gif',format='gif -index 4'),PhotoImage(file='Gif//TouchGrass.gif',format='gif -index 5'),
         PhotoImage(file='Gif//TouchGrass.gif',format='gif -index 6'),PhotoImage(file='Gif//TouchGrass.gif',format='gif -index 7'),PhotoImage(file='Gif//TouchGrass.gif',format='gif -index 8'),
         PhotoImage(file='Gif//TouchGrass.gif',format='gif -index 9'),PhotoImage(file='Gif//TouchGrass.gif',format='gif -index 10')]
political=[PhotoImage(file='Gif//PoliticalTakeHere.gif',format='gif -index 0'),PhotoImage(file='Gif//PoliticalTakeHere.gif',format='gif -index 1'),PhotoImage(file='Gif//PoliticalTakeHere.gif',format='gif -index 2'),
           PhotoImage(file='Gif//PoliticalTakeHere.gif',format='gif -index 1')]
rgb=[PhotoImage(file='Gif//TV.gif',format='gif -index 0'),PhotoImage(file='Gif//TV.gif',format='gif -index 1'),PhotoImage(file='Gif//TV.gif',format='gif -index 2'),
     PhotoImage(file='Gif//TV.gif',format='gif -index 3'),PhotoImage(file='Gif//TV.gif',format='gif -index 4'),PhotoImage(file='Gif//TV.gif',format='gif -index 5'),
     PhotoImage(file='Gif//TV.gif',format='gif -index 6'),PhotoImage(file='Gif//TV.gif',format='gif -index 7'),PhotoImage(file='Gif//TV.gif',format='gif -index 8')]
royal=[PhotoImage(file='Gif//CollectTax.gif',format='gif -index 0'),PhotoImage(file='Gif//CollectTax.gif',format='gif -index 1'),PhotoImage(file='Gif//CollectTax.gif',format='gif -index 2'),
       PhotoImage(file='Gif//CollectTax.gif',format='gif -index 3'),PhotoImage(file='Gif//CollectTax.gif',format='gif -index 4'),PhotoImage(file='Gif//CollectTax.gif',format='gif -index 5'),
       PhotoImage(file='Gif//CollectTax.gif',format='gif -index 6'),PhotoImage(file='Gif//CollectTax.gif',format='gif -index 7')]
bobby=[PhotoImage(file='Gif//HiBobby.gif',format='gif -index 0'),PhotoImage(file='Gif//HiBobby.gif',format='gif -index 1'),PhotoImage(file='Gif//HiBobby.gif',format='gif -index 2'),
       PhotoImage(file='Gif//HiBobby.gif',format='gif -index 1')]
def play_gif(gif_list,speed,frame_number):
    '''Plays gifs
gif_list=.gif file seperated into frames and put into a list
speed=how many milliseconds X 100 the function will take to run again
frame_number=to indicate current frame to display (Just set this to 0)'''
    #Copies contents of gif_list to play list so ids remain different
    play=gif_list.copy()
    #Only if play list is not empty does any looping occur
    if play!=[]:
        currentframe=play[frame_number]
        if currentframe!=frame_number:
            currentframe=play[frame_number]
        frame_number+=1
        #Check to see if frame_number will create an IndexError
        if frame_number>=len(play):
            frame_number=0
        if animation['height']!=currentframe.height() and animation['width']!=currentframe.width():
            animation.config(width=currentframe.width(),height=currentframe.height())
        animation.config(image=currentframe)
    #Does the command again after speed x 100 seconds have past because while loop won't work
    window.after(speed*100,play_gif,gif_list,speed,frame_number)
#Command
class change():
    #Flags
    def __init__(self,window):
        '''Draws the main game stuff and initalize some stuff'''
        self.window=window
        #Variables
        self.red_flag=False
        self.blue_flag=False
        self.yellow_flag=False
        self.orange_flag=False
        self.green_flag=False
        self.purple_flag=False
        self.pink_flag=False
        self.brown_flag=False
        self.black_flag=False
        self.white_flag=False
        self.rainbow_flag=False
        self.bear_flag=False
        self.zebra_flag=False
        self.love_flag=False
        self.bee_flag=False
        self.outdoor_flag=False
        self.political_flag=False
        self.rgb_flag=False
        self.royal_flag=False
        self.bobby_flag=False
        self.flaglist=[self.red_flag,self.blue_flag,self.yellow_flag,self.orange_flag,self.green_flag,self.purple_flag,self.pink_flag,self.brown_flag,self.black_flag,self.white_flag,
                       self.rainbow_flag,self.bear_flag,self.zebra_flag,self.love_flag,self.bee_flag,self.outdoor_flag,self.political_flag,self.rgb_flag,self.royal_flag,self.bobby_flag]
        #Frame
        self.frame=Frame(self.window,width=500,height=500,relief='ridge',bd=5)
        self.frame.place(x=0,y=0)
        #Button
        self.button=Button(self.frame,text='Random Color\nChange',relief='ridge',width=15,height=8,command=lambda:[self.command(),self.color_check(),self.flag_check()])
        self.button.place(x=200,y=190)
        self.special_button=Button(self.frame,text='Start Game',relief='ridge',width=15,height=8,command=self.special_button_check)
        self.rest=Button(self.frame,text='Rest List',relief='ridge',width=15,height=3,fg=self.button['foreground'],bg=self.button['background'],command=lambda:[self.special_click.clear()])
        self.special_button.place(x=200,y=190)
        #Lists
        self.color=('Red','Blue','Yellow','Orange','Green','Purple','Pink','Brown','Black','White')
        self.special_click=[]
        self.active_animation=[]
    def refresh_list(self,element):
        '''Copies contents of element list to self.active_animation list because command does
not like = for some reason'''        
        self.active_animation.clear()
        self.active_animation=element.copy()
        window.after(100,play_gif,self.active_animation,2,0)
    def command(self):
        '''Changes colors of self.frame and self.button'''
        Random=self.color[randint(0,9)]
        self.frame.configure(bg=Random)
        self.button.configure(bg=Random)
    def set_color(self,bgc,fgc):
        '''Sets self.button, self.frame, self.special_button, and self.rest to a specific
color to make color changing mechanic work
bgc=background color
fgc=foreground color'''
        self.button.config(bg=bgc,fg=fgc)
        self.frame.config(bg=bgc)
        self.special_button.config(bg=bgc,fg=fgc)
        self.rest.config(bg=bgc,fg=fgc)
        #Is function so only checks if called
        self.color_check()
    def flag_check(self):
        '''Checks boolean value of flags and makes getting these buttons to appear as simple
as set to True, save, and run'''
        #if all of them for one click checks all. elif except the first to not do that
        ##istrue because checking a flag would probably mean the button is placed each time once it becomes true, which may cause memory issues
        if self.red_flag and 'red_flag' not in istrue:
            red_button.place(x=0,y=50)
            istrue.append('red_flag')
            tab.select(tab_id=0)
        elif self.blue_flag and 'blue_flag' not in istrue:
            blue_button.place(x=80,y=50)
            istrue.append('blue_flag')
            tab.select(tab_id=0)
        elif self.yellow_flag and 'yellow_flag' not in istrue:
            yellow_button.place(x=160,y=50)
            istrue.append('yellow_flag')
            tab.select(tab_id=0)
        elif self.orange_flag and 'orange_flag' not in istrue:
            orange_button.place(x=240,y=50)
            istrue.append('orange_flag')
            tab.select(tab_id=0)
        elif self.green_flag and 'green_flag' not in istrue:
            green_button.place(x=320,y=50)
            istrue.append('green_flag')
            tab.select(tab_id=0)
        elif self.purple_flag and 'purple_flag' not in istrue:
            purple_button.place(x=0,y=136)
            istrue.append('purple_flag')
            tab.select(tab_id=0)
        elif self.pink_flag and 'pink_flag' not in istrue:
            pink_button.place(x=80,y=136)
            istrue.append('pink_flag')
            tab.select(tab_id=0)
        elif self.brown_flag and 'brown_flag' not in istrue:
            brown_button.place(x=160,y=136)
            istrue.append('brown_flag')
            tab.select(tab_id=0)
        elif self.black_flag and 'black_flag' not in istrue:
            black_button.place(x=240,y=136)
            istrue.append('black_flag')
            tab.select(tab_id=0)
        elif self.white_flag and 'white_flag' not in istrue:
            white_button.place(x=320,y=136)
            istrue.append('white_flag')
            tab.select(tab_id=0)
        elif self.rainbow_flag and 'rainbow_flag' not in istrue:
            rainbow_button.place(x=0,y=50)
            istrue.append('rainbow_flag')
            tab.select(tab_id=1)
        elif self.bear_flag and 'bear_flag' not in istrue:
            bear_button.place(x=80,y=50)
            istrue.append('bear_flag')
            tab.select(tab_id=1)
        elif self.zebra_flag and 'zebra_flag' not in istrue:
            zebra_button.place(x=160,y=50)
            istrue.append('zebra_flag')
            tab.select(tab_id=1)
        elif self.love_flag and 'love_flag' not in istrue:
            love_button.place(x=240,y=50)
            istrue.append('love_flag')
            tab.select(tab_id=1)
        elif self.bee_flag and 'bee_flag' not in istrue:
            bee_button.place(x=320,y=50)
            istrue.append('bee_flag')
            tab.select(tab_id=1)
        elif self.outdoor_flag and 'outdoor_flag' not in istrue:
            outdoor_button.place(x=0,y=136)
            istrue.append('outdoor_flag')
            tab.select(tab_id=1)
        elif self.political_flag and 'political_flag' not in istrue:
            political_button.place(x=80,y=136)
            istrue.append('political_flag')
            tab.select(tab_id=1)
        elif self.rgb_flag and 'rgb_flag' not in istrue:
            rgb_button.place(x=160,y=136)
            istrue.append('rgb_flag')
            tab.select(tab_id=1)
        elif self.royal_flag and 'royal_flag' not in istrue:
            royal_button.place(x=240,y=136)
            istrue.append('royal_flag')
            tab.select(tab_id=1)
        elif self.bobby_flag and 'bobby_flag' not in istrue:
            bobby_button.place(x=320,y=136)
            istrue.append('bobby_flag')
            tab.select(tab_id=1)
        #No point in checking the above if all flags are true
        if all(self.flaglist):
            self.button.config(command=lambda:[self.command(),self.color_check()])
    def special_button_check(self):
        '''Does color related checks and because wanted self.button to be the start button then the random color picker button'''
        #Setting color to red because why not
        self.button.config(bg='Red',fg='White')
        self.frame.config(bg='Red')
        #Change what self.specia_button does in hope of saving memory
        self.special_button.config(text='Click Me',bg='Red',fg='White',command=lambda:[self.list_check(),self.flag_check()])
        self.special_button.place(x=0,y=0)
        self.rest.config(bg='Red',fg='White')
        self.rest.place(x=200,y=320)
        self.flag_check()
    def list_check(self):
        '''Checks if self.special_click matches a list after reaching a certain length and empties it at the end'''
        #Adds self.button's current background color to special_click list
        self.special_click.append(self.button['background'])
        self.special_button.place(x=700,y=700)
        #Checks self.special_click if length reaches 3 elements
        if len(self.special_click)==3:
            if self.special_click==Red:
                self.red_flag=True
                self.special_click.clear()
            elif self.special_click==Blue:
                self.blue_flag=True
                self.special_click.clear()
            elif self.special_click==Yellow:
                self.yellow_flag=True
                self.special_click.clear()
            elif self.special_click==Orange:
                self.orange_flag=True
                self.special_click.clear()
            elif self.special_click==Green:
                self.green_flag=True
                self.special_click.clear()
            elif self.special_click==Purple:
                self.purple_flag=True
                self.special_click.clear()
            elif self.special_click==Pink:
                self.pink_flag=True
                self.special_click.clear()
            elif self.special_click==Brown:
                self.brown_flag=True
                self.special_click.clear()
            elif self.special_click==Black:
                self.black_flag=True
                self.special_click.clear()
            elif self.special_click==White:
                self.white_flag=True
                self.special_click.clear()
            elif self.special_click==Bears:
                self.bear_flag=True
                self.special_click.clear()
            elif self.special_click==RGB:
                self.rgb_flag=True
                self.special_click.clear()
            elif self.special_click==Political:
                self.political_flag=True
                self.special_click.clear()
        #Checks self.special_click if length reaches 4 elements
        elif len(self.special_click)==4:
            if self.special_click==ZebraCoffee:
                self.zebra_flag=True
                self.special_click.clear()
            elif self.special_click==Love:
                self.love_flag=True
                self.special_click.clear()
            elif self.special_click==Bee:
                self.bee_flag=True
                self.special_click.clear()
            elif self.special_click==Royal:
                self.royal_flag=True
                self.special_click.clear()
        #Checks self.special_click if length reaches 5 elements
        elif len(self.special_click)==5:
            if self.special_click==Bobby:
                self.bobby_flag=True
                self.special_click.clear()
        #Checks self.special_click if length reaches 6 elements
        elif len(self.special_click)==6:
            if self.special_click==Rainbow:
                self.rainbow_flag=True
            elif self.special_click==Outdoor:
                self.outdoor_flag=True
            self.special_click.clear()
    def color_check(self):
        '''Makes sure self.speical_button and self.config all have the consistent background
and foreground color based on self.button['background']'''
        if self.button['background']=='Red':
            self.special_button.config(bg='Red',fg='White')
            self.special_button.place(x=0,y=0)
            self.button.config(fg='White')
            self.rest.config(bg='Red',fg='White')
        elif self.button['background']=='Blue':
            self.special_button.config(bg='Blue',fg='White')
            self.special_button.place(x=0,y=100)
            self.button.config(fg='White')
            self.rest.config(bg='Blue',fg='White')
        elif self.button['background']=='Yellow':
            self.special_button.config(bg='Yellow',fg='Black')
            self.special_button.place(x=350,y=0)
            self.button.config(fg='Black')
            self.rest.config(bg='Yellow',fg='Black')
        elif self.button['background']=='Orange':
            self.special_button.config(bg='Orange',fg='Black')
            self.special_button.place(x=350,y=100)
            self.button.config(fg='Black')
            self.rest.config(bg='Orange',fg='Black')
        elif self.button['background']=='Green':
            self.special_button.config(bg='Green',fg='White')
            self.special_button.place(x=0,y=360)
            self.button.config(fg='White')
            self.rest.config(bg='Green',fg='White')
        elif self.button['background']=='Purple':
            self.special_button.config(bg='Purple',fg='White')
            self.special_button.place(x=350,y=360)
            self.button.config(fg='White')
            self.rest.config(bg='Purple',fg='White')
        elif self.button['background']=='Pink':
            self.special_button.config(bg='Pink',fg='Black')
            self.special_button.place(x=300,y=0)
            self.button.config(fg='Black')
            self.rest.config(bg='Pink',fg='Black')
        elif self.button['background']=='Brown':
            self.special_button.config(bg='Brown',fg='White')
            self.special_button.place(x=375,y=100)
            self.button.config(fg='White')
            self.rest.config(bg='Brown',fg='White')
        elif self.button['background']=='Black':
            self.special_button.config(bg='Black',fg='White')
            self.special_button.place(x=250,y=0)
            self.button.config(fg='White')
            self.rest.config(bg='Black',fg='White')
        elif self.button['background']=='White':
            self.special_button.config(bg='White',fg='Black')
            self.special_button.place(x=375,y=0)
            self.button.config(fg='Black')
            self.rest.config(bg='White',fg='Black')
#mainloop
if __name__=='__main__':
    #Game
    game=change(window)
    #Colors tab
    #Content for Color and Animation tabs
    red_button=Button(color,text='Make It Red',bg='Red',fg='White',relief='ridge',width=10,height=5,command=lambda:[game.set_color('Red','White')])
    blue_button=Button(color,text='Splash It\nWith Blue',bg='Blue',fg='White',relief='ridge',width=10,height=5,command=lambda:[game.set_color('Blue','White')])
    yellow_button=Button(color,text='A Shine of\nYellow',bg='Yellow',fg='Black',relief='ridge',width=10,height=5,command=lambda:[game.set_color('Yellow','Black')])
    orange_button=Button(color,text='Squeeze A Bit\n Of Orange',bg='Orange',fg='Black',relief='ridge',width=10,height=5,command=lambda:[game.set_color('Orange','Black')])
    green_button=Button(color,text='Brush Some\nGreen',bg='Green',fg='White',relief='ridge',width=10,height=5,command=lambda:[game.set_color('Green','White')])
    purple_button=Button(color,text='Add Some\nPurple',bg='Purple',fg='White',width=10,height=5,command=lambda:[game.set_color('Purple','White')])
    pink_button=Button(color,text='Spring Of Pink',bg='Pink',fg='Black',relief='ridge',width=10,height=5,command=lambda:[game.set_color('Pink','Black')])
    brown_button=Button(color,text='Toss Some\nBrown',bg='Brown',fg='White',relief='ridge',width=10,height=5,command=lambda:[game.set_color('Brown','White')])
    black_button=Button(color,text='Darken It\nWith Black',bg='Black',fg='White',relief='ridge',width=10,height=5,command=lambda:[game.set_color('Black','White')])
    white_button=Button(color,text='Light It Up\nWith White',bg='White',fg='Black',relief='ridge',width=10,height=5,command=lambda:[game.set_color('White','Black')])
    rainbow_button=Button(animation,text='A rainbow\nis here',bg='SkyBlue',fg='Black',relief='ridge',width=10,height=5,command=lambda:[game.refresh_list(rainbow)])
    bear_button=Button(animation,text='Bear party!',bg='honeydew',fg='black',relief='ridge',width=10,height=5,command=lambda:[game.refresh_list(bear)])
    zebra_button=Button(animation,text='Zebra drinking\ncoffee.',bg='Beige',fg='Black',relief='ridge',width=10,height=5,command=lambda:[game.refresh_list(zebracoffee)])
    love_button=Button(animation,text="Want to see\nsomething\nyou'll never\nexperience?",bg='Hot Pink',relief='ridge',width=10,height=5,command=lambda:[game.refresh_list(love)])
    bee_button=Button(animation,text='Happy bee\n just flying',bg='PaleGreen',fg='Black',relief='ridge',width=10,height=5,command=lambda:[game.refresh_list(bee)])
    outdoor_button=Button(animation,text='Click here\nto touch\ngrass',bg='Spring Green',fg='Black',relief='ridge',width=10,height=5,command=lambda:[game.refresh_list(outdoor)])
    political_button=Button(animation,text="Because\n'everything is\npolitical'",bg='grey54',fg='Black',relief='ridge',width=10,height=5,command=lambda:[game.refresh_list(political)])
    rgb_button=Button(animation,text='RGB screen\ntest!',bg='grey15',fg='White',relief='ridge',width=10,height=5,command=lambda:[game.refresh_list(rgb)])
    royal_button=Button(animation,text='Collect the\ntaxes\nknights!',bg='gold',fg='White',relief='ridge',width=10,height=5,command=lambda:[game.refresh_list(royal)])
    bobby_button=Button(animation,text='Say hi\nto Bobby',bg='mint cream',fg='Black',relief='ridge',width=10,height=5,command=lambda:[game.refresh_list(bobby)])
    #Animations
    animation=Label(window,width=22,height=11,bd=5,relief='ridge')
    animation.place(x=500,y=323)
    #Hints
    hint1=Label(hint,text="-You must click the button labeled 'Click Me' for the current color to be\n  added to your combination.",justify='left')
    hint1.place(x=0,y=0)
    hint2=Label(hint,text='-Shortest color combinations have a length of three and the longest have\n  a length of six.',justify='left')
    hint2.place(x=0,y=33)
    hint3=Label(hint,text="-'Colors' tab: Once the correct color combinations are provided, one can\n  freely change the color to the unlocked color with a button.",justify='left')
    hint3.place(x=0,y=66)
    hint4=Label(hint,text="-'Animations' tab: Once the correct color combinations are provided, one\n  can unlock a button to play an animation",justify='left')
    hint4.place(x=0,y=99)
    hint5=Label(hint,text='-If your color combination reaches a length of six, the list is reset\n  automatically.',justify='left')
    hint5.place(x=0,y=132)
    hint6=Label(hint,text='-When you unlock something new, assuming you are not on it, will send\n  you to the tab with the new content',justify='left')
    hint6.place(x=0,y=165)
    hint7=Label(hint,text="-'Reset' button: Don't be afraid to use it if you think the current your color\n  combination may not be right",justify='left')
    hint7.place(x=0,y=198)
    hint8=Label(hint,text='-The number of animations avaliable is equal to amouunt of colors one\n  can get to display.',justify='left')
    hint8.place(x=0,y=231)
    #Loops
    window.mainloop()
