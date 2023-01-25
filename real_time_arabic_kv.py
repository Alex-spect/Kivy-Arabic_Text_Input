# -*- coding: utf-8 -*-

# Kivy Arabic Text Input is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

# Written by Eng.Ali Taher Al_Iraqi
# Email: ali.altaher.h@gmail.com

from arabic_reshaper import reshape     #pip install arabic_reshaper
from bidi.algorithm import get_display  #pip install python_bidi

###########################################################################

"""
Kivy Arabic Text Input by Eng.Ali Taher Al_Iraqi
is licensed under a
Creative Commons Attribution-ShareAlike 4.0 International License.

"""
def str_dif(str1:str,str2:str) -> (str,int):
    """
        This function takes two strings as input 
        this function compare two strings and 
        return difference between strings and num
        refers that who string is longer 
        if num =1 1st string longer if = 2
        then 2nd string longer if ==0 then 
        the strings have same length
        How to Use:
        var1,var2 = str_def(str1,str2)
        var1 handle difference string
        var2 handle num to indicate who is longer
    """    
    who_is_longer = 0  # 0 equal length : 1 str1 longer : 2 str2 longer

###########################################################################
    long_str = str1 if len(str1) >= len(str2) else str2
    if str1 != str2:
        
        if len(str1) > len(str2):
            who_is_longer = 1
        elif len(str2) > len(str1):
            who_is_longer = 2
            
    short_str = str1 if len(str1) >= len(str2) else str1
    str_deff=""  # Holding the substring Which represents the difference between 2 strings
    for c,i in enumerate(long_str):
        if(c>=len(short_str)):
            str_deff +=i
            
    return str_deff,who_is_longer



###########################################################################
logger=""
def arabi_txt_in(txt_input_val):
        """
        This function takes the text of the input_text box and returns
        a reshaped version of the text that is normally viewable on the
        requirements.txt
        
        """
        global logger
         
        reversed_str = get_display(reshape(logger))
        diff,k = str_dif(reversed_str,txt_input_val)
        if k == 1 :
            
            logger = logger[:len(logger)-1]
           
        if k ==2:
            logger+=diff
        # if k ==0:    
        txt_input_val = get_display(reshape(logger))
        
        
        #print("Logger : ",logger)
        print("Difference : ",diff)
        return txt_input_val,logger
####################################################################
    
