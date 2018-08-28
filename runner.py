import uiautomator2 as u2
from time import sleep
from os import path
import os
import time
from config import *
import shutil
import subprocess
basedir = path.abspath(path.join(path.abspath(__file__),'..'))





class UIHelper(object):
    def __init__(self, driver, pkg_name):
        self.driver = driver
        self.pkg_name = pkg_name
        self.device_info = self.driver.device_info
        self.window_size = self.device_info.get('display', '')
        if isinstance(self.window_size, dict):
            self.height = self.window_size.get('height', '')
            self.width = self.window_size.get('width', '')

    # return width and height
    def get_screen_size(self):
        return self.height, self.width

    # swipe one page
    def swipe_up_one_page(self, times=1, duration=0.5):
        print 'swiping up one page for {} times'.format(times)
        return self.swipe_by_percent(start_x_per=0.5, start_y_per=0.8, end_y_per=0.3, end_x_per=0.5, times=times, duration=duration)

    # swipe interface
    def swipe_by_percent(self, start_x_per, start_y_per, end_x_per, end_y_per, times=1, duration=0.5):
        while times:
            try:
                height = self.height
                width = self.width
                start_x = width * start_x_per
                start_y = height * start_y_per
                end_x = width * end_x_per
                end_y = height * end_y_per
                print ("swiping by percent with fx={}, fy={}, tx={}, ty={}, duration={}".format(start_x, start_y, end_x, end_y, duration))
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
                times -= 1
                sleep(1)
            except BaseException as e:
                print (e.message)
                print (e.args)

    # getscreenshot
    def get_screenshot(self):
        screenshot_filedir = basedir + '/screenshot'
        if not path.exists(screenshot_filedir):
            os.mkdir(screenshot_filedir)
        now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        filename = screenshot_filedir + '/' + now + ".png"
        sleep(1)
        self.driver.screenshot(filename)
        print ('taking screenshot: ' + filename)


# clean screenshot folder
# use this if you need
def clear_former_screenshot():
    shutil.rmtree(basedir + '/screenshot')


# start uiautomator2 server on mobile device
def start_server_on_mobile(udid):
    cmd = 'python -m uiautomator2 init --serial {}'.format(udid)
    output = subprocess.check_output(cmd, shell=True)
    print output


# case runner
def runner():
    start_server_on_mobile(udid)
    driver = u2.connect(udid)  # alias for u2.connect_usb('123456f')
    uihelper = UIHelper(driver=driver, pkg_name=pkg_name)
    driver.app_start(pkg_name)
    i = 0
    global swipe_times
    while i < swipe_times:
        uihelper.get_screenshot()
        uihelper.swipe_up_one_page()
        i += 1


if __name__ == '__main__':
    # clear_former_screenshot()
    runner()