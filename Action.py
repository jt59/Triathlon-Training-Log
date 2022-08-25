#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jillian Turner
Class: CS 521 - Summer 2
Date: 8/20/2022
Final Project: Action Class
Description: A class representing a user's action choice
"""
import Entry
import validate
import os

class Action():
    """A class representing a user's action choice
    
    Args:
        log (list): A list of all log entries

    """
    
    __format_headers = '#        Date          Workout       Duration        Distance             Pace                      Race Distance                    Race Time \n-        ----          -------       --------        --------             ----                      -------------                    ---------'
    
    def __init__(self, log=[], test=False):
        """
        Constructor method to create an Action instance
        
        Parameters
        ----------
        log: list of log entries
        test: boolean, tells whether method is being tested

        Returns
        -------
        None.

        """
        self.__log = log
        self.max_distance_entry = []
        if not test:
            print("Welcome to your interactive half ironman training log! ")
            self.__enter_action()
        
    
    def __enter_action(self):
        """
        Prompts user to enter an action

        Returns
        -------
        None.

        """
        self.__user_action = input("\nPlease enter a number corresponding to one of the following options: \n\n(1) New Entry \n(2) Delete Entry \n(3) Edit Entry \n(4) View Entry \n(5) View Full Log\n(6) View Max Distance Entry \n(7) Exit program\n\nEnter choice here: ")
        if not validate.validate_input(self.__user_action, ('1','2','3','4','5','6','7')):
            self.__enter_action()
        else:
            self.__process_action()
            
        
        
    def __process_action(self):
        """
        Processes the action to run the method that correspons to the user's choice'

        Returns
        -------
        None.

        """
        #create new entry
        if self.__user_action == "1":
            entry = Entry.Entry()
            if entry.distance != "N/A":
                self.check_max(entry)
            self.__log.append(entry)
            print("\nWorkout logged!\n")
            print(self.__format_headers)
            print(f'{self.__log.index(entry) + 1 :<5} {entry}')
            self.__create_log_file()
            self.__enter_action()
        #delete entry
        elif self.__user_action == "2":
            self.__delete_entry()
            self.__create_log_file()
            self.__enter_action()
        #edit entry
        elif self.__user_action == "3":
            self.__edit_entry()
            self.__create_log_file()
            self.__enter_action()
        #view entry
        elif self.__user_action == "4":
            self.__view_entry()
            self.__enter_action()
        #view full log
        elif self.__user_action == "5":
            print("\nCheck your working directory for a file called my_log.txt. This file contains your full exercise log!")
            self.__enter_action()
        #view max distance entry
        elif self.__user_action == "6":
            if len(self.__log) == 0:
                print("\nYour log is currently empty. If you want to add a new entry, select New Entry.")
            elif len(self.max_distance_entry) == 0:
                print('\nYour only workout(s) are of Other type, which doees not support Max Distance functionality.')
            else:
                print(self.__format_headers)
                for e in self.max_distance_entry:
                    print(f'{self.__log.index(e) + 1 :<5} {e}')
            self.__enter_action()
        elif self.__user_action == "7":
            print("\nGoodbye and happy training!")
        else:
            print("Error")
            
    def __create_log_file(self):
        """
        Creates output file with the users full exercise log

        Returns
        -------
        None.

        """
        curr_dir = os.getcwd()
        output_file = 'my_log.txt'
        error = 0
        try: 
            file_name = os.path.join(curr_dir,output_file)
            text_file = open(file_name,'w')
        except:
            error = 1
            print('There was an error creating your log.')
        if error == 0:
            try:
                text_file.write(self.__format_headers + "\n")
                for entry in self.__log:
                    text_file.write(str(self.__log.index(entry) + 1) + "     " + entry.get_formatted_entry() + "\n\n")
            except Exception as e:
                print(e)
                print(f'There was an error writing to {output_file}.')
            text_file.close()
    
    def __edit_entry(self):
        """
        The user is able to edit an existing workout entry

        Returns
        -------
        None.

        """   
        log_len = len(self.__log)
        if log_len == 0:
            print("\nYour log is currently empty. If you want to add a new entry, select New Entry.")
            return
        #ask the user which entry they want to updaate, validate input
        valid_num = False
        while not valid_num:
            entry_num = input("\nEnter the ID number of the entry you want to edit (ID number can be found in your my_log.txt file): ")
            valid_num = validate.validate_entry_num(entry_num, log_len)
        entry = self.__log[int(entry_num)-1]
        entry.edit_entry(entry_num)
        #update the log file with edited entry
        self.__create_log_file()
        #check if user wants to edit another field in the same entry
        another_field = True
        while another_field: 
            #update the log file with edited entry
            self.__create_log_file()
            valid_again = False
            while not valid_again:
                edit_again = input("\nDo you want to edit another field in this entry? (y/n) ")
                valid_again = validate.validate_yn(edit_again)
            if edit_again[0] == 'y':
                entry.edit_entry(entry_num)
            else:
                self.new_max()
                another_field = False
            
    def __view_entry(self):
        """
        the user is able to view an existing entry

        Returns
        -------
        None.

        """
        log_len = len(self.__log)
        if log_len == 0:
            print("\nYour log is currently empty. If you want to add a new entry, select New Entry.")
            return
        #ask the user which entry they want to updaate, validate input
        valid_num = False
        while not valid_num:
            entry_num = input("\nEnter the ID number of the entry you want to edit (ID number can be found in your my_log.txt file): ")
            valid_num = validate.validate_entry_num(entry_num, log_len)
        entry = self.__log[int(entry_num)-1]
        print(self.__format_headers)
        print(f'{self.__log.index(entry) + 1 :<5} {entry}')
        
    def __delete_entry(self):
        """
        the user is able to delete an existing entry

        Returns
        -------
        None.

        """
        log_len = len(self.__log)
        if log_len == 0:
            print("\nYour log is currently empty. If you want to add a new entry, select New Entry.")
            return
        #ask the user which entry they want to update, validate input
        valid_num = False
        while not valid_num:
            entry_num = input("\nEnter the ID number of the entry you want to edit (ID number can be found in your my_log.txt file): ")
            valid_num = validate.validate_entry_num(entry_num, log_len)
        entry = self.__log[int(entry_num)-1]
        self.__log.remove(entry)
        #check if the entry the user deleted was the max distance entry
        if entry in self.max_distance_entry:
            #if yes, then remove from list. Find a new max entry if it was the only one in the list
            self.max_distance_entry.remove(entry)
            if len(self.max_distance_entry) == 0:
                self.new_max()
        print(f'\nEntry number {entry_num} has deleted.')
        
    def check_max(self,entry):
        """
        Updates the maximum distance value
        
        Parameters
        ----------
        entry: Entry
            entry to be compared to max

        Returns
        -------
        None.

        """
        #if it's the first workout, make it the max
        if len(self.max_distance_entry) == 0:
            self.max_distance_entry.append(entry)
        #if it's equal to the current max, add it to the list, otherwise update the list to include the new max entry
        else:
            if entry == self.max_distance_entry[0]:
                self.max_distance_entry.append(entry)
            elif entry > self.max_distance_entry[0]:
                self.max_distance_entry.clear()
                self.max_distance_entry.append(entry)
                
    def new_max(self):
        """
        Finds the new max distance entry after the old max entry was deleted by the user

        Returns
        -------
        None.

        """
        #remaining distances
        log_distances = [e.distance for e in self.__log if e.distance != "N/A"]
        #if there are no more non-Other entries, clear the list
        if len(log_distances) == 0:
            self.max_distance_entry = []
        else:
            #find the max distance in the remaining workouts, and add any workout to the max distance list that hits that distance
            max_distance = max(log_distances)
            self.max_distance_entry = [e for e in self.__log if e.distance == max_distance]
        
            
            

                
        
        
    

