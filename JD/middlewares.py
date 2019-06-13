"""对接selenium """
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import scrapy
import time


class SeleniumMiddleware():
    # 初始化
    def __init__(self):
        # 声明浏览器对象及显式等待
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)
    # 关闭
    def __del__(self):
        self.browser.close()
    def process_request(self, request, spider):
        # 接收jd.py传过来的meta
        page = request.meta.get("page")
        print("==============第%d页==========="%page)
        try:
            self.browser.get(request.url)
            # 翻页
            time.sleep(2)
            if page >1:
                next = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J_bottomPage"]/span[1]/a[9]')))
                next.click()
                
            # 滚动
            js = 'window.scrollTo(0,document.body.scrollHeight)'
            self.browser.execute_script(js)
            time.sleep(2)
           
            # 确保商品列表所在元素加载完毕
            self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="J_goodsList"]/ul/li')))
            # 返回一个响应对象
            return scrapy.http.HtmlResponse(url=request.url, body=self.browser.page_source, encoding="utf-8", request=request)
        except TimeoutException:
            print("请求超时！")
