import os, time, json
from openai import OpenAI


def txt_answers_output(fold_path, contents):
    """将 contents 中的回答写入txt文件"""

    log_name = input("请输入txt日志名：")

    time_str = str(time.strftime('%Y%m%d%H%M%S', time.localtime()))
    file_path = fold_path + '/' + f'{log_name}' + f"log{time_str}.txt"

    with open(file_path, 'a', encoding='utf-8') as f:
        for content in contents:
            f.write(content)
            f.write("\n------\n")  # 分割线


def json_infos_output(fold_path, datas):
    """将更新后的 datas 写入json文件"""

    log_name = input("请输入json日志名：")

    time_str = str(time.strftime('%Y%m%d%H%M%S', time.localtime()))
    file_path = fold_path + '/' + f'{log_name}' + f"log{time_str}.json"

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(datas, f, indent=4, ensure_ascii=False)


def find_txts(directory_path):
    """获取 directory_path 下所有txt文件的路径"""

    file_infos = []

    for file_name in os.listdir(directory_path):

        file_path = os.path.join(directory_path, file_name)

        if os.path.isfile(file_path):

            if os.path.splitext(file_name)[1].lower()  == '.txt':
                file_infos.append(file_path)

    return file_infos


class class_API:

    def __init__(
            self,
            model_name='qwen-turbo',
            system_guidance='You are a helpful assistant.',
            seed=20020506, temperature=0
    ):
        """初始化信息：模型名称、系统指令、待分析文本、模型种子、模型温度"""

        self.model_name = model_name
        self.system_guidance = system_guidance
        self.seed = seed
        self.temperature = temperature

        self.client = OpenAI(
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )    # 换用其它设备或其它大语言模型时需要进行修改

        self.analyzed_text = None
        self.time_consume = None
        self.answer = None

    def API_analysis(self, analyzed_text='Tell me who you are in just one sentence.'):
        """按照提示词进行分析，输出分析时间和分析结果"""

        self.analyzed_text = analyzed_text

        startTime = time.time()  # 计时开始

        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {'role': 'system', 'content': self.system_guidance},
                {'role': 'user', 'content': self.analyzed_text}
            ],
            seed=self.seed,
            temperature=self.temperature
        )

        time_consume = time.time() - startTime

        self.time_consume = time_consume
        self.answer = completion.choices[0].message.content

    def API_print(self):
        """打印提示词、分析结果、分析时间"""

        # print(f'我的问题是：{self.analyzed_text}\n')
        print(f'{self.model_name}的回答是：{self.answer}\n')
        print(f'本次分析的耗时为：{self.time_consume}\n')

'''
api = class_API()
api.API_print()
'''
if __name__ == "__main__":
    api = class_API()
    api.API_print()
