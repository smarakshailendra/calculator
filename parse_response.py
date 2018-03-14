import json
import re
from collections import OrderedDict


def convert_op_json(response):
    lst_vals = response.split("**")
    person_details = lst_vals[0]
    follower_details = lst_vals[1]
    lst_persondetails = person_details.split("|")[1:]
    lst_followerdetails = follower_details.split("@@")
    follower_list = list()
    follower_dict = dict()
    for follower in lst_followerdetails:
        follower = filter(None, follower.split("|"))
        if "followers" in follower:
            follower = follower[1:]

        follower_list.append(get_person_details(follower, True))

    follower_dict.update({"followers" : follower_list})

    person_details_dict = get_person_details(lst_persondetails)
    person_details_dict.update(follower_dict)
    json_person = json.dumps(person_details_dict, indent=4)
    print json_person


def get_person_details(lst_details, follower=False):

    id = get_id(lst_details)
    dict_name = get_name(lst_details)
    dict_loc = get_location(lst_details)
    imageID = get_imageID(lst_details)
    output = OrderedDict()
    if follower:
        if id:
            output.update({"id": id})
        if imageID:
            output.update({"imageId": imageID})
        if dict_name:
            output.update({"name": dict_name})
        if dict_loc:
            output.update({"location": dict_loc})
    else:
        if id:
            output.update({"id": id})
        if dict_name:
            output.update({"name": dict_name})
        if dict_loc:
            output.update({"location": dict_loc})
        if imageID:
            output.update({"imageId": imageID})
    return output


def get_id(lst_details):
    if len(lst_details) >= 1:
        return lst_details[0]
    else:
        return None


def get_name(lst_name):
    if len(lst_name) >= 2:
        lst_name = lst_name[1].split("><")
        lst_names = list()
        for name in lst_name:
            rgx = re.compile('[<>]')
            lst_names.append(rgx.sub("", name))

        dict_name = OrderedDict()
        dict_name.update({"first": lst_names[0]})
        dict_name.update({"middle": lst_names[1]})
        dict_name.update({"last": lst_names[2]})
        return dict_name
    else:
        return None


def get_location(lst_loc):
    try:
        if len(lst_loc) >= 3:
            lst_loc = lst_loc[2].replace("<", "")
            lst_loc = lst_loc.split(">")
            dict_loc = OrderedDict()
            dict_loc.update({"name": lst_loc[0]})
            dict_coord = OrderedDict()
            if lst_loc[1]:
                dict_coord.update({"long": float(lst_loc[1])})
            else:
                dict_coord.update({"long": lst_loc[1]})
            if lst_loc[2]:
                dict_coord.update({"lat": float(lst_loc[2])})
            else:
                dict_coord.update({"lat": lst_loc[2]})
            dict_loc.update({"coords": dict_coord})
            return dict_loc
        else:
            return None
    except:
        print "Error getting location"


def get_imageID(lst_details):
    try:
        if len(lst_details) >= 4:
            imageID = lst_details[3]
            imageID = re.sub(r"\s+", "", imageID)
            return imageID
        else:
            return None
    except:
        print "Error getting image id"
        return None

z = "profile|73241232|<Aamir><Hussain><Khan>|<Mumbai><<72.872075><19.075606>>|73241 232.jpg**followers|54543342|<Anil><>" \
    "<Kapoor>|<Delhi><<23.23><12.07>>|54543342. jpg@@|12311334|<Amit><><Bansal>|<Bangalore><<><>>|12311334.jpg"

y = "profile|73241234|<Niharika><><Khan>|<Mumbai><<72.872075><19.075606>>|73241234.jpg**followers|54543343" \
    "|<Amitabh><><>|<Dehradun><<><>>|54543343.jpg@@|22112211|<Piyush><><>||"

# convert_op_json(z)
# convert_op_json(y)