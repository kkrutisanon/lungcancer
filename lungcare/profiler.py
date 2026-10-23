changingValues = ['','Male','Female']
yesNoParam = ['Chest_Pain','Swallowing_Difficulty','Shortness_of_Breath','Coughing','Alcohol_Consuming','Wheezing','Allergy','Fatigue','Chronic_Disease','Peer_Pressure','Anxiety','Yellow_Fingers','Smoking']
yesNoValues = ['','No','Yes']
   
def generateProfile(data):
    Person_Profile = []
    for x in data:
        if x in yesNoParam:
            newStrings = x.replace('_'," ") + '  :  ' + yesNoValues[int(data[x])]
        elif x == 'Gender':
            newStrings = 'Gender : ' + changingValues[int(data[x])]
        else:
            newStrings = x.replace('_'," ") + '  :  ' + data[x]
        Person_Profile.append(newStrings)
    return Person_Profile

def generateOutput(prediction):
    base = 'From the given profile our model has predicted : '
    choice = ['The person does have Lung Cancer','The person does not have Lung Cancer']
    
    return base + choice[prediction]