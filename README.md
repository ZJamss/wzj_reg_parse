**适用于微助教答题内容，转化为考试宝导入所需格式**
> 基本不会更新，代码写得很简单，有问题可以提issue或者自己修改，欢迎pr

### 支持的题目类型：
- 单选
- 多选
- 是非
- 填空
- 简答

### 已知问题：
- 单多选固定ABCD四个选项，不符合无法解析
> 题量不多可以手动修改格式，或者修改代码
- 简答题中的图片无法解析，因为是复制的文字，图片无法拷贝进剪贴板，且未知考试宝是否支持答案添加图片(未使用过)

### 使用教程：
- 打开微助教答题页面，复制所有的题目，形式以及格式如下所示：
![image](https://github.com/ZJamss/wzj_reg_parse/assets/76551468/b034d161-1929-4f05-a213-cd94415e94f1)
```
单选
1
回答正确
下面哪一个活动不是项目？

你的答案

A
野餐活动


B
集体婚礼


C
开发操作系统


D
上课

正确
正确答案
D
解析
暂无解析

隐藏解析
......
```
- 在脚本同目录下新建一个`q.txt`文件，将题目内容复制到其中
- 运行脚本，控制台打印出解析后的格式
- 导入到考试宝即可
