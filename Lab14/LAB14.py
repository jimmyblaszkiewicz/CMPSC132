#LAB 14
#Due Date: 12/07/2018, 11:59PM
########################################
#                                      
# Name: James Blaszkiewicz
# Collaboration Statement: I completed this code by myself 
#                          using only the class materials.             
#
########################################

def makingSound(n,sound):
	#Write your code here
    def soundFunc(m):
        # create a message to build
        message = []
        for i in range(m):
            if i % n == 0:
                message.append(sound)
            else:
                message.append(i)

        return message
    return soundFunc

def vectorizing(term):
	#Write your code here
    # create the function
    def func(aList):
        # return mapping term to aList
        return list(map(term, aList))
    return func