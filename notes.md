

# BeautifulSoup的find()和findAll()
- findAll(tag, attributes, recursive, text, limit, keywords)
- find(tag, attributes, recursive, text, keywords)
	- tag: 接收一个标签的名称或多个标签名称组成的python列表做标签参数
	- attributes: 用一个Python字典封装一个标签的若干属性和对应的属性值.
	- recursive: 是一个布尔变量.
		- True: findAll会根据要求去查找标签参数的所有子标签
		- False: 只查找文档的一级标签
		- 默认是支持递归查找

	- text: 使用标签的文本内容去匹配而不是标签的属性.
	- limit: 范围限制参数.获取网页中的前x项(limit=x)
	- keyword: 选择具有指定属性的标签
