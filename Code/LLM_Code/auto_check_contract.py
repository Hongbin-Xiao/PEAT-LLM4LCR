def contract_base_check(text, model_name='gpt-4'):  # content1 为合同的txt文本，model_name为要使用的模型名称。函数返回为建议的txt文本

    print('suggest1：运行中')

    import json
    import os
    import re
    from openai import OpenAI
    content1 = text
    with open(os.getcwd() + '/model/promot/review.txt', 'r', encoding='utf-8') as file:
        content2 = file.read()
    # 打开并读取JSON文件
    with open(os.getcwd() + '/model/promot/action_items_change.json', 'r', encoding='utf-8') as file:
        promt_one = json.load(file)

    os.environ["http_proxy"] = "http://127.0.0.1:7890"  # 指定代理，解决连接问题
    os.environ["https_proxy"] = "http://127.0.0.1:7890"  # 指定代理，解决连接问题

    client = OpenAI(api_key="****")
    suggestion = ""
    for i1 in range(0, len(promt_one)):
        data = content2.replace("${" + 'content' + "}", content1)
        matches = re.findall(r"(?<=\${).*?(?=\})", content2)
        for i in matches:
            if i == 'action_item':
                data = data.replace("${" + i + "}", promt_one[i1]['action_item'])
            if i == 'condition':
                data = data.replace("${" + i + "}", promt_one[i1]['condition'])
            if i == 'risk':
                data = data.replace("${" + i + "}", promt_one[i1]['risk'])
            if i == 'solution':
                data = data.replace("${" + i + "}", promt_one[i1]['solution'])
        client.base_url = "https://ai-yyds.com/v1"
        completion = client.chat.completions.create(model=model_name, messages=[{"role": "user", "content": data}])
        # response_format={"type": }
        suggestion = suggestion + '\n' + '审核条款编号:' + '####' + promt_one[i1]['index'] + '####' + '\n审核款项：' + \
                     promt_one[i1]['category'] + '\n' + '审核目标：' + promt_one[i1]["action"] + '\n' + '建议：' + \
                     completion.choices[0].message.content + '\n'
    return suggestion


def contract_base_jude(text, model_name='gpt-4'):  # content1 为合同的txt文本，model_name为要使用的模型名称。函数返回为建议的txt文本

    print('suggest2：运行中')

    import json
    import os
    import re
    from openai import OpenAI
    content1 = text
    with open(os.getcwd() + '/model/promot/judge.txt', 'r', encoding='utf-8') as file:
        content2 = file.read()
    # 打开并读取JSON文件
    with open(os.getcwd() + '/model/promot/judgement_items.json', 'r', encoding='utf-8') as file:
        promt_one = json.load(file)

    os.environ["http_proxy"] = "http://127.0.0.1:7890"  # 指定代理，解决连接问题
    os.environ["https_proxy"] = "http://127.0.0.1:7890"  # 指定代理，解决连接问题
    client = OpenAI(api_key="******")
    suggestion = ""
    for i1 in range(0, len(promt_one)):
        data = content2.replace("${" + 'content' + "}", content1)
        matches = re.findall(r"(?<=\${).*?(?=\})", content2)
        for i in matches:
            if i == 'purpose':
                data = data.replace("${" + i + "}", promt_one[i1]['purpose'])
            if i == 'condition':
                data = data.replace("${" + i + "}", promt_one[i1]['condition'])
            if i == 'task':
                data = data.replace("${" + i + "}", promt_one[i1]['task'])
        client.base_url = "https://ai-yyds.com/v1"
        completion = client.chat.completions.create(model=model_name, messages=[{"role": "user", "content": data}])
        # response_format={"type": }
        suggestion = suggestion + '\n' + '提取条款编号:' + '####' + promt_one[i1]['index'] + '####' + '\n待审核款项：' + \
                     promt_one[i1]['category'] + '\n' + '待审核目标：' + promt_one[i1]["purpose"] + '\n' + '建议：' + \
                     completion.choices[0].message.content + '\n'
    return suggestion


