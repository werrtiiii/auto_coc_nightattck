import cv2
import pyautogui as pa
import time
import win32gui
def get_window_center(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        rect = win32gui.GetWindowRect(hwnd)
        left, top, right, bottom = rect
        center_x = (left + right) // 2
        center_y = (top + bottom) // 2
        return (center_x, center_y)
    else:
        return None
    

def getxy(img_model_path, threshold):
    pa.screenshot().save("./pic/screenshot.png")
    img = cv2.imread("./pic/screenshot.png")
    img_m = cv2.imread(img_model_path)
    height, width, _ = img_m.shape
    result = cv2.matchTemplate(img, img_m, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if min_val > threshold:
        return 0
    up_left = min_loc
    low_right = (up_left[0] + width, up_left[1] + height)
    avg = (int((up_left[0] + low_right[0]) / 2), int((up_left[1] + low_right[1]) / 2))
    
    return avg


def auto_click(avg):
    pa.moveTo(avg[0],avg[1],0.15)
    pa.click(avg[0],avg[1],button='left')

#蛮野人放角落
def attack_plan1():
    auto_click(getxy("./pic/soldier/wild_man.png",0.3))
    pa.moveTo(getxy("./pic/corner.png",0.3),duration= 0.4)
    pa.mouseDown(button='left')
    time.sleep(4)
    pa.mouseUp(button='left')
#女巫放角落
def attack_plan2():
    if getxy("./pic/king3.png",0.2)!=0:
        auto_click(getxy("./pic/king3.png",0.3))#下王
        pa.moveTo(*get_window_center("雷电模拟器"))
        pa.moveRel(580,20,duration=0.2)     #移到下兵位置
        pa.click(button='left')
        pa.click(getxy("./pic/king3.png",0.3))
    elif getxy("./pic/king.png",0.2)!=0:
        auto_click(getxy("./pic/king.png",0.3))#下王
        pa.moveTo(*get_window_center("雷电模拟器"))
        pa.moveRel(580,20,duration=0.2)     #移到下兵位置
        pa.click(button='left')
        pa.click(getxy("./pic/king.png",0.3))
    auto_click(getxy("./pic/soldier/nvwu.png",0.3))
    time.sleep(2) #隔两秒后下女巫
    pa.moveTo(*get_window_center("雷电模拟器"))
    pa.moveRel(580,20,duration=0.2)     #移到下兵位置
    pa.mouseDown(button='left')
    time.sleep(2)
    pa.mouseUp(button='left')
    pa.moveTo(*get_window_center("雷电模拟器"))
    pa.moveRel(-610,350)
    pa.click()
    for i in range(8):
        pa.moveRel(118,0)
        pa.click()
    while ((getxy("./pic/next.png",0.3)==0)and(getxy("./pic/back_home.png",0.2)==0)):
        time.sleep(1)
        while getxy("./pic/king3.png",0.3)!=0 or getxy("./pic/king.png",0.3)!=0:
            if (getxy("./pic/next.png",0.1)!=0)or(getxy("./pic/back_home.png",0.2)!=0):
                break
            temp1 =getxy("./pic/king3.png",0.2)
            temp2 =getxy("./pic/king.png",0.2)
            if temp1!=0:
                pa.click(temp1[0],temp1[1],button='left')
            elif temp2!=0:
                pa.click(temp2[0],temp2[1],button='left')
            time.sleep(2)
    print("下一次进攻")
    if getxy("./pic/next.png",0.3)!=0:
        if getxy("./pic/king3.png",0.2)!=0:
            center = get_window_center("雷电模拟器")
            if center:
                pa.moveTo(*center, 0.3)
            else:
                print("未找到指定窗口")
            pa.keyDown('ctrl')
            pa.scroll(-400)
            time.sleep(0.1)
            pa.scroll(-400)
            pa.keyUp('ctrl')
            auto_click(getxy("./pic/king3.png",0.3))#下王
            pa.moveTo(*get_window_center("雷电模拟器"))
            pa.moveRel(580,20,duration=0.2)     #移到下兵位置
            pa.click(button='left')
            pa.click(getxy("./pic/king3.png",0.3))
            
        elif getxy("./pic/king.png",0.25)!=0:
            center = get_window_center("雷电模拟器")
            if center:
                pa.moveTo(*center, 0.3)
            else:
                print("未找到指定窗口")
            pa.keyDown('ctrl')
            pa.scroll(-400)
            time.sleep(0.1)
            pa.scroll(-400)
            pa.keyUp('ctrl')
            auto_click(getxy("./pic/king.png",0.3))#下王
            pa.moveTo(*get_window_center("雷电模拟器"))
            pa.moveRel(580,20,duration=0.2)     #移到下兵位置
            pa.click(button='left')
            pa.click(getxy("./pic/king.png",0.3))
        auto_click(getxy("./pic/soldier/nvwu.png",0.3))
        time.sleep(2) #隔两秒后下女巫
        pa.moveTo(*get_window_center("雷电模拟器"))
        pa.moveRel(580,20,duration=0.2)     #移到下兵位置
        pa.mouseDown(button='left')
        time.sleep(2)
        pa.mouseUp(button='left')
        while getxy("./pic/soldier/nvwu1.png",0.3)!=0:
            pa.click(getxy("./pic/soldier/nvwu1.png",0.3))
        while ((getxy("./pic/back_home.png",0.2)==0)):
            time.sleep(1)
            while getxy("./pic/king3.png",0.3)!=0 or getxy("./pic/king.png",0.3)!=0:
                if (getxy("./pic/back_home.png",0.2)!=0):
                    break
                temp1 =getxy("./pic/king3.png",0.2)
                temp2 =getxy("./pic/king.png",0.2)
                if temp1!=0:
                    pa.click(temp1[0],temp1[1],button='left')
                elif temp2!=0:
                    pa.click(temp2[0],temp2[1],button='left')
                time.sleep(2)

    


def auto_night_attack(attack_plan):
    time.sleep(0.5)
    auto_click(getxy("./pic/Night_Attack.png",0.2))
    #time.sleep(0.5)
    if getxy("./pic/search.png",0.3)!=0:
        auto_click(getxy("./pic/search.png",0.3))
    else:
        print("检测不到搜索玩家按钮")
    time.sleep(4)
    center = get_window_center("雷电模拟器")
    if center:
        pa.moveTo(*center, 0.3)
    else:
        print("未找到指定窗口")
    time.sleep(0.5)
    pa.keyDown('ctrl')
    pa.scroll(-400)
    time.sleep(0.1)
    pa.scroll(-400)
    pa.keyUp('ctrl')
    attack_plan() #进攻方案
    while getxy("./pic/back_home.png",0.2)==0:
        time.sleep(0.4)
    auto_click(getxy("./pic/back_home.png",0.2))

if __name__ == '__main__':
    auto_click(getxy("./pic/open_leidian.png",0.3))
    time.sleep(0.5)
    count=0
    a=1
    while 1:
        print(f"第{a}次进攻")
        a=a+1
        auto_night_attack(attack_plan2)
        time.sleep(3)
        if getxy("./pic/yes.png",0.2)!=0:
                pa.click(getxy("./pic/yes.png",0.2))
                time.sleep(1)
        if count==3:
            print("收集圣水")
            count=0
            center = get_window_center("雷电模拟器")
            if center:
                pa.moveTo(*center, 0.3)
            else:
                print("未找到指定窗口")
            time.sleep(0.5)
            pa.scroll(300)
            time.sleep(0.1)
            pa.scroll(300)
            time.sleep(0.2)
            pa.moveTo(*getxy("./pic/dw.png",0.3),0.1)
            pa.moveRel(-151,90,duration=0.1)
            pa.click()
            center = get_window_center("雷电模拟器")
            if center:
                pa.moveTo(*center, 0.2)
            else:
                print("未找到指定窗口")
            pa.moveRel(328,276)
            pa.click()
            pa.moveRel(290,0)
            pa.click()
            time.sleep(0.8)
        count=count+1
    
    #print(f"{get_window_center("雷电模拟器")}")