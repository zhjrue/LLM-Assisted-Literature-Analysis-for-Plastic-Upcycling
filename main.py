import sys, time
from api_LLM import class_API, txt_answers_output, find_txts


def main(analyzed_text, model_name='qwen-plus-2024-12-20'):
    """_summary_

    Args:
        analyzed_text (str): 提示语
        model_name (str, optional): 设置模型. Defaults to 'qwen-plus-2024-12-20'.
    """
    txt_fold = "data/txts/"    ##### 设置输入文件夹路径
    sleep_time = 4    ##### 设置延迟时间

    files = find_txts(txt_fold)
    print(f'{txt_fold}中共有{len(files)}个txt文件。\n')
    # files = files[:10]    ##### 调节分析范围（用于测试）

    print('')
    condition = input('输入yes开始分析：')
    print('')

    if condition != 'yes':
        sys.exit()

    answers = []
    processing_time, processing_times = 0, 0

    api = class_API(
            model_name=model_name,    ### 设置模型类型
            system_guidance='You are a helpful assistant, who knows a lot about plastic upcycling.',    ### 设置提示语
            seed=20020506, temperature=0    ### 设置模型参数
        )

    for file in files:

        print(file)

        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

        api.API_analysis(
            analyzed_text= f'{analyzed_text}\n\n{text}'
        )  ##### 设置prompt
        api.API_print()

        answers.append(api.answer)
        processing_time += api.time_consume
        processing_times += 1

        time.sleep(sleep_time)


    log_date = input("日志创建日期（六位）：")
    output_path = "your_path"    ##### 设置输出文件路径
    log_fold_path = output_path + "/" + log_date

    txt_answers_output(log_fold_path, answers)

    print(f'运行结束！\n本次共分分析了{processing_times}篇文章，分析耗时{processing_time / 60:.2f}分钟，'
        f'延迟耗时{sleep_time * processing_times / 60:.2f}分钟。')



if __name__ == "__main__":
    # # cate_API_plus.py
    # main(
    #     analyzed_text='Later, I will show you a chemical literature focused on plastic upcycling. '
    #                   'After reading it, please tell me which area or areas this literature is related to. '
    #                   'Your answer can only be one or some of the following eleven options: chemistry, engineering, '
    #                   'environmental science, materials science, science technology, business economics, energy fuels, '
    #                   'polymer science, physics, public environmental occupational health, others. '
    #                   'Just give the answer, do not explain your answer. \n\n'
    #                   'Here comes to the text:',
    #     model_name='qwen-plus-2024-12-20'
    # )

    # # prod_API_max.py
    # main(
    #     analyzed_text='Later, I will show you a chemical literature focused on plastic upcycling. '
    #                   'After reading it, please tell me what kind or kinds of valuable product are obtained in this '
    #                   'literature. '
    #                   'Your answer can only be one or some of the following eight options: carbon monoxide, hydrogen, '
    #                   'hydrocarbons, polymer materials, carbon materials, small organic molecules with oxygen atom, '
    #                   'monomers of the original plastic, others. '
    #                   'If the information is not provided or you are unsure, use "N/A" instead. Just give the answer, '
    #                   'do not explain your answer. \n\n'
    #                   'Here comes to the text:',
    #     model_name='qwen-max-2024-09-19' 
    # )

    # # react_API_max.py
    # main(
    #     analyzed_text='Later, I will show you a chemical literature focused on plastic upcycling. '
    #                   'After reading it, please tell me what kind or kinds of plastic are upcycled in this literature. '
    #                   'Your answer can only be one or some of the following seven options: polyethylene, polypropylene, '
    #                   'polyvinyl chloride, polyethylene terephthalate, polystyrene, polyurethane, others. '
    #                   'If the information is not provided or you are unsure, use "N/A" instead. Just give the answer, '
    #                   'do not explain your answer. \n\n'
    #                   'Here comes to the text:',
    #     model_name='qwen-max-2024-09-19'
    # )

    # # route_API_max.py
    # main(
    #     analyzed_text='Later, I will show you a chemical literature focused on plastic upcycling. '
    #                  'After reading it, please tell me which category this upcycling process falls into. '
    #                   'Your answer can only be one of the following six options: mechanical process, chemical process '
    #                   'with catalyst, chemical process without catalyst, biological process, hybrid process, others. '
    #                   'If the information is not provided or you are unsure, use "N/A" instead. Just give the answer, '
    #                   'do not explain your answer. \n\n'
    #                   'Here comes to the text:',
    #     model_name='qwen-max-2024-09-19'
    # )

    main("测试", model_name='qwen-plus-2024-12-20')
