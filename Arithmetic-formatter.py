############################################
#
#   arithmetic_arranger(problems)
#       input: List of problems
#              Boolean; show or not results
#       output: String
#   Supports only + and - Operations 
#   
#   Max_number of problems : 5
#   Max_number digits : 4 
#
#############################################

import re
import operator
from functools import reduce

def arithmetic_arranger(problems,show_result=False):
    
    try:
        output_array = []
        if len(problems)>5:
            raise Exception("Too many problems.")

        for x in problems:

            symbol  = re.findall('[+-]',x)
            
            if symbol == []:
                raise Exception("Operator must be '+' or '-'.")

            numbers = re.split('[+-]',x.replace(" ",""))
            symbol  = symbol[0]

            if len([True for x in numbers if x.isnumeric()]) != 2:
                raise Exception("Numbers must only contain digits.")

            numbers = list(map(lambda x: int(x),numbers))

            if symbol == "+":
                result = reduce(operator.__add__, numbers)

            else:
                result = reduce(operator.__sub__, numbers)

            max_len = len(str(max(numbers)))

            if max_len > 4:
                raise Exception("Numbers cannot be more than four digits.")
            
            output = {
            "first_number" : numbers[0],
            "second_number": numbers[1],
            "symbol"       : symbol,
            "result"       : result,
            "max_len"      : max_len
            }
            output_array.append(output)

        # Print results
        line_one   = ""
        line_two   = ""
        line_three = ""
        line_four  = ""
        space      = " "*4

        for x in output_array:

            f_num   = x["first_number"]
            f_len   = x["max_len"] + 2 - len(str(f_num))
            s_num   = x["second_number"]
            s_len   = x["max_len"] + 1 - len(str(s_num))
            sym     = x["symbol"]
            result  = x["result"]
            max_len = x["max_len"]

            line_one   += f"{' '*f_len}{f_num}{space}"
            line_two   += f"{sym}{' '*s_len}{s_num}{space}"
            line_three += f"{'-'*(max_len+2)}{space}"
            line_four  += f"{' '*2}{result}{space}"

        if show_result:
            string = line_one+"\n"+line_two+"\n"+line_three+"\n"+line_four
        else:
            string = line_one+"\n"+line_two+"\n"+line_three

        print(string)
    
    except Exception as e:
        print(e)
        

arithmetic_arranger(["32 + 62", "380", "45 + 43"])