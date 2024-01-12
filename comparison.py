import re
import operator 


def compare(string: str) -> str:
    pattern = r"(\W?\d+)(\W)(\W?\d+)" 
    string_reg = re.split(pattern, string)
    for element in string_reg:
        if element == '':
            string_reg.remove(element)
            if string_reg[1] == '<':
                result = operator.lt(int(string_reg[0]), int(string_reg[2]))
            elif string_reg[1] == '>':
                result = operator.gt(int(string_reg[0]), int(string_reg[2]))

    return result


# print(compare('112>12'))
# print(compare('-758<-978'))
# print(compare('758>-978'))
# print(compare('758<-978'))


