import requests
from bs4 import BeautifulSoup

// pip install requests beautifulsoup4
class HTMLParserTool:
    def __init__(self, url):
        self.url = url
        self.page_content = self.fetch_html()

    def fetch_html(self):
        """
        获取网页内容
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # 如果响应状态码不是 200，将抛出异常
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"获取页面失败: {e}")
            return None

    def parse_html(self):
        """
        解析网页内容并返回BeautifulSoup对象
        """
        if self.page_content:
            soup = BeautifulSoup(self.page_content, 'html.parser')
            return soup
        else:
            print("网页内容为空，无法解析")
            return None

    def extract_title(self):
        """
        提取页面标题
        """
        soup = self.parse_html()
        if soup:
            title = soup.title.string if soup.title else '无标题'
            return title
        return None

    def extract_links(self):
        """
        提取页面中所有的链接（<a> 标签中的 href 属性）
        """
        soup = self.parse_html()
        links = []
        if soup:
            for link in soup.find_all('a', href=True):
                links.append(link['href'])
        return links

    def extract_paragraphs(self):
        """
        提取页面中的所有段落（<p> 标签内容）
        """
        soup = self.parse_html()
        paragraphs = []
        if soup:
            for paragraph in soup.find_all('p'):
                paragraphs.append(paragraph.get_text())
        return paragraphs

    def extract_images(self):
        """
        提取页面中的所有图片（<img> 标签中的 src 属性）
        """
        soup = self.parse_html()
        images = []
        if soup:
            for img in soup.find_all('img', src=True):
                images.append(img['src'])
        return images

    def display_info(self):
        """
        打印网页的基本信息：标题、所有链接、段落和图片
        """
        print(f"网页标题: {self.extract_title()}")
        print("\n网页链接：")
        links = self.extract_links()
        for link in links:
            print(link)
        
        print("\n网页段落：")
        paragraphs = self.extract_paragraphs()
        for para in paragraphs:
            print(para)
        
        print("\n网页图片：")
        images = self.extract_images()
        for img in images:
            print(img)

# 使用示例
if __name__ == "__main__":
    url = input("请输入要解析的URL: ")
    tool = HTMLParserTool(url)
    tool.display_info()
