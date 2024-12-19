import requests

def download_image(url, save_path):
    try:
        # 向图片的URL发送GET请求
        response = requests.get(url)
        
        # 如果请求成功（HTTP 状态码 200）
        if response.status_code == 200:
            # 打开文件并以二进制模式写入图片内容
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"图片已成功下载到: {save_path}")
        else:
            print(f"下载失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"发生错误: {e}")

# 示例：下载一张图片
image_url = "https://example.com/path/to/image.jpg"  # 请替换为你需要下载的图片的URL
save_path = "downloaded_image.jpg"  # 保存图片的路径

download_image(image_url, save_path)