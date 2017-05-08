# if you are putting your test script folders under {git project folder}/tests/, it will work fine.
# otherwise, you either add it to system path before you run or hard coded it in here.
sys.path.append(sys.argv[2])
import os
import common
import facebook
import shutil
import browser
import time

# Disable Sikuli action and info log
com = common.General()
com.infolog_enable(0)

chrome = browser.Chrome()
fb = facebook.facebook()

chrome.clickBar()
chrome.enterLink(sys.argv[3])
wait(fb.comment_icons, 15)

sample2_fp = os.path.join(sys.argv[4], sys.argv[5].replace('sample_1', 'sample_2'))
sleep(2)
capture_width = int(sys.argv[6])
capture_height = int(sys.argv[7])

# Set mouse move delay time to 0 for immediately action requirement
Settings.MoveMouseDelay = 0
hover(fb.comment_icons.targetOffset(-340, -40))
mouseDown(Button.LEFT)
capimg2 = capture(0, 0, capture_width, capture_height)
t1 = time.time()

com.system_print('[log] Mouse Click - Button Up')
mouseUp(Button.LEFT)
sleep(0.1)
t2 = time.time()
com.updateJson({'t1': t1, 't2': t2}, sys.argv[8])
shutil.move(capimg2, sample2_fp.replace(os.path.splitext(sample2_fp)[1], '.png'))
