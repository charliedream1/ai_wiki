# 注意事项

请参看使用文档里的样例使用

- 代码开头务必加上os.getenv('GOOGLE_API_KEY') ，不加会报错，你所在国家无法免费使用
- 直接打印response，中文的答复会变成/u的码，所以请打印response.text。另外在windows或有中文环境的linux下，直接把该字符串打印即可出中文
- 初步测试对话中无法加入system，测试给入system，模型不会响应system中的要求