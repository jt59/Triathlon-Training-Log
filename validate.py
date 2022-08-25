#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 19:49:46 2022

@author: Jillian
"""

import re

def validate_input(user_input, valid_options):
    """
    Validates that the user entered a valid action choice

    Returns
    -------
    Boolean, true or false depending on entry validity

    """
    if user_input in valid_options:
        return True
    else:
        print("\nError: Entry not valid. Please enter a number in the range provided.")
        return False
    
def validate_date(date_input):
    """
    

    Parameters
    ----------
    date_input : string
        Date in MM/DD/YYYY format

    Returns
    -------
    Boolean, true or false depending on entry validity

    """
    date_pattern = "^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"
    if re.match(date_pattern, date_input):
        return True
    else:
        print("\nError: Please enter a date in the required MM/DD/YYYY format.")
        return False
    
def validate_float(float_input):
    """
    

    Parameters
    ----------
    float_input : string
        string corresponding to the workout duration

    Returns
    -------
    Boolean, true or false depending on entry validity

    """
    success = 0
    try:
        num = float(float_input)
        success = 1
    except:
        print("\nError: Please enter a number greater than zero. Do not include any other text.")
        return False
    if success == 1:
        if num > 0:
            return True
        else:
            print("\nError: Please enter a number greater than zero.")
            return False
        
def validate_entry_num(entry_num, log_len):
    """
    

    Parameters
    ----------
    entry_num : int
        integer corresponding to an existing log entry ID number
    log_len : int
        length of the log

    Returns
    -------
    Boolean, true or false depending on entry validity

    """
    success = 0
    try:
        entry_num = int(entry_num)
        success = 1
    except:
        print("\nError: Please enter an integer only.")
        return False
    if success == 1:
        if entry_num > log_len or log_len < 1:
            print("\nError: The ID you entered is not valid.")
            return False
    return True

def validate_yn(yn_str):
    """
    

    Parameters
    ----------
    yn_str : string
        y or n corresponding to yes or no

    Returns
    -------
    Boolean, true or false depending on entry validity

    """
    if yn_str[0] in ('y','n'):
        return True
    else:
        print("\nError: Please enter either 'y' or 'n'.")
        return False
        
    
            
    
