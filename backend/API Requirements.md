# Activity Centre
### Overall trail stats:
Get the overall trail stats for a given user
```python
# Recieve data:
user_id = request.get_json()["userID"]

# Send data:
return jsonify({
    # Total time spent doing activities in a period of time (try to make the time easily variable)
    "totalDuration": {"hours": 0, "minutes": 0},
    # Longest activity in time period
    "longestTime": {"hours": 0, "minutes": 0},
    # Total calories burn in time period
    "totalCalories": 0
})
```

## List of all trails
### Get Trail ids
Get all the trail ids for a given user id
```python
# Recieve data:
user_id = request.get_json()["userID"]

# Send data:
return jsonify({
    # List of trail IDs
    "trails": [1,2,3,4]
})
```
### Get data for given ID
You get sent the trail ID, and send back:
```python
# Recieve data:
trail_id = request.get_json()['trailID']

# Send data:
return jsonify({
    "name": "",
    "date": "",
    "distance": 0.0,    # In Km
    "time": {"hours": 0, "minutes": 0, "seconds": 0},
    "speed": 0.0,   # In Km/h
    "calories": 0,
    "gpx": None,    # The GPX data (IDK what type that is)
})
```

### Delete trail
A post request that takes a given trail and deletes it from the DB.
```python
# Recieve data:
trail_id = request.get_json()['trailID']
```

# View Trail
Only uses calls defined above (in Activity Centre)

# Community
### List friends
Gets a list of the friends and the display data for them
```python
# Recieve data:
user_id = request.get_json()['userID']

# Send data:
return jsonify({
    "friends": [
        {
            "id": 1,
            "name": "",     # Username of the user
            "profilePhoto": None    # IDK what type this will be...
        },
        {
            "id": 2,
            "name": "",     # Username of the user
            "profilePhoto": None    # IDK what type this will be...
        }
    ],
})
```

### List groups
Get a list of the group names a user is part of.
```python
# Recieve data:
user_id = request.get_json()['userID']

# Send data:
return jsonify({
    "groups": [
        {"id": 1, "name": "groupname1"}, 
        {"id": 2, "name": "groupname2"}
        ]
})
```

### Create group
Create a new group with a given name, and add the user to it.
```python
# Recieve data:
data = request.get_json()
user_id = data["userID"]
group_name = data["groupName"]
```

### Get friend requests
Get a list of all friend requests for the given user.
```python
# Recieve data:
user_id = request.get_json()['userID']

# Send data:
return jsonify({
    "friends": [
        {
            "id": 1,
            "name": "",     # Username of the user
            "profilePhoto": None    # IDK what type this will be...
        },
        {
            "id": 2,
            "name": "",     # Username of the user
            "profilePhoto": None    # IDK what type this will be...
        }
    ],
})
```

### Add friend
Add a friend to a user given both user ids
```python
data = request.get_json()
user_id1 = request.get_json()['userID1']
user_id2 = request.get_json()['userID2']
```

### Send friend request
Send a friend request from given user to other user.
```python
data = request.get_json()
send_user_id = request.get_json()['sendUserID']
recieve_user_id = request.get_json()['recieveUserID']
```

# Group
### Get group trail data
Get all the trails currently added to the group map/
```python
# Recieve data:
group_id = request.get_json()["groupID"]

# Send data:
return jsonify({
    trails = [1, 2, 3] # Route IDs
})
```

### Get members
Get all member info for group (similar to friends list - only certain info)
```python
# Recieve data:
group_id = request.get_json()['groupID']

# Send data:
return jsonify({
    "friends": [
        {
            "id": 1,
            "name": "",     # Username of the user
            "profilePhoto": None    # IDK what type this will be...
        },
        {
            "id": 2,
            "name": "",     # Username of the user
            "profilePhoto": None    # IDK what type this will be...
        }
    ],
})
```

### Leave group
Have the given user leave the given group, and delete the group if there are no members.
```python
# Recieve data:
data = request.get_json()
user_id = data["userID"]
group_id = data["groupID"]
```

### Add route to group
Add the given route to the given group and return the new map data
```python
# Receive data:
data = request.get_json()
trail_id = data["trailID"]
group_id = data["groupID"]
```

### Add friend to group
Add the given friend to the given group and send the new list of group memebers.
```python
# Recieve data:
data = request.get_json()
user_id = data["userID"]
group_id = data["groupID"]
```

# Membership
### Get membership options
Get a list of all options for the membership plan, with their benefits and prices.
Also get sent the user_id and return the current plan that user is on.
```python
# Recieve data:
user_id = request.get_json()["userID"]

# Send data:
return jsonify({
    "membershipOptions": [
        {
            "name": "Plan 1",
            "regularity": "Weekly",
            "price": 7,
            "isCurrentPlan": True   # Is true if it is the given user's plan
        },
        {
            "name": "Plan 2",
            "regularity": "Monthly",
            "price": 6.6,
            "isCurrentPlan": False
        },
    ]
})
```

# Account
### Get account details
More detailed info for the given user's account.
```python
# Recieve data:
user_id = request.get_json()["userID"]

# Send data:
return jsonify({
    "name": "",
    "profilePhoto": None    # IDK what format this will be in
    "membershipTier": "",
    "gender": "",
    "age": 12,
    "paymentRegularity": "Monthly"
})
```

### Change password
Update the given user's password with the new info.
```python
# Recieve data:
data = request.get_json()
user_id = data["userID"]
password = data["password"]
```

### Delete account
Delete the given user's account.
```python
# Recieve data:
user_id = request.get_json()["userID"]
```

# Login/Register
Basically done I think... If not, I'll work on it.

# Reset password
We will ignore this for now, no system in place to handle this yet

# Upload trail
### Upload trail
Upload the trail for the given user ID
```python
# Recieve data:
data = request.get_json()
user_id = data["userID"]
gpx_data = data["gpx_data"]
name = data["name"]
exercise_type = data["exerciseType"]
```