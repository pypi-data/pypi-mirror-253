#! /usr/bin/env python
# -*- coding=utf-8 -*-
'''
@Author: xiaobaiTser
@Time  : 2024/1/4 22:37
@File  : MonitorBrowser.py
'''
import asyncio
import copy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep, time
from threading import Thread, Lock
'''
selenium > 4.14
'''

async_js = '''
function getXPathForElement(element) {
    if (element && element.id !== "" && element.id !== undefined) {
        return '//' + element.tagName.toLowerCase() + '[@id="' + element.id + '"]';
    }else if (element && element.name !== "" && element.name !== undefined) {
        return '//' + element.tagName.toLowerCase() + '[@name="' + element.name + '"]';
    }else if (element && element.name !== "" && element.name !== undefined) {
        return '//' + element.tagName.toLowerCase() + '[@href="' + element.href + '"]';
    }else if (element && element.src !== "" && element.src !== undefined) {
        return '//' + element.tagName.toLowerCase() + '[@src="' + element.src + '"]';
    }else if (element && element.value !== "" && element.value !== undefined) {
        return '//' + element.tagName.toLowerCase() + '[@value="' + element.value + '"]';
    }else if (element && element.tagName.toLowerCase() === 'html' && !element.parentNode) {
        return '/html';
    }else{
        var index = 0;
        var siblings = element.parentNode.childNodes;

        for (var i = 0; i < siblings.length; i++) {
            var sibling = siblings[i];

            if (sibling === element) {
                return getXPathForElement(element.parentNode) + '/' + element.tagName + '[' + (index + 1) + ']';
            }

            if (sibling.nodeType === 1 && sibling.tagName === element.tagName) {
                index++;
            }
        }
    }
}

var callback = arguments[arguments.length - 1];
var clickedElement = null;

// 遍历当前网页HTML文档中的所有元素
var elements = document.querySelectorAll('*');

for (var i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', function(event) {
        var clickedElement = event.target;
        // 获取最近的包含 iframe 的祖先元素
        var iframeAncestor = clickedElement.closest("iframe");

        // 点击元素的xpath表达式
        var xpath = getXPathForElement(clickedElement);

        // 部分元素type为submit需要存储到缓存中
        if (clickedElement && clickedElement.tagName.toLowerCase() === 'input' && clickedElement.type === 'submit') {
            localStorage.setItem('XPATH', getXPathForElement(clickedElement));
        }

        var value = {
            "iframeAncestor": iframeAncestor,
            "clickedElement": clickedElement.tagName,
            "localStorage": localStorage.getItem('XPATH'),
            "xpath": xpath
        }
        console.log(clickedElement.tagName);
        console.log(value);
        callback(value);
    });
}
'''

thread_lock = Lock()

# 定义一个简单的线程类
class MyThread(Thread):
    def __init__(self, name, target, args):
        super().__init__()
        self.name = name
        self.target = target
        self.args = args
        self.stop_flag = False

    def run(self):
        # print(f"线程 {self.name} 启动")
        while not self.stop_flag:
            print(f"参数 self.args = {self.args}")
            self.target(self.args)
            # print(f"线程 {self.name} 正在运行")
            sleep(0.5)
        # print(f"线程 {self.name} 结束")

    def stop(self):
        # print(f"停止线程 {self.name}")
        self.stop_flag = True

def addJSEventListener(browser):
    # 等待所有元素加载完成
    WebDriverWait(browser, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*'))
    )

    try:
        local_xpath = browser.execute_script("return localStorage.getItem('XPATH')")
        if local_xpath:
            print("您点击元素的Xpath表达式:", local_xpath)
            browser.execute_script("localStorage.removeItem('XPATH')")
        else:
            result = browser.execute_async_script(async_js)
            # 输出返回值
            print("您点击元素的Xpath表达式:", result)
    except Exception as e:
        pass

class MonitorBrowser(object):
    def __init__(self):
        ''' 初始化浏览器对象 '''
        self.Options = webdriver.ChromeOptions()
        self.Options.add_experimental_option('useAutomationExtension', False)      # 去除"Chrome正在受到自动化测试软件的控制"弹出框信息
        self.Options.add_experimental_option('excludeSwitches', ['--enable-automation'])  # 去除"Chrome正在受到自动化测试软件的控制"弹出框信息
        self.Options.add_experimental_option('detach', True)                       # 禁止自动关闭浏览器
        self.Options.add_argument('--ignore-ssl-errors')
        self.Options.add_argument('--disable-blink-features=AutomationControlled')   # 隐藏Webdriver特征

    def browser_status(self):
        ''' 关闭浏览器 '''
        try:
            self.browser.title
            return True
        except Exception as e:
            return False

    def start(self):
        ''' 启动浏览器 '''
        self.browser = webdriver.Chrome(options=self.Options)
        self.browser.implicitly_wait(30)
        self.browser.get('https://mail.163.com/')  # iframe案例
        # self.browser.get('https://www.baidu.com/')  # type=submit案例
        self.browser.set_script_timeout(0.5)
        _t_list = []

        while self.browser_status():
            self.browser.switch_to.default_content()
            _start_time = time()
            addJSEventListener(self.browser)
            # print(f'主页注入js耗时：{time() - _start_time}s')
            # _t_list.append(MyThread(name='page', target=addJSEventListener, args=self.browser))
            iframes = self.browser.find_elements(By.XPATH, '//iframe')
            for i, _ in enumerate(iframes):
                _start_time = time()
                self.browser.switch_to.default_content()
                self.browser.switch_to.frame(_)
                addJSEventListener(self.browser)
                # print(f'iframe_{i}注入js耗时：{time() - _start_time}s')
                # _t_list.append(MyThread(name=f'iframe_{i}', target=addJSEventListener, args=self.browser))

            # for i, t in enumerate(_t_list):
            #     self.browser.switch_to.default_content()
            #     if 0 == i:
            #         t.start()
            #     else:
            #         self.browser.switch_to.frame(iframes[i-1])
            #         t.start()

            sleep(0.2)
            # for t in _t_list:
            #     t.stop()
        self.browser.quit()

    @property
    def js(self):
        return open('getXPathInCurrentPage.js', 'r', encoding='utf-8').read()

if __name__ == '__main__':
    monitor = MonitorBrowser()
    monitor.start()