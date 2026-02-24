import pygame
import json

FONT = None
def load_font():
    global FONT
    FONT = pygame.font.SysFont("Arial",30)

def draw_text(surface,text,size,x,y):
    global FONT
    if not FONT:
        load_font()
    f = pygame.font.SysFont("Arial",size)
    img = f.render(text,True,(255,255,255))
    surface.blit(img,(x,y))

def save_highscore(score):
    try:
        with open("highscore.json","r") as f:
            data = json.load(f)
    except:
        data = {"highscore":0}
    if score > data["highscore"]:
        data["highscore"] = score
        with open("highscore.json","w") as f:
            json.dump(data,f)

def load_highscore():
    try:
        with open("highscore.json","r") as f:
            data = json.load(f)
            return data.get("highscore",0)
    except:
        return 0