# LLM-Assisted Literature Analysis for Plastic Upcycling
提供“LLM-Assisted Literature Analysis for Plastic Upcycling”一文中使用到的`python`代码

python codes for "LLM-Assisted Literature Analysis for Plastic Upcycling"
***
## pdf2txt.py
- `pdf2txt.py`借助`fitz`提取pdf文件中的文本并将其写入txt文件中，方便后续直接输入给大语言模型。
- `pdf2txt.py`无法识别某些非英文文献以及英语文献中的某些字体，不过这样的例子在本工作中非常之少，不影响最终得到的统计性规律。
- 对于较长的、无法一次性提供给大语言模型的txt文件，可以人工删除其中不重要的文本（如Reference部分）或将其分成两部分依次输入给大语言模型。
- `pdf2txt.py` utilizes `fitz` to extract text from pdf files and writes it into a txt file, facilitating subsequent input to LLMs.
- Certain non-English literatures and specific fonts within English literatures may not be recognized through `pdf2txt.py`. (Such instances are exceedingly rare in this work and do not affect the final statistical patterns.)
- For lengthy txt files that cannot be fed into LLM in one go, one can manually remove less important text (*e.g.*, Reference section) or split the file into two parts for sequential input to LLM.
## api_LLM.py
- `api_LLM.py`定义了函数`txt_answers_output`、`json_infos_output`、`find_txts`，用于实现基本的文件读写等操作；还定义了类`class_API`，通过调用阿里云旗下大语言模型的API获取有关文献分析的信息。
- 使用时，应将`api_LLM.py`文件放置于python的项目文件夹中，以方便对其进行导入。
- `api_LLM.py` defines functions such as `txt_answers_output`, `json_infos_output`, and `find_txts` to handle basic file operations like reading and writing. It also defines the `class_API` class, which interfaces with the API of LLMs from Alibaba Cloud to retrieve information for literature analysis.
- One should place the `api_LLM.py` file within your Python project directory for direct import.
## cate_API_plus.py、reac_API_max.py、route_API_max.py、prod_API_max.py
- 通过导入`api_LLM.py`中的函数与类调用指定大语言模型的API，对文献进行分析，并将分析结果写入日志。
- 通过调整`class_API`中的`model_name`、`system_guidance`、`seed、temperature`参数以及`API_analysis`中的`analyzed_text`参数，用户可以在特定的场景下调用指定的大语言模型对自己感兴趣的问题进行分析。
- These scripts import functions and classes from `api_LLM.py` to invoke the specified large language model's API for literature analysis and log the analysis results.
- By adjusting parameters such as `model_name`, `system_guidance`, `seed`, `temperature` in `class_API`, and `analyzed_text` in `API_analysis`, users can tailor the LLMs' API calls to analyze specific questions of interest in particular scenarios.
