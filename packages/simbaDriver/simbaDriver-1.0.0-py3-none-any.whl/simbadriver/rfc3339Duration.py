# BEGIN: Copyright 
# Copyright (C) 2024 Rector and Visitors of the University of Virginia 
# All rights reserved 
# END: Copyright 

# BEGIN: License 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
#   http://www.apache.org/licenses/LICENSE-2.0 
# END: License 

# timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
from datetime import timedelta
import re

# Durations:
# 
#    dur-second        = 1*DIGIT "S" (?P<seconds>[\d]+)S
#    dur-minute        = 1*DIGIT "M" [dur-second] (?P<minutes>[\d]+)M((?P<m_seconds>[\d]+)S)?
#    dur-hour          = 1*DIGIT "H" [dur-minute] (?P<hours>[\d]+)H((?P<h_minutes>[\d]+)M((?P<h_seconds>[\d]+)S)?)? 
#    dur-time          = "T" (dur-hour / dur-minute / dur-second) T(?P<time>([\d]+)H(([\d]+)M(([\d]+)S)?)?|([\d]+)M(([\d]+)S)?)
#    dur-day           = 1*DIGIT "D" (?P<days>[\d]+)D
#    dur-week          = 1*DIGIT "W" (?P<weeks>[\d]+)W
#    dur-month         = 1*DIGIT "M" [dur-day] (?P<months>[\d]+)M((?P<m_days>[\d]+)D)?
#    dur-year          = 1*DIGIT "Y" [dur-month] (?P<years>[\d]+)Y((?P<y_months>[\d]+)M((?P<y_days>[\d]+)D)?)?
#    dur-date          = (dur-day / dur-month / dur-year) [dur-time] (([\d]+)D|([\d]+)M(([\d]+)D)?|([\d]+)D(([\d]+)M(([\d]+)D)?)?)(T(([\d]+)H(([\d]+)M(([\d]+)S)?)?|([\d]+)M(([\d]+)S)?))
# 
#    duration          = "P" (dur-date / dur-time / dur-week) (-)?P((([\d]+)D|([\d]+)M(([\d]+)D)?|([\d]+)D(([\d]+)M(([\d]+)D)?)?)(T(([\d]+)H(([\d]+)M(([\d]+)S)?)?|([\d]+)M(([\d]+)S)?))|T(([\d]+)H(([\d]+)M(([\d]+)S)?)?|([\d]+)M(([\d]+)S)?)|([\d]+)W)
# 	

class rfc3339Duration:
    @staticmethod
    def toTimeDelta(duration):
        p_time = 'T(?P<time>(?P<hours>[\d]+)H((?P<h_minutes>[\d]+)M((?P<h_seconds>[\d]+)S)?)?|(?P<minutes>[\d]+)M((?P<m_seconds>[\d]+)S)?|(?P<seconds>[\d]+)S)'
        p_week = '(?P<weeks>[\d]+)W'
        p_date = '(?P<date>(?P<years>[\d]+)Y((?P<y_months>[\d]+)M((?P<y_days>[\d]+)D)?)?|(?P<months>[\d]+)M((?P<m_days>[\d]+)D)?|(?P<days>[\d]+)D)'

        regexp = re.compile('\A(?P<minus>-)?P(' + p_week + '|(' + p_date+ ')?(' + p_time + ')?)\Z')

        match = regexp.match(duration)

        if (match == None):
            raise Exception('Invalid rfc3339 duration: ' + duration)

        seconds = 0

        if (match != None):
            if (match.group('time')):
                if (match.group('hours')):
                    seconds += 3600 * int(match.group('hours'))
                    if (match.group('h_minutes')):
                        seconds += 60 * int(match.group('h_minutes'))
                        if (match.group('h_seconds')):
                            seconds += int(match.group('h_seconds'))
            
                if (match.group('minutes')):
                    seconds = 60 * int(match.group('minutes'))
                    if (match.group('m_seconds')):
                        seconds += int(match.group('m_seconds'))

                if (match.group('seconds')):
                    seconds = int(match.group('seconds'))

            if (match.group('date')):
                if (match.group('years')):
                    seconds += 31557600 * int(match.group('years'))
                    if (match.group('y_months')):
                        seconds += 2629800 * int(match.group('y_months'))
                        if (match.group('y_days')):
                            seconds += 86400 * int(match.group('y_days'))
            
                if (match.group('months')):
                    seconds += 2629800 * int(match.group('months'))
                    if (match.group('m_days')):
                        seconds += 86400 * int(match.group('m_days'))

                if (match.group('days')):
                    seconds += 86400 * int(match.group('days'))

            if (match.group('weeks')):
                seconds += 86400 * int(match.group('weeks'))

            if (match.group('minus')):
                seconds *= -1

        return timedelta(seconds = seconds)
