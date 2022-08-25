#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jillian Turner
Class: CS 521 - Summer 2
Date: 8/20/2022
Final Project: helper functions to perform calculations
Description: Enables a user to log triathlon exercises
"""

import math

def calculate_pace(distance,duration):
    """
    

    Parameters
    ----------
    distance : string
        workout distance
    duration : string
        workout duration

    Returns
    -------
    Tuple
        two floats, coresponding to mile pace minutes and seconds

    """
    duration = float(duration)
    distance = float(distance)
    mile_pace = duration / distance
    #find the minutes per mile
    mile_pace_min = math.floor(mile_pace)
    #convert remainder into seconds
    mile_pace_sec = round((mile_pace % 1) * 60)
    return mile_pace_min, mile_pace_sec

def calculate_race_time(race_distance, distance, duration):
    """
    

    Parameters
    ----------
    race_distance : float
        race distance corresponding to workout type
    distance : string
        workout distance
    duration : string
        workout duration

    Returns
    -------
    Tuple (3 floats)
        corresponds to race time hrs, minutes, seconds
    """
    distance = float(distance)
    duration = float(duration)
    factor = race_distance / distance
    race_time = duration * factor
    #find expected race time minutes
    race_min = math.floor(race_time)
    #find expected race time seconds
    race_sec = round((race_time % 1) * 60)
    #find expected race time in hours
    race_hr = 0
    if race_min > 60:
        race_hr = math.floor(race_min/60)
        race_min = race_min - 60 * race_hr
    return race_hr, race_min, race_sec
