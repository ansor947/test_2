import re
import operator 


def compare(string: str) -> str:
    pattern = r"(\W?\d+)(\W)(\W?\d+)"

    string_reg = re.split(pattern, string)
    for element in string_reg:
        if element == '':
            string_reg.remove(element)
            if string_reg[1] == '<':
                result = operator.lt(string_reg[0], string_reg[2])
            elif string_reg[1] == '>':
                result = operator.gt(string_reg[0], string_reg[2])
    return result


# print(compare('548>787'))
# print(compare('-758<-978'))
# print(compare('758>-978'))
# print(compare('758<-978'))


