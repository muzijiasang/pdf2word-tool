from pdf2docx import Converter
import os


def pdf_to_word(pdf_path, word_path=None):
    # 检查PDF文件是否存在
    if not os.path.exists(pdf_path):
        print(f"错误：找不到文件 {pdf_path}")
        return

    # 自动生成Word路径
    if word_path is None:
        word_path = os.path.splitext(pdf_path)[0] + ".docx"

    try:
        # 旧版本写法：手动创建+关闭，不用with语句
        cv = Converter(pdf_path)
        cv.convert(word_path, start=0, end=None)  # 转换所有页
        cv.close()  # 手动关闭转换器
        print(f"转换成功！Word文件已保存至：{word_path}")
    except Exception as e:
        print(f"转换失败：{str(e)}")


# 调用示例（替换为你的PDF绝对路径）
if __name__ == "__main__":
    # 务必用绝对路径，比如：
    pdf_to_word("D:/C-language/自动控制原理/实验/20220954 李方乔.pdf")  # Windows写法
    # pdf_to_word("/Users/你的名字/Desktop/test.pdf")  # Mac/Linux写法