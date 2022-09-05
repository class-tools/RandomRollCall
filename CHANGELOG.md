# Changelog

This is the changelog of [Random Roll Call](https://github.com/class-tools/RandomRollCall).

这是 [随机点名](https://github.com/class-tools/RandomRollCall) 的更新日志。

This change log supports two languages: `en-US` `zh-CN`. (**Every two lines, the first line is `en-US` and the second line is `zh-CN`**)

这个更新日志支持两个语言：`en-US` `zh-CN`。（**每两行第一行为 `en-US` 第二行为 `zh-CN`**）

## 2.0.0

Replan the project.

重新规划项目。

Add CodeQL GitHub Action for static code scanning.

添加 CodeQL GitHub Action 以进行静态代码扫描。

Rename language identifier for Simplified Chinese.

重命名简体中文语言标识符。

Change data files format to Json (Because this module is built-in in Python).

更改数据文件格式为 Json （因为此模块内置在 Python 中）。

Change source code indent to Tab.

更改源代码缩进为 Tab。

When the setting file is missing, the file with the default configuration is automatically generated.

缺失设置文件时自动生成带有默认配置的文件。

The installation package is no longer planned to be provided.

计划不再提供安装包 （但我们允许其他人在发布的文件为基础制作并自由分发安装包）。

Update repository related files to the latest organization standards (However, we allow others to make and freely distribute installation packages based on published files).

将存储库相关文件更新至最新组织标准。

## 1.1.6.x

Add changing number. (The number changes continuously after the first click, and stops after the second click)

添加不断变化的数字。（第一次点击后数字不断变化，第二次点击后停止）

Add welcome text. ("Start")

添加欢迎文本。（“开始”）

## 1.1.5.x LTS

~~**This version of the program is long term supported.**~~

~~**此版本的程序被长期支持。**~~

Fix ISS #6.

修复 ISS #6。

Change Issues Checker Action runtime environment.

更改 Issues Checker Action 运行时环境。

Fix ISS #5. (Modify number range & The font size varies with the length of the number)

修复 ISS #5。（修改数字范围 & 字号随数字长度变化）

Add exception handling.

加入异常处理。

## 1.1.4.x LTS

~~**This version of the program is long term supported.**~~

~~**此版本的程序被长期支持。**~~

Add Github Action to delete issue of users without starring repository.

增加 Github Action 以删除没有 Star 存储库的用户的 Issue。

Add wiki. (Move information from readme to wiki)

增加 Wiki。（移动自述文件中的信息至 Wiki）

Update language yaml file.

更新语言 YAML 文件。

The modified minimum and maximum student numbers can be saved to the setting file.

修改最小及最大学号可以被保存至设置文件。

Increase the version number in the setting file.

在设置文件中增加版本号。

Add data file reading error display. (no longer unresponsive)

增加数据文件读取错误显示。（不再是无反应）

## 1.1.3.x

~~Add Github Action to check pull request code quality.~~ (Deleted in 1.1.4)

~~增加 Github Action 以分析拉取请求的代码质量。~~（在 1.1.4 中被删除）

~~Add Github Action to see result of code on Codecov _(Fixed three times)_.~~ (Deleted in 1.1.3.7)

~~增加 Github Action 以查看在 Codecov 上的代码分析结果 _（修复了三次）_~~（在 1.1.3.7 中被删除）

Edit language operation mode (using YAML).

修改语言运行模式（使用 YAML）。

Add settings file (using YAML).

增加设置文件（使用 YAML）。

**From now on, the program is not a single file (using the installation package).**

**从此版本起，本程序不再是单一编译文件（使用安装包）。**

## 1.1.2.x

Add "Help" to open readme in the browser.

增加 “帮助” 以在浏览器中打开自述文件。

Add dialog to ask the minimum and the maximum student number for random number.

加入对话框以询问最小及最大的学号以获取随机数。

Add changelog.

加入了更新日志。

Update readme.

更新自述文件。

## 1.1.0.x ~ 1.1.1.x

Add label to random roll call.

增加标签以获取随机数。

Add menubar.

增加菜单栏。

Update readme.

更新自述文件。

## Init & 1.0.0.x

Create Github Action to check commit message.

创建 Github Action 以检查提交信息格式。

Add MIT License.

添加 MIT 许可证。

Create readme.

创建自述文件。