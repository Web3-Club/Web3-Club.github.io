# AD 入门系列一：环境搭建

Altium Designer 系列教程

---

## 背景

本系列教程基于 Altium Designer 19，往后如遇版本更新，本教程也将同步跟进。

### 声明

* 为保持版面整洁，提高阅读体验，本系列教程较少插入图片，替换以清晰的文字描述；
* 中英文排版规范遵守 [我的排版标准](https://wiki-power.com/literary/words/wo-de-pai-ban-biao-zhun) ，其中，详细操作步骤及重点内容以 **粗体文本** 展现；
* 本系列教程由 Power Lin 撰写，采用 [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) 协议，转载请保留全文并注明出处。

## 软件下载

本处引用公众号 **软件安装管家** 提供的 [**Altium Designer 2019 安装教程**](https://mp.weixin.qq.com/s?__biz=MzIwMjE1MjMyMw==&mid=2650202563&idx=8&sn=00f54cc41f8232db01982a22e3b729a2&chksm=8ee1412fb996c839543c2d9d25e4597b98ae1f810d3b45d5b01bba4c037daf65281e90bc030e&scene=21#wechat_redirect)，包含软件的下载、破解教程，简单几步即可完成软件的安装，此处不再赘述。

## 调整设置项

工欲善其事，必先利其器。初次打开 Altium Designer，我们可以调整其中的一些设置项，让工具用起来更顺手一些。找到右上角的 **齿轮** 标志，**打开设置页面**，继续以下操作。

### 设置中文

1. 左侧列表依次单击 **System - General** 选项卡，在 **Localizatioin** 栏目下勾选 **Use localized resources** 选项；
2. 点击 **应用** 保存设置，重启 Altium Designer .

### PCB 编辑器

1. 左侧列表单击 **PCB Editor** 选项卡；
2. 在 **PCB Editor**  下单击 **General** 选项卡，在 **铺铜重建** 栏目下，勾选 **铺铜修改后自动重铺** ；在 **文档格式修改报告** 栏目下，勾选 **禁用打开旧版本报告** 和 **禁用打开新版本报告** ；在 **其他** 栏目下，将 **光标类型** 改为 **Large 90** ；
3. 单击 **Display** 选项卡，在 **高亮选项** 栏目下，勾选 **交互编辑时应用高亮** ；
4. 单击 **Board Insight Color Overrides** 选项卡，在 **基础样式** 栏目下，选择 **实心（覆盖颜色）** ；
5. 单击 **DRC Violations Display** 选项卡，在 **冲突 Overlay 样式** 栏目下，选择 **实心（Overlay 颜色）** ；
6. 点击 **应用** 保存设置，重启 Altium Designer .

### 面板

1. 关闭设置页面，在主页菜单栏选择 **视图 - 面板** ，依次点击 **Components, Messages** ；
2. 在弹出的面板右上角点击 **回形针** 标志，将面板吸附在右侧。

### 背景设置为网格

1. 打开任意 PCB 文件（若没有可以新建一个）；
2. **Ctrl + G** 打开网格设置窗口；
3. 在 **显示** 栏目下，将 **精细** 和 **粗糙** 选项卡都设为 **Dots**；

## 输入法兼容性

若无法使用快捷键，请检查是否已经切换到英文状态（输入法状态栏显示为 **ENG**），若无此选项，按如下步骤操作： 

1. 打开 **控制面板** ，打开 **时钟、语言和区域 - 语言** 页面； 
2. 点击 **添加语言** 按钮，添加 **英语** 并选择 **英语（美国）** ； 
3. 在桌面任务栏即可切换输入法。

## 总结

在这一章节中，我们基本完成了 Altium Designer 软件环境的搭建，可以开始愉快地画板子了 :\)

## 参考与致谢

* [Altium 公司 Altium Designer 专栏](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)

另：感谢彬哥整理的经验和笔记。

