import re

with open('q.txt', 'r', encoding='utf-8') as file:
    content = file.read()

pattern = re.compile(
    r'(单选|多选|是非|填空|简答)\n*(\d+)\n*(?:回答正确|回答错误)?\n*(.+?)\n*你的答案\n*(.*?)(?=单选|多选|是非|填空|简答|$)',
    re.DOTALL)

matches = pattern.findall(content)

for match in matches:
    if match[0] == '是非':
        print(f'{match[1]}.{match[2]}')
        sf_pattern = re.compile(r'正确答案\n*([A-Z])\n*')
        sf_matches = sf_pattern.findall(match[3])
        print(f'答案:{"对" if sf_matches[0] == "A" else "错"}')
    elif match[0] == '单选':
        print(f'{match[1]}.{match[2]}')
        dx_pattern = re.compile(
            r'\n*[A-Z]\n(.*)\n*(?:正确|错误)?(?:\n*)*\n*[A-Z]\n(.*)\n*(?:正确|错误)?(?:\n*)*\n*[A-Z]\n(.*)\n*(?:正确|错误)?(?:\n*)*\n*[A-Z]\n(.*)\n*(?:正确|错误)?(?:\n*)*正确答案\n(.*)\n*')
        dx_matches = dx_pattern.findall(match[3])
        print(f'A. {dx_matches[0][0]}')
        print(f'B. {dx_matches[0][1]}')
        print(f'C. {dx_matches[0][2]}')
        print(f'D. {dx_matches[0][3]}')
        print(f'答案:{dx_matches[0][4]}')

    elif match[0] == '多选':
        print(f'{match[1]}.{match[2]}')
        dx_pattern = re.compile(
            r'\n*[A-Z]\n(.*)\n(?:正确|错误)?(?:\n)*[A-Z]\n(.*)\n(?:正确|错误)?(?:\n)*[A-Z]\n(.*)\n(?:正确|错误)?(?:\n)*[A-Z]\n(.*)\n(?:正确|错误)?(?:\n)*正确答案\n(.*)\n*')
        dx_matches = dx_pattern.findall(match[3])
        print(f'A. {dx_matches[0][0]}')
        print(f'B. {dx_matches[0][1]}')
        print(f'C. {dx_matches[0][2]}')
        print(f'D. {dx_matches[0][3]}')
        print(f'答案:{dx_matches[0][4].replace(" ", "")}')

    elif match[0] == '填空':
        # if match[1] == '27':
        #     print(f'{match[1]}.{match[2]}')
        #     print('答案: ')
        #     continue

        q = re.sub('_+', '()', match[2])
        count = q.count('()')
        ans_reg = '\n?[0-9]+\n(.*)\n?'
        reg = r'正确答案'
        for i in range(count):
            reg += ans_reg
        print(f'{match[1]}.{q}')
        dx_pattern = re.compile(reg)
        dx_matches = dx_pattern.findall(match[3])
        if type(dx_matches[0]) is tuple:
            print(f'答案: {"|".join(dx_matches[0])}')
        else:
            print(f'答案: {dx_matches[0]}')

    elif match[0] == '简答':
        print(f'{match[1]}.{match[2]}')
        dx_pattern = re.compile(
            r'参考答案\n*(.*)', re.DOTALL)
        dx_matches = dx_pattern.findall(match[3])
        ans = dx_matches[0].replace("\n", "")
        print(f'答案:{ans}')
