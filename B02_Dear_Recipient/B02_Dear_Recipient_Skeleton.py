### OBJECTIVE
"""
You are given a list of mail addresses and a string. The string is composed of different sections that are each seperated
by \n\n (two new lines). In the first section you need to find a substring of one of the mailaddresses.
"""

### INPUT - DO NOT TOUCH
mail = eval(input())
### END INPUT


def get_direct_address(mail):
    #TODO
    pass

### OUTPUT - DO NOT TOUCH
print(get_direct_address(mail))
### END OUTPUT


### TEST CASES
# mail1 = (["orestis.lomis@best-eu.org", "eveline.le.bruyn@twipemobile.com", "jasper.rots@best-eu.org"], "Dear Mr Lomis\n\n We have found a dirty sock in the parking lot today and we have strong evidence that it is yours. \n Please come to the security building as soon as possible! \n\n Greetings Mr T")
# mail2 = (["orestis.lomis@best-eu.org", "eveline.le.bruyn@twipemobile.com", "jasper.rots@best-eu.org"], "Dear Ms Le Bruyn\n\n We have found a dirty sock in the parking lot today and we have strong evidence that it is yours. \n Please come to the security building as soon as possible! \n\n Greetings Mr T")
# mail3 = (["orestis.lomis@best-eu.org", "eveline.le.bruyn@twipemobile.com", "michael.le.jaune@live.be","jasper.rots@best-eu.org"], "Dear Mr Le Jaune\n\n We have found a dirty sock in the parking lot today and we have strong evidence that it is yours. \n Please come to the security building as soon as possible! \n\n Greetings Mr T")


# print(get_direct_address(mail1) == "orestis.lomis@best-eu.org")
# print(get_direct_address(mail2) == "eveline.le.bruyn@twipemobile.com")
# print(get_direct_address(mail3) == "michael.le.jaune@live.be")
### END TEST CASES
