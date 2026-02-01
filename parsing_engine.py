#This file is responsible for parsing the provided text file and organizing the system accordingly for prediction and simulations

#Remove the self. for all of the iterables that I justa added and have the methods feed the other method I need through the final method argument itself


import sys 
import sympy as sp

class parsing_engine:

    def __init__(self, text_file):

        self.tf = text_file
        print("Parsing the file you provided.")
        with open(self.tf) as tf:
            self.line_list = tf.readlines()

    def sympy_initializer(self, iterable):
        for var in iterable:
            sp.Symbol(var)

    #START HERE TOMORROW - BEGIN BY FIXING THE PROBLEMS RESULTING FROM SWAPPING OF SET FOR LIST IN CHAR GATHERING
    def static_init_parser(self, required_command: str):

        self.static_init_ls = []
        command_line = None
            
        for line in self.line_list:
            
            str_line = str(line)
            if required_command in str_line and ";" in str_line:
                command_line = str_line.strip()
                break

            
        if command_line == None:

            sys.exit(f"{required_command} line was not located. Did you use the {required_command} command with a semicolon? It must be in the following format,{required_command} x y z;")
        
        prev_char = ""

        for indx, char in enumerate(command_line):
            print(char)
            print(prev_char)
            

            if indx+1 <= len(required_command):
                continue

            elif char.strip() != "" and prev_char.strip() == "":
                self.static_init_ls.append(char)
                
            elif char.strip() != "" and prev_char.strip() != "":
                 self.static_init_ls.remove(prev_char)
                 combined_var = prev_char + char
                 self.static_init_ls.append(combined_var)
                 prev_char = combined_var
                 continue
                    

            prev_char = char 

        for variable in static_init_ls:
            if ";" in variable:
                no_sl = variable.replace(";", "")
                final_no_sl = no_sl.strip()
                self.static_init_ls.remove(variable)
                self.static_init_ls.append(final_no_sl)
        
        if "" in self.static_init_ls:
            self.static_init_ls.remove("")

        return self.static_init_ls

    def var_collect(self):

        var_ls = parsing_engine.static_init_parser(self, "var")
        return var_ls
        
    def varexo_collect(self):

        varexo_ls = parsing_engine.static_init_parser(self, "varexo")
        return varexo_ls

    def parameter_collect(self):

        self.parameter_ls = parsing_engine.static_init_parser(self, "parameters")
        return self.parameter_ls

    def parameter_define(self):

        self.param_define_dict = {}

        for line in self.line_list:
            str_line = str(line)
            for parameter in self.parameter_ls:
                if parameter in str_line and ";" in str_line and "parameters" not in str_line:
                    no_param_line = str_line.replace(parameter, "")
                    no_param_eq_line = no_param_line.replace("=", "")
                    no_sc_line = no_param_eq_line.replace(";", "")
                    no_comment_line = no_sc_line.split("/")[0]
                    value = no_comment_line.strip()
                    self.param_define_dict[parameter] = float(value)
            
            if len(self.param_define_dict) == 3:
                break
                
        return self.param_define_dict
            

    def model_collect(self):
        
        eq_dict = {}
        

        for iterable_item in []
        

        for line in self.line_list:
            str_line = str(line)
            if "model;" in str_line:
                min_index = self.line_list.index(line)
            if "end;" in str_line and min_index != None:
                max_index = self.line_list.index(line)

        model_list = self.line_list[min_index+1:max_index]

        for counter, line in enumerate(model_list):
            str_line = str(line)
            if ";" in str_line:
                lhs_carrot = str_line.split("=")[0].strip()
                lhs = lhs_carrot.replace("^", "**")
                rhs_sc_carrot = str_line.split("=")[1].strip()
                rhs_carrot = rhs_sc_carrot.replace(";", "")
                rhs = rhs_carrot.replace("^", "**")
                eq_dict[f"Equation {counter}"] = sp.Eq(lhs, rhs)

        return eq_dict

        

is_a_test = True
if is_a_test == True:
    temp_instance = parsing_engine(r"example_solveconn_textfile.txt")
    set_one = temp_instance.var_collect()
    print(set_one)
    set_two = temp_instance.varexo_collect()
    print(set_two)
    set_three = temp_instance.parameter_collect()
    print(set_three)
    set_four = temp_instance.parameter_define()
    print(set_four)
    set_five = temp_instance.model_collect()
    print(set_five)




