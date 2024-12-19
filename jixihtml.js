// 导入模块
const cheerio = require('cheerio');
const axios = require('axios');

// 解析 HTML 字符串
const parseHtml = (html) => {
  // 使用 cheerio 加载 HTML
  const $ = cheerio.load(html);

  // 提取标题
  const title = $('title').text();
  console.log('页面标题:', title);

  // 提取所有的链接 (a 标签)
  $('a').each((index, element) => {
    const link = $(element).attr('href');
    const text = $(element).text();
    console.log(`链接 ${index + 1}: ${text} -> ${link}`);
  });

  // 提取所有的图片链接 (img 标签)
  $('img').each((index, element) => {
    const imgSrc = $(element).attr('src');
    console.log(`图片 ${index + 1}: ${imgSrc}`);
  });
};

// 从网络加载 HTML 页面并解析
const fetchAndParseHtml = async (url) => {
  try {
    const response = await axios.get(url);  // 获取网页内容
    const html = response.data;
    parseHtml(html);  // 解析 HTML 内容
  } catch (error) {
    console.error('获取网页内容失败:', error);
  }
};

// 例子：从一个 URL 中获取 HTML
const url = 'http://www.pwypx.com/view/1493.html'; // 可以替换为你想解析的 URL
fetchAndParseHtml(url);
