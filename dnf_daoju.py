# coding:utf-8
"""
#   @Author QianLinGo
#   @Date   2018-7-3
#   @Use    获取地下城与勇士的大区数据
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
import Mysql

area_list = []
user_qq = ''
user_qq_password = ''

driver = webdriver.Firefox()
url = "http://daoju.qq.com/dnf/"
driver.get(url)
driver.implicitly_wait(1000)

#Click Login Btn
mouse = driver.find_element_by_id("btn_topbar_unlogin_login")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_id("btn_topbar_unlogin_login").click()
driver.implicitly_wait(6000)
#切换到loginIframe模块
driver.switch_to_frame('loginIframe')
#休眠3秒，等待页面加载完毕继续执行
sleep(3)
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys(user_qq)
driver.find_element_by_id('p').clear()
driver.find_element_by_id('p').send_keys(user_qq_password)
sleep(4)
driver.find_element_by_id('login_button').click()
#查找绑定角色超链接元素
driver.switch_to_default_content()
sleep(3)
driver.find_element_by_id("bind-role-btn").click()
#三秒延迟等待页面加载完成后，获取第一个大区Select
sleep(3)
all_selected_area = driver.find_element_by_id("dj_rb_area")
#遍历第一个Select时，将文本存入集合
for select in Select(all_selected_area).options:
    print(select)
    if(select.text =="选择大区"):
        continue
    area_list.append(select.text)
#外循环刚刚存入的集合
#内循环获取外循环的值（即大区名称，如福建）赋值到第一个Select，并取得第二个Select的联动数据
for text in area_list:
    Select(all_selected_area).select_by_visible_text(text)
    all_selected_child_area = driver.find_element_by_id("dj_rb_server")
    area_parent_id = Mysql.execute_insert('INSERT INTO DNF_AREA(C_NAME,I_LEVEL,C_PARENT) VALUES(%s,1,0)',text)
    count = area_parent_id
    for value in Select(all_selected_child_area).options:
        if(value.text=="选择服务器"):
            continue
        print(count)
        sql = "INSERT INTO DNF_AREA(C_NAME,I_LEVEL,C_PARENT) VALUES('%s',0,'%s')" % \
                (value.text,count)
        area_parent_id = Mysql.execute(sql)
        print("  "+value.text)

#退出浏览器
driver.quit()
