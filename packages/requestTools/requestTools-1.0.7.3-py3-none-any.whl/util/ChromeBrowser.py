import base64

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BrowserUtil:

    @staticmethod
    def blobToPdf(htmlContent, pdfName,chromedriverPath):

        # 指定ChromeDriver的路径
        service = Service(chromedriverPath)  # 请替换为你的chromedriver路径

        # 设置浏览器选项
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        # 创建浏览器实例
        browser = webdriver.Chrome(service=service, options=options)

        # 浏览器访问空白页面
        browser.get("about:blank")

        # 使用浏览器执行JavaScript来设置页面内容
        browser.execute_script(f"document.write(`{htmlContent}`)")

        result = browser.execute_cdp_cmd("Page.printToPDF", {
            "landscape": False,  # 是否横向打印
            "printBackground": True,  # 是否打印背景
            "displayHeaderFooter": False,  # 是否显示页眉页脚
        })

        # 获取 PDF 文件的内容（base64 编码）
        pdf_content = result['data']

        # 对编码后的内容进行解码得到二进制数据
        pdf_content = base64.b64decode(pdf_content)

        # 将 PDF 内容保存到文件
        with open(pdfName + ".pdf", "wb") as f:
            f.write(pdf_content)

        # 退出浏览器
        browser.quit()