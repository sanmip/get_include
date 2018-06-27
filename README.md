# get_include
选择DTS,获取全部include的DTSI以及DTS文件.

# 背景
高通将整个基线的所有dts及dtsi都放在同一个目录下,而单独某个平台某个项目,只会使用部分dts及dtsi.因此我们将使用到的dts及dtsi都单独放在一个目录中,方便修改和查看


# 使用例子
## 获取高通平台sdm450-mtp.dts所使用到所有文件:

在kernel/arch/arm/boot/dts/qcom下
```
python get_include sdm450-mtp.dts
```
解析文件后,输入一个保存所有文件的目录名
```
output dir name:
```
回车后即可得到所有include的文件