def contract_base_part_check(text, model_name='gpt-4'):  # content1 为合同的txt文本，model_name为要使用的模型名称。函数返回为建议的txt文本

    print('suggest3：运行中')

    import json
    import os
    import re
    from openai import OpenAI
    content1 = text
    with open(os.getcwd() + '/model/promot/customized_review.txt', 'r', encoding='utf-8') as file:
        content2 = file.read()
    # 打开并读取JSON文件
    with open(os.getcwd() + '/model/promot/customized_action_items.json', 'r', encoding='utf-8') as file:
        promt_one = json.load(file)

    os.environ["http_proxy"] = "http://127.0.0.1:7890"  # 指定代理，解决连接问题
    os.environ["https_proxy"] = "http://127.0.0.1:7890"  # 指定代理，解决连接问题
    client = OpenAI(api_key="******")
    suggestion = ""
    for i1 in range(0, len(promt_one)):
        data = content2.replace("${" + 'content' + "}", content1)
        matches = re.findall(r"(?<=\${).*?(?=\})", content2)
        for i in matches:
            if i == 'action_item':
                data = data.replace("${" + i + "}", promt_one[i1]['action_item'])
            if i == 'customized_prompt':
                data = data.replace("${" + i + "}", promt_one[i1]['customized_prompt'])

        client.base_url = "https://ai-yyds.com/v1"
        completion = client.chat.completions.create(model=model_name, messages=[{"role": "user", "content": data}])
        # response_format={"type": }
        suggestion = suggestion + '\n' + '审核条款编号:' + '####' + promt_one[i1]['index'] + '####' + '\n审核款项：' + \
                     promt_one[i1]['category'] + '\n' + '审核目标：' + promt_one[i1]["action"] + '\n' + '建议：' + \
                     completion.choices[0].message.content + '\n'
    return suggestion


def contract_base_ip(text, model_name='gpt-4'):  # content1 为合同的txt文本，model_name为要使用的模型名称。函数返回为建议的txt文本

    print('suggest4：运行中')

    import json
    import os
    import re
    from openai import OpenAI
    content1 = text
    with open(os.getcwd() + '/model/promot/ip_determine.txt', 'r', encoding='utf-8') as file:
        content2 = file.read()
    # 打开并读取JSON文件
    with open(os.getcwd() + '/model/promot/ip_graph_nodes.json', 'r', encoding='utf-8') as file:
        promt_one = json.load(file)
    os.environ["http_proxy"] = "http://127.0.0.1:7890"  # 指定代理，解决连接问题
    os.environ["https_proxy"] = "http://127.0.0.1:7890"  # 指定代理，解决连接问题
    client = OpenAI(api_key="******")
    suggestion = ""
    for i1 in range(0, len(promt_one)):
        data = content2.replace("${" + 'content' + "}", content1)
        matches = re.findall(r"(?<=\${).*?(?=\})", content2)
        for i in matches:
            if i == 'purpose':
                data = data.replace("${" + i + "}", promt_one[i1]['purpose'])
            if i == 'attention':
                data = data.replace("${" + i + "}", promt_one[i1]['attention'])
            if i == 'task':
                data = data.replace("${" + i + "}", promt_one[i1]['task'])
            if i == 'output':
                data = data.replace("${" + i + "}", promt_one[i1]['output'])

        client.base_url = "https://ai-yyds.com/v1"
        completion = client.chat.completions.create(model=model_name, messages=[{"role": "user", "content": data}])
        # response_format={"type": }
        suggestion = suggestion + '\n' + '审核条款编号:' + '####' + promt_one[i1]['index'] + '####' + '\n审核款项：' + \
                     promt_one[i1]['category'] + '\n' + '审核目标：' + promt_one[i1]["purpose"] + '\n' + '建议：' + \
                     completion.choices[0].message.content + '\n'
    return suggestion


def check_contract(text, model_name='gpt-4'):
    suggest1 = contract_base_check(text, model_name)
    print('suggest1：运行完成')

    suggest2 = contract_base_jude(text, model_name)
    print('suggest2：运行完成')

    suggest3 = contract_base_part_check(text, model_name)
    print('suggest3：运行完成')

    suggest4 = contract_base_ip(text, model_name)
    print('suggest4：运行完成')


    with open('审核建议.txt', 'w') as f:
        f.write(suggest1)
    with open('辅助审核款项.txt', 'w') as f:
        f.write(suggest2)
    with open('知识产权审核建议.txt', 'w') as f:
        f.write(suggest3)
    with open('审核分项建议.txt', 'w') as f:
        f.write(suggest4)

    return [suggest1, suggest2, suggest3, suggest4]
    # return [{'主体与基本要素建议': suggest1}, {'高风险建议': suggest2}, {'核心条款': suggest3}, {'知识产权': suggest4}]
