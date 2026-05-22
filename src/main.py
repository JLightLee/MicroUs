# PoC using hard coded mock data
# have a list of players: username, date & hours free, skill level & role
# make a class later
# need to specify exactly what hours on what days later

# roles represented as:
# 1 = DPS | 2 = TANK | 3 = HEAL

# setup the gamer data for now
gamers = {
    "weekend_gamer": {
        "available days": [5, 6, 7], # friday, saturday, sunday
        "available hours": [12, 13, 14, 15, 19, 20, 21, 22], # from noon to 3pm and 7pm to 10pm
        "skill": [6], # 6/10 on skill level
        "role": [2] # role 
    },
    "sometimes_gamer":{
        "available days": [3, 5, 7], # wed, fri, sunday
        "available hours": [14, 15, 19, 20, 21, 22], # from 2pm to 3pm and 8pm to 10pm
        "skill": [4], # 4/10 on skill level
        "role": [1] # role 
    },
    "always_gamer":{
        "available days": [1, 2, 3, 4, 5, 6, 7], # wed, fri, sunday
        "available hours": [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], # from 9am to 10pm
        "skill": [8], # 4/10 on skill level
        "role": [2] # role 
    },

# we need to actually convert this data into something we can compare and organize


}