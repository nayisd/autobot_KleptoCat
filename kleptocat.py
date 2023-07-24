import pyautogui as p
import keyboard as k
import time

def sclick(x):
    p.click(x)
    time.sleep(0.5)

def play1():
    button1 = p.locateCenterOnScreen('assets/button1.png', confidence = 0.9)
    sclick(button1)
    outplay = p.pixelMatchesColor(703,833,(105,105,105))
    while outplay:
        bub = p.locateAllOnScreen('assets/bubble_bub.png', confidence = 0.92)
        coin = p.locateAllOnScreen('assets/bubble_coin.png', confidence = 0.92)
        for i in bub:
            p.click(i)
        for i in coin:
            p.click(i)
        if k.is_pressed("Shift"):
            confirm_result = p.confirm('Do you wanna call back?')
            if confirm_result == 'OK':
                p.press('Esc')
                bell = p.locateCenterOnScreen('assets/bell.png', confidence = 0.5)
                time.sleep(1)
                sclick(bell)
                yesbutton = p.locateCenterOnScreen('assets/yesbutton.png', confidence = 0.9)
                sclick(yesbutton)
                time.sleep(3)
                break
            else:
                pass
        outplay = p.locateCenterOnScreen('assets/outplay.png', confidence = 0.3, region = outregion)
    else:
        p.press('Esc')
        
def feed():
    count = 0
    while count < 3:
        sclick(cat)
        treat = p.locateCenterOnScreen('assets/treat.png', confidence = 0.9)
        sclick(treat)
        p.moveTo(705,661)
        p.click()
        p.dragTo(705,741, 2.5, button='left')
        time.sleep(0.5)
        count +=1


begin = p.locateCenterOnScreen('assets/begin.png', confidence = 0.9)
cat = 702,830
playregion = 512,256,902,520
outregion = 596,670,805,849
game = True

if begin != None:
    sclick(begin)
    time.sleep(7)

while game:
    close = p.locateCenterOnScreen('assets/close.png', confidence = 0.7)
    out = p.locateCenterOnScreen('assets/out.png', confidence = 0.3, region = outregion)
    if out:
        playbutton = p.locateCenterOnScreen('assets/playbutton.png', confidence = 0.5)   
        sclick(playbutton)
        play1()
    elif close:
        sclick(close)
    else:
        sclick(cat)
        time.sleep(2)
        treat = p.locateOnScreen('assets/treat.png', confidence = 0.9)
        if treat:
            sclick(cat)
        else:
            time.sleep(7)
            close2 = p.locateCenterOnScreen('assets/close2.png', confidence = 0.7)
            if close2:
                sclick(close2)
        feed()
        sclick(cat)
        leave = p.locateCenterOnScreen('assets/leave.png', confidence = 0.7) 
        p.click(leave)
