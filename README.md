# pdf2word-tool
Python PDF to Word converter
PDF转Word工具
一个基于Python实现的高质量PDF转Word工具，支持保留PDF中的文字、图片、数学公式及原始排版，操作简单，新手可快速上手。
📋 项目介绍
•核心功能：将PDF文件转换为可编辑的Word（.docx）文件
•转换优势：保留原始排版、文字格式、图片及大部分数学公式
•适用场景：学习资料转换、工作文档编辑、论文格式调整等
•依赖库：pdf2docx（核心转换库）、python-docx（Word文件处理）
🔧 环境搭建
本项目支持Windows/Mac/Linux系统，需先安装Python环境，再配置依赖库。
步骤1：安装Python（必做）
1.下载Python安装包：访问Python官网，下载对应系统的3.8+版本（推荐3.10）
2.安装注意：
        
￮Windows：勾选「Add Python to PATH」（自动添加环境变量），其他默认下一步
￮Mac/Linux：可通过官网安装包或终端命令 brew install python3（需先安装Homebrew）
3.验证安装：打开终端/命令提示符，输入 python --version 或 python3 --version，显示版本号即安装成功
步骤2：安装依赖库（必做）
打开终端/命令提示符，直接复制以下命令执行，自动安装所有依赖：
bash
pip install pdf2word python-docx
如果安装失败，尝试用以下命令（针对Python3）：
bash
pip3 install pdf2word python-docx
步骤3：下载项目代码
4.访问本项目GitHub地址：https://github.com/muzijiasang/pdf2word-tool.git
5.点击右上角「Code」→ 选择「Download ZIP」，下载后解压到任意文件夹（如：D:\pdf2word-tool）
🚀 使用步骤
本工具支持两种使用方式，新手推荐「直接修改代码」，进阶用户可使用「命令行传参」。
方式1：新手推荐 - 直接修改代码（最简单）
6.打开解压后的项目文件夹，找到核心文件 pdf2word.py
7.用文本编辑器（如记事本、PyCharm、VS Code）打开 pdf2word.py
8.找到代码末尾的「调用示例」部分，修改 pdf_to_word("你的PDF文件路径") 中的路径：
        # 原代码示例
if __name__ == "__main__":
    # 替换为你的PDF绝对路径（Windows示例）
    pdf_to_word("D:/test.pdf")  
    # Mac/Linux示例：pdf_to_word("/Users/你的名字/Desktop/test.pdf")路径填写规则：
￮Windows系统：用 / 分隔路径（如 D:/学习资料/论文.pdf），或用 \\ 转义（如 D:\\学习资料\\论文.pdf）
￮避免路径包含中文/空格（如「D:\我的文件\测试.pdf」可能报错）
9.保存修改后的代码
10.运行代码：
        
￮方式A：用PyCharm打开项目，点击绿色三角「Run」运行
￮方式B：打开终端，进入项目文件夹（如 cd D:\pdf2word-tool），输入命令 python pdf2word.py 并回车
11.查看结果：转换成功后，Word文件会自动生成在PDF文件同目录下，文件名与PDF一致（如 test.pdf → test.docx）
方式2：进阶使用 - 命令行传参（更灵活）
无需修改代码，直接在终端输入命令指定PDF路径和输出Word路径：
bash
# 基础用法：只指定输入PDF，自动生成Word
python pdf2word.py -i "D:/test.pdf"

# 进阶用法：指定输入PDF和输出Word路径
python pdf2word.py -i "D:/test.pdf" -o "D:/输出结果/转换后的文档.docx"
参数说明：
•-i：必选参数，指定需要转换的PDF文件绝对路径
•-o：可选参数，指定转换后的Word文件保存路径，不指定则默认与PDF同目录
📌 常见问题解决
问题1：运行后提示「错误：找不到文件 xxx.pdf」
•原因：PDF路径填写错误，或文件不在指定路径下
•解决：
        
￮右键PDF文件 → 「属性」→ 复制「位置」+「文件名」，组合成绝对路径（如 D:\Downloads\test.pdf）
￮将PDF文件直接放到项目文件夹下，直接用文件名调用（如 pdf_to_word("test.pdf")）
问题2：转换失败，提示「__enter__」
•原因：pdf2docx库版本过旧，不支持上下文管理器语法
•解决：升级pdf2docx库，终端执行命令：pip install --upgrade pdf2docx
问题3：转换后文字乱码/公式显示异常
•原因：PDF编码特殊，或公式为复杂LaTeX格式
•解决：
        
￮文字乱码：尝试将代码中编码相关参数改为 codec="gbk"
￮公式异常：转换后的Word文件中，用「插入→公式」功能手动微调，或使用LaTeX编辑器辅助编辑
问题4：Git推送时提示「443连接失败」
•原因：国内网络无法直接访问GitHub
•解决：配置Git代理，终端执行命令：
git config --global http.sslVerify false
git config --global http.proxy https://ghproxy.com:443
git config --global https.proxy https://ghproxy.com:443
✨ 功能特性
•✅ 保留文字：完美还原PDF中的文字内容、字体、字号
•✅ 保留图片：自动提取PDF中的图片，插入到Word对应位置
•✅ 保留公式：支持简单数学公式还原，复杂公式可微调
•✅ 排版不失真：还原PDF的段落、行距、页边距等排版格式
•✅ 操作简单：新手可通过修改路径直接使用，无需复杂配置
📝 注意事项
•建议转换单个PDF文件大小不超过100MB，超大文件可分章节转换
•加密的PDF文件需先解密（输入密码打开后保存为普通PDF），否则无法转换
•转换后的Word文件建议用Office 2016+或WPS打开，避免低版本兼容问题
•项目中的venv 文件夹是本地虚拟环境，无需下载和使用
🤝 贡献与反馈
如果使用过程中遇到问题，或有功能优化建议，欢迎在GitHub仓库提交Issues，也可以直接Fork项目进行修改，提交Pull Request～
📌 项目地址
GitHub：https://github.com/muzijiasang/pdf2word-tool.git
