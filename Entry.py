#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jillian Turner
Class: CS 521 - Summer 2
Date: 8/20/2022
Final Project: Entry Class
Description: A class representing a triathlon exercise log entry
"""
import validate
import calculations

class Entry():
    """A class representing a triathlon exercise log entry

    Args:
        sentence (str): XXX
    
    """
    
    __workout_dict = {"1":"Swim", "2":"Bike","3":"Run", "4":"Other"}
    #race distnces in miles
    __race_distances = {"1":1.2, "2":56, "3":13.1, "4":"N/A"}
    
    def __init__(self,test=False):
        """
        Constructor method to create an Entry instance
        
        Parameters
        ----------
        test: boolean
            determines whether the class is being tested

        Returns
        -------
        None.

        """
        
        if not test:
            self.__enter_workout()
        else:
            self.log_entry = {"date":"", "workout":"", "duration": "", "distance":"", "pace":"", "race distance":"", "race time": ""}

            
    def __enter_workout(self):
        """
        Prompts user to enter a workout type and validates entry.

        Returns
        -------
        None.

        """
        self.__workout_num = input("\nYou chose New Entry. Please enter a number corresponding to the type of workout you want to log. \n\n(1) Swim \n(2) Bike \n(3) Run \n(4) Other \n \nEnter choice here:  ")
        if not validate.validate_input(self.__workout_num, ('1','2','3','4')):
            self.__enter_workout()
        else:
            self.__process_workout()
            
    def __process_workout(self):
        """
        Processes the user's workout type entry to call the correct method

        Returns
        -------
        None.

        """
        workout_name = self.__workout_dict[self.__workout_num]
        #if the user entered Other, ask them the name of the workout
        if workout_name == "Other":
            workout_name = input("\nEnter the name of your workout: ")
        log_entry = {"date":"", "workout":workout_name, "duration": "", "distance":"", "pace":"", "race distance":"", "race time": ""} 
        #prompt user for date and validate format
        valid_date = False
        while not valid_date:
            date = input("\nEnter the date of your {} (MM/DD/YYYY): ".format(workout_name.lower()))
            valid_date = validate.validate_date(date)
        log_entry["date"] = date
        #prompt user for workout duration and validate number
        valid_duration = False
        while not valid_duration:
            duration = input("\nEnter the duration of your {} in minutes: ".format(workout_name.lower()))
            valid_duration = validate.validate_float(duration)
        log_entry["duration"] = duration + " minutes"
        self.__duration = duration
        #prompt user for workout distance if the workout was not other, check validity
        valid_distance = False
        if self.__workout_num == "4":
            distance = "N/A"
            valid_distance = True
        while not valid_distance:
            distance = input("\nEnter the distance of your {} in miles: ".format(workout_name.lower()))
            valid_distance = validate.validate_float(distance)
        log_entry["distance"] = distance + " miles"
        self.distance = distance
        #calculate mile pace
        log_entry["pace"] = "N/A"
        log_entry["race distance"] = "N/A"
        log_entry["race time"] = "N/A"
        if self.__workout_num != "4":
            mile_pace_min, mile_pace_sec = calculations.calculate_pace(distance,duration)
            log_entry["pace"] = "{} minute {} second mile".format(mile_pace_min, mile_pace_sec)
            #set race distance based on workout type
            race_distance = self.__race_distances[self.__workout_num]
            log_entry["race distance"] = "{} miles".format(race_distance)
            #calculate race time
            race_hr, race_min, race_sec = calculations.calculate_race_time(race_distance, distance, duration)
            log_entry["race time"] = "{} miles in {} hours, {} minutes, and {} seconds".format(race_distance, race_hr, race_min, race_sec)
        self.log_entry = log_entry
        
        
        
    def __repr__(self):
        """
        Prints out the log entry

        Returns
        -------
        string: a formatted entry string

        """
        str_format = [v for k,v in self.log_entry.items()]
        space = " "
        return (space*8).join(str_format)
    
    def get_formatted_entry(self):
        """
        Returns formatted entry

        Returns
        -------
        string: a formatted entry string

        """
        str_format = [v for k,v in self.log_entry.items()]
        space = " "
        return (space*8).join(str_format)

    def edit_entry(self, entry_num):
        """
        Edits a user's entry'
        
        Parameters
        ----------
        entry_num : string
            number correspoding to entry ID being edited
    
        Returns
        -------
        None.
    
        """
        edit_options = ('1','2','3','4')
        valid_num = False
        while not valid_num:
            edit_num = input("\nPlease enter a number corresponding to the field you want to edit. \n\n(1) Date \n(2) Workout Type \n(3) Duration \n(4) Distance \n \nEnter choice here:  ")
            valid_num = validate.validate_input(edit_num, edit_options)
        #user wants to edit date
        if edit_num == '1':
            self.__update_date(entry_num)           
        #user wants to edit workout type
        if edit_num == '2':
            self.__update_workout_type(entry_num)
        #user wants to edit workout duration
        if edit_num == "3":
            self.__update_duration(entry_num)
        #user wants to edit workout distance
        if edit_num == "4":
            self.__update_distance(entry_num)
        
        
    
            
    def __update_date(self, entry_num):
        """
        Updates an existing entry's date
        
        Parameters
        ----------
        entry_num : string
            number correspoding to entry ID being edited

        Returns
        -------
        None.

        """
        valid_date = False
        while not valid_date:
            new_date = input('\nThe date for this entry is curently {}. Enter the new date (MM/DD/YYYY): '.format(self.log_entry["date"]))
            valid_date = validate.validate_date(new_date)
        self.log_entry["date"] = new_date
        print(f"\nDate of entry {entry_num} has been changed to {new_date}.")
        
    def __update_workout_type(self, entry_num):
        """
        Updates existing entry's workout type        
        
        Parameters
        ----------
        entry_num : string
            number correspoding to entry ID being edited

        Returns
        -------
        None.

        """
        valid_workout = False
        while not valid_workout:
            new_workout = input("\nThe workout type for this entry is currently {}. Please enter a number corresponding to the type of workout you want to change to. \n\n(1) Swim \n(2) Bike \n(3) Run \n(4) Other \n \nEnter choice here:  ".format(self.log_entry["workout"]))
            valid_workout = validate.validate_input(new_workout, ('1','2','3','4'))
        new_workout_name = self.__workout_dict[new_workout]
        self.__workout_num = new_workout
        if new_workout_name == "Other":
            new_workout_name = input("\nEnter the name of your workout: ")
            self.log_entry["race time"] = "N/A"
            self.log_entry["pace"] = "N/A"
            self.log_entry["distance"] = "N/A"
            self.distance = "N/A"
        self.log_entry["workout"] = new_workout_name
        #set race distance based on workout type
        race_distance = self.__race_distances[self.__workout_num]
        self.log_entry["race distance"] = "{} miles".format(race_distance)
        if new_workout != "4":
            if  self.distance == "N/A":
                valid_distance = False
                while not valid_distance:
                    distance = input("\nPlease enter a new distance in miles for your {}: ".format(new_workout_name.lower()))
                    valid_distance = validate.validate_float(distance)
                self.log_entry["distance"] = distance + " miles"
                self.distance = distance
            #recalculate mile pace
            distance = self.distance
            duration = self.__duration
            mile_pace_min, mile_pace_sec = calculations.calculate_pace(distance,duration)
            self.log_entry["pace"] = "{} minute {} second mile".format(mile_pace_min, mile_pace_sec)
            #recalculate race time
            distance = self.distance
            duration = self.__duration
            race_hr, race_min, race_sec = calculations.calculate_race_time(race_distance, distance, duration)
            self.log_entry["race time"] = "{} miles in {} hours, {} minutes, and {} seconds".format(race_distance, race_hr, race_min, race_sec)
        print(f"\nWorkout type of entry {entry_num} has been changed to {new_workout_name}.")
        
    def __update_duration(self, entry_num):
        """
        Updates existing entry's duration'

        Parameters
        ----------
        entry_num : string
            number correspoding to entry ID being edited

        Returns
        -------
        None.

        """
        workout_name = self.__workout_dict[self.__workout_num]
        valid_duration = False
        while not valid_duration:
            duration = input("\nThe current duration of your {} is {}. Enter a new duration in minutes: ".format(workout_name.lower(), self.log_entry["duration"]))
            valid_duration = validate.validate_float(duration)
        self.log_entry["duration"] = duration + " minutes"
        self.__duration = duration
        if workout_name != "Other":
            #recalculate mile pace
            distance = self.distance
            duration = self.__duration
            mile_pace_min, mile_pace_sec = calculations.calculate_pace(distance,duration)
            self.log_entry["pace"] = "{} minute {} second mile".format(mile_pace_min, mile_pace_sec)
            #calculate race time
            race_distance = self.__race_distances[self.__workout_num]
            race_hr, race_min, race_sec = calculations.calculate_race_time(race_distance, distance, duration)
            self.log_entry["race time"] = "{} miles in {} hours, {} minutes, and {} seconds".format(race_distance, race_hr, race_min, race_sec)
        print(f"\nDuration of entry {entry_num} has been changed to {self.log_entry['duration']}.")
        
    def __update_distance(self, entry_num):
        """
        

        Parameters
        ----------
        entry_num : string
            number correspoding to entry ID being edited

        Returns
        -------
        None.

        """
        workout_name = self.__workout_dict[self.__workout_num]
        valid_distance = False
        if self.__workout_num == "4":
            distance = "N/A"
            print('\nSorry, you cannot edit the distance of an Other type workout.')
            valid_distance = True
            return
        while not valid_distance:
            distance = input("\nThe current distance of your {} is {}. Please enter a new distance in miles: ".format(workout_name.lower(), self.log_entry["distance"]))
            valid_distance = validate.validate_float(distance)
        self.log_entry["distance"] = distance + " miles"
        self.distance = distance
        #recalculate mile pace
        distance = self.distance
        duration = self.__duration
        mile_pace_min, mile_pace_sec = calculations.calculate_pace(distance,duration)
        self.log_entry["pace"] = "{} minute {} second mile".format(mile_pace_min, mile_pace_sec)
        #calculate race time
        race_distance = self.__race_distances[self.__workout_num]
        race_hr, race_min, race_sec = calculations.calculate_race_time(race_distance, distance, duration)
        self.log_entry["race time"] = "{} miles in {} hours, {} minutes, and {} seconds".format(race_distance, race_hr, race_min, race_sec)
        print(f"\nDistance of entry {entry_num} has been changed to {self.log_entry['distance']}.")
        
    def __gt__(self,other):
        """
        Magic functon, greater than defined by distance

        Parameters
        ----------
        other : Entry

        Returns
        -------
        bool
            True if the original entry is greater than the other entry

        """
        if self.distance > other.distance:
            return True 
        return False
        
    def __eq__(self,other):
        """
        Magic functon, equal to, defined by distance

        Parameters
        ----------
        other : Entry

        Returns
        -------
        bool
            True if the original entry is equal to the other entry

        """
        if self.distance == other.distance:
            return True 
        return False
    
        
      
    

