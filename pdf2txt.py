import os, re, time, fitz


def process_pdf(pdf_file_path):
    """将位于 pdf_file_path 处的pdf文件转化为字符串"""

    file_name_full = os.path.basename(pdf_file_path)
    print(file_name_full)    # 文件名 + 拓展名

    file_name = os.path.splitext(file_name_full)[0]    # 文件名

    doc = fitz.open(pdf_file_path)
    raw = ''

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        raw += page.get_text()

    return [file_name, raw]


def list_files_in_directory(directory_path):
    """获取 directory_path 下所有文件的文件名"""

    file_infos = []

    for file_name_full in os.listdir(directory_path):

        file_path = os.path.join(directory_path, file_name_full)

        if os.path.isfile(file_path):  # 判断目标是否为文件

            file_name, file_extension = os.path.splitext(file_name_full)  # 获取文件名和拓展名
            file_infos.append((file_name, file_extension))

    return file_infos


def pdf2txt_write(fold_path, file_name, content):
    """将 content 写入 fold_path 下的 file_name 文件中"""

    file_path = fold_path + "\\" + f"{file_name}.txt"

    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(content)


data_path = "your_path"    # 默认文件夹位置（建议尽可能短，否则可能超出系统识别上限）

pdf_fold = input("输入pdf文件在默认文件夹中的位置：")
txt_fold = input("输入txt文件在默认文件夹中的位置：")
print('\n')

files = list_files_in_directory(data_path + '\\' + pdf_fold)

processing_time, processing_times = 0, 0    # 总处理时间，总处理次数

for file_name, extension in files:

    if extension == '.pdf' or extension == '.PDF':

        pdf_file_path = data_path + '\\' + pdf_fold + "\\" + file_name + extension

        startTime = time.time()

        result = process_pdf(pdf_file_path)
        pdf2txt_write(data_path + '\\' + txt_fold, file_name, result[1])

        one_time = time.time() - startTime
        processing_time += one_time
        processing_times += 1

        print(f'处理时间：{one_time}秒')    # 处理时间      
        print('\n')    # 分割输出结果

print(f'运行结束！\n本次共处理了{processing_times}个pdf文件，处理耗时{processing_time}秒。')
