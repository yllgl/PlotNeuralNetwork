import os
import re
def tikz_unit_conversion(value, from_unit, to_unit):
    # 定义转换因子
    conversion_factors = {
        'pt': {'mm': 0.3514598, 'cm': 0.03514598, 'in': 1/72.27, 'pt': 1},
        'mm': {'mm': 1, 'cm': 0.1, 'in': 0.0393701, 'pt': 2.83464567},
        'cm': {'mm': 10, 'cm': 1, 'in': 0.393701, 'pt': 28.3464567},
        'in': {'mm': 25.4, 'cm': 2.54, 'in': 1, 'pt': 72.27},
    }

    # 检查输入单位和输出单位是否有效
    if from_unit not in conversion_factors:
        raise ValueError(f"Invalid from_unit: {from_unit}")

    if to_unit not in conversion_factors[from_unit]:
        raise ValueError(f"Invalid to_unit: {to_unit}")

    # 计算转换后的值
    converted_value = value * conversion_factors[from_unit][to_unit]

    return converted_value
def get_unit_and_number(value):
    # 从字符串中提取单位和数值
    unit = ""
    number = ""
    for char in value:
        if char.isdigit() or char == '.' or char == '-':
            number += char
        elif char.isalpha():
            unit += char
    return unit, number
def change_to_cm(value,default_unit="cm"):
    # 将输入值转换为毫米
    unit, number = get_unit_and_number(value)
    if unit == "":
        unit = default_unit
    return tikz_unit_conversion(float(number), unit, "cm")
def check_isdigit(input):
    if not isinstance(input,str):
        input = str(input)
    if input[0]=='(' and input[-1]==')':
        input = input[1:-1]
    if ',' in input:
        input = input.split(',')
        for i in input:
            if re.match(r'^-?[0-9]+[0-9a-z\.]?$',i.strip()) is None:
                return False
        return True
    else:
        if re.match(r'^-?[0-9]+[0-9a-z\.]?$',input.strip()) is None:
            return False
        return True
def get_digit_tuple(input):
    if not isinstance(input,str):
        input = str(input)
    if input[0]=='(' and input[-1]==')':
        input = input[1:-1]
    if ',' in input:
        out = []
        input = input.split(',')
        for i in input:
            out.append((i.strip()))
        return tuple(out)
    else:
        return ((input),)
def returnStrList(input):
    if isinstance(input,str) or isinstance(input,int) or isinstance(input,float):
        input = [input]
    for i in input:
        if not isinstance(i,str):
            if isinstance(i,int) or isinstance(i,float):
                yield f'{i}'
            else:
                raise TypeError(f"input must be str or int or float get {type(i)}")
        else:
            if i.strip()=="":
                yield '" "'
            else:
                yield f'"{i}"'