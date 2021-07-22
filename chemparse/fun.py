import re

# function to return index of all instances of a substring in a string
def find_all(sub, a_str):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

# functions to parse elemental formulas (handles both floats and ints)
def get_first_elem(formula):
    needed_split = False
    for char in formula:
        if formula.find(char) != 0 and (char.isupper() or char == "+" or char == "-"):
            formula = formula.split(char)[0]
            needed_split = True
            return formula, needed_split
        
        char_ind = list(find_all(char, formula))
        if len(char_ind) > 1 and (char.isupper() or char == "+" or char == "-") and (formula[1] == char or formula[1].islower()) and sum(1 for c in formula[0:char_ind[1]] if c.isupper())==1:
            formula = formula[0:char_ind[1]]
            needed_split = True
            return formula, needed_split

    return formula, needed_split

def inner_parse_formula(text):
    formula_dict = {}
    for i in range(0, len(text)):
        element = re.findall("^[a-zA-Z-+]+", text)
        if element == []:
            break
        else:
            element, needed_split = get_first_elem(element[0])
            text = text.replace(element, '', 1)
            if needed_split:
                number = 1.0
            else:
                try:
                    number = float(re.findall(r"(^(?=.)([+-]?([0-9]*)(\.([0-9]+))?)([eE][+-]?\d+)?)", text)[0][0])
                except:
                    number = 1.0
                text = re.sub(r"(^(?=.)([+-]?([0-9]*)(\.([0-9]+))?)([eE][+-]?\d+)?)", "", text)
            if element not in list(formula_dict.keys()):
                formula_dict[element] = number
            else:
                formula_dict[element] += number
    return formula_dict

def parse_formula(text):
    
    # handle parentheses in formula
    if "(" in text and ")" in text:
        parenth_list = re.findall(r"(?:\([^()]*\))?", text)
        parenth_list = [seg for seg in parenth_list if seg != '']
        seg_dict_list = []
        if len(parenth_list) != 0:
            for seg in parenth_list:
                try:
                    number = float(re.findall(r"(^(?=.)([+-]?([0-9]*)(\.([0-9]+))?)([eE][+-]?\d+)?)", text.split(seg)[-1])[0][0])
                except:
                    number = 1.0
                seg_no_parenth = seg[1:-1]
                seg_formula_dict = inner_parse_formula(seg_no_parenth)
                seg_formula_dict_mult = {k:v*number for (k,v) in seg_formula_dict.items()}
                endseg = re.sub(r"(^(?=.)([+-]?([0-9]*)(\.([0-9]+))?)([eE][+-]?\d+)?)", "", text.split(seg)[-1])
                text = text.split(seg)[0]+endseg
                seg_dict_list.append(seg_formula_dict_mult)
        seg_dict_list.append(inner_parse_formula(text))
        
        # merge and sum all segments
        if len(seg_dict_list) > 1:
            start_dict = seg_dict_list[0]
            for i in range(1, len(seg_dict_list)):
                next_dict = seg_dict_list[i]
                start_dict = { k: start_dict.get(k, 0) + next_dict.get(k, 0) for k in set(start_dict) | set(next_dict) }
            return start_dict
        else:
            return seg_dict_list[0]
    
    # if there are no parenthesis, parse formula directly
    else:
        return inner_parse_formula(text)