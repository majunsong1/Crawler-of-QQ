from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import json
# -*- coding: utf-8 -*-
#definde save file
def saveFile0(date,add):
        f_obj = open(add, 'a', encoding='gbk', errors='ignore')#this kind of arg format can ignore encoding errors
        f_obj.write(date,)#a , can add an Enter in the tail
        #f_obj.write(\n)
        f_obj.close()#should not forget this
#使用selenium
driver = webdriver.PhantomJS(executable_path="C:\\Python\\Python36-32\\Scripts\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")#?the address in windows should be this kind of format
driver.set_window_size(1920, 1080)
#log in
def get_shuoshuo(qq,add):
    print(qq)
    driver.get('https://user.qzone.qq.com/{}/311'.format(qq))#enter your friend's Qzone
    time.sleep(3)
    try:
        driver.find_element_by_id('login_div')
        log_sign = True
    except:
        log_sign = False
    if log_sign == True:
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys('767499658')#your Q number to login
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('mjs122333QQ3')#your Q key to login
        driver.find_element_by_id('login_button').click()
        time.sleep(6)
    driver.implicitly_wait(6)
    #add the follow codes to test whether you have the right to enter your friend's Q zone
    #try:
    #    driver.find_element_by_id('QM_OwnerInfo_Icon')
    #   v_right = True
    #except:
     #   v_right = False
    #if v_right == True:
    driver.switch_to.frame('app_canvas_frame')#if you don't have a friend named qq, there will be wrong
    not_tail = True
    num = 0
    while not_tail == True:
        nickname = driver.find_elements_by_css_selector('qz_311_author.c_tx nickname.goProfile')
        content = driver.find_elements_by_css_selector('.content')
        stime = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
        for con,sti in zip(content,stime):
            data = {
                '昵称':qq,
                '时间':sti.text,
                '说说':con.text
                }
            #print(data)
            saveFile0(str(data),add)
        try:
            driver.find_element_by_link_text(str(num+2))#there should be less spell wrong like drinver
            #t = driver.find_element_by_link_text('下一页')#if there is guy named '下一页'，there will be wrong.
            
            not_tail = True
        except:
            not_tail = False
        if not_tail == True:
            driver.find_element_by_id('pager_go_'+str(num)).send_keys(str(num+2))#the x-path is always changing.
            num=num+1
            t = driver.find_elements_by_class_name("bt_tx2")[1]#t = driver.find_element_by_link_text('确定')
            t.click()#the feedback of driver.find_element_by_class_name()是list类，需要指定具体元素才能使用click
            time.sleep(1)#there should be enough time waiting Qzone cache.
        
            
               
    cookie = driver.get_cookies()#gain the cookies
    cookie_dict = []
    for c in cookie:
        ck = "{0}={1};".format(c['name'],c['value'])
        cookie_dict.append(ck)
    i = ''
    for c in cookie_dict:
        i += c
    print("\n")
    print("==========完成================")
 

 
if __name__ == '__main__':
    get_shuoshuo(int(1746058643),'E:/Python/crawler/test1.txt')
    #get_shuoshuo(int(1303033990),'E:/Python/crawler/test2.txt')
    #get_shuoshuo(int(2458238406),'E:/Python/crawler/test3.txt')
