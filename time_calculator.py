##################################################################################
#
#   time_calculator:
#    The function adds the duration time to the start time and return the result.
#       Input: 
#           start_time (required):
#           interval (required): Duration
#           start_day (optional): Specify day of the week
#       
#       Output:
#           None. Prints the result
#
###################################################################################
import re

def add_time(start_time, interval,start_day=False):
    
    try:

        week_days     = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

        ##############
        # Check Input.
        if not(start_day == False or start_day.capitalize() in week_days):
            raise Exception("Error: Check spelling!") 

        structure_input = re.search("[\d]*[:][\d]*",start_time)
        if structure_input == None:
            raise Exception("Error: Check Time Input")

        structure_add_hours = re.search("[\d]*[:][\d]*",interval)
        if structure_add_hours == None:
            raise Exception("Error: Check Time Input")

        ##########################
        # Dictionary for Cuteness.
        initial_parameters  = re.split('[:|\s]',start_time)
        time_dict = {
            "hours"  :int(initial_parameters[0]),
            "minutes":int(initial_parameters[1]),
            "am_pm"  :initial_parameters[2].lower()
        }
        
        ##########################
        # Check dictionary Values.
        if  not(0 < time_dict["hours"] <= 12 and  60 > time_dict["minutes"] >=0 and time_dict["am_pm"] in ["am","pm"]):
            raise Exception("Error: Check Time Input")

        ##########################
        # Dictionary for Cuteness.
        interval_parameters = re.split('[:|\s]',interval)
        interval_dict = {
            "hours"  : int(interval_parameters[0]),
            "minutes": int(interval_parameters[1])
        }

        ##########################
        # Check dictionary Values.
        if not(60 > interval_dict["minutes"] >= 0):
            raise Exception("Error: Check Time Input")
        
        ############################ 
        # Transform into 24hs clock.
        if time_dict["am_pm"] == "pm":
            time_dict["hours"] += 12
        
        ###########################
        # Sum of hours and minutes.
        total_minutes = time_dict["minutes"] + interval_dict["minutes"]
        minutes       = total_minutes % 60
        total_hours   = (time_dict["hours"] + interval_dict["hours"] + (total_minutes//60))
        total_days    = total_hours // 24
        hours         = total_hours % 24

        ###################
        # Days of the week.
        if start_day:
            init_day      = start_day.capitalize()
            day           = f", {week_days[(total_days + week_days.index(init_day)) % 7]}"
        else :
            day           = ""

        ########
        # Print.
        if hours > 12:
            prt_hours = hours - 12
        
        elif hours == 0:
            prt_hours = hours +12
        
        else:
            prt_hours = hours

        prt_minutes       = minutes if len(str(minutes))>1 else f"0{minutes}"
        am_pm             = "PM" if hours >= 12 else "AM"
        
        if total_days == 0:
            prt_total_days = ""
        
        elif total_days == 1:
            prt_total_days = "(next day)"
        
        else:
            prt_total_days = f"({total_days} days later)"

        result = f"{prt_hours}:{prt_minutes} {am_pm}{day} {prt_total_days}"
        print(result)

    except Exception as e:
        print(e)


########
# Tests.
add_time("300 PM", "3:10")
add_time("11:30 AMs", "2:32", "Monday")
add_time("12:51 AM", "00:20")
add_time("10:10 PM", "3:30")
add_time("11:43 PM", "24:20", "tueSday")
add_time("6:30 PM", "205:12")
    