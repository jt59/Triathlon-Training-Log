#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jillian Turner
Class: CS 521 - Summer 2
Date: 8/20/2022
Final Project: unit tests
Description: tests public class methods of Action class
"""

import Entry
import Action

if __name__ == "__main__":
    #test check_max() method using a workout of 5 miles
    entry_1 = Entry.Entry(True)
    entry_1.distance = 5
    action = Action.Action([entry_1],True)
    action.check_max(entry_1)
    assert len(action.max_distance_entry) == 1, "Error: max_distance_entry is not as expected"
    assert action.max_distance_entry[0].distance == 5, "Error: max_distance_entry is not expected distance"
    #add in a second workout of 5 miles
    action.check_max(entry_1)
    assert len(action.max_distance_entry) == 2, "Error: max_distance_entry is not as expected"
    #add in a workout of 6 miles
    entry_2 = Entry.Entry(True)
    entry_2.distance = 6
    action.check_max(entry_2)
    assert len(action.max_distance_entry) == 1, "Error: max_distance_entry is not as expected"
    assert action.max_distance_entry[0].distance == 6, "Error: max_distance_entry is not expected distance"
    
    #test new_max() function
    action = Action.Action([entry_1,entry_1,entry_2],True)
    action.new_max()
    assert len(action.max_distance_entry) == 1, "Error: max_distance_entry new_max() not working"
    assert action.max_distance_entry[0].distance == 6, "Error: max_distance_entry is not expected distance"
    action = Action.Action([entry_1,entry_1],True)
    action.new_max()
    assert len(action.max_distance_entry) == 2, "Error: max_distance_entry new_max() not working"
    assert action.max_distance_entry[0].distance == 5, "Error: max_distance_entry is not expected distance"
    print("Unit tests passed!")
