#This file is responsible for parsing the provided text file and organizing the system accordingly for prediction and simulations

import sys 

class parsing_engine:

    def __init__(self, text_file):

        self.tf = text_file
        print("Parsing the file you provided.")
    

    #START HERE TOMORROW - BEGIN BY FIXING THE PROBLEMS RESULTING FROM SWAPPING OF SET FOR LIST IN CHAR GATHERING
    def static_init_parser(self, required_command: str):

        static_init_set = []
        command_line = None
    
        with open(self.tf) as tf:
            line_list = tf.readlines()
            
        for line in line_list:
            
            str_line = str(line)
            if required_command in str_line and ";" in str_line:
                command_line = str_line.strip()
                break

            
        if command_line == None:

            sys.exit(f"{required_command} line was not located. Did you use the {required_command} command with a semicolon? It must be in the following format,{required_command} x y z;")
        
        prev_char = ""

        for indx, char in enumerate(command_line):
            print(char)
            

            if indx+1 <= len(required_command):
                continue

            elif char.strip() != "" and prev_char.strip() == "":
                static_init_set.append(char)
                
            elif char.strip() != "" and prev_char.strip() != "":
                 static_init_set.remove(prev_char)
                 combined_var = prev_char + char
                 static_init_set.append(combined_var)
            
            prev_char = char 

        for variable in static_init_set:
            if ";" in variable:
                no_sl = variable.replace(";", "")
                final_no_sl = no_sl.strip()
                static_init_set.remove(variable)
                static_init_set.append(final_no_sl)
        
        if "" in static_init_set:
            static_init_set.remove("")

        return static_init_set

    def var_collect(self):

        var_set = parsing_engine.static_init_parser(self, "var")
        return var_set
        
    def varexo_collect(self):

        varexo_set = parsing_engine.static_init_parser(self, "varexo")
        return varexo_set

    def parameter_collect(self):

        parameter_set = parsing_engine.static_init_parser(self, "parameters")
        return parameter_set


is_a_test = True
if is_a_test == True:
    temp_instance = parsing_engine(r"example_solveconn_textfile.txt")
    set_one = temp_instance.var_collect()
    print(set_one)
    set_two = temp_instance.varexo_collect()
    print(set_two)
    set_three = temp_instance.parameter_collect()
    print(set_three)






