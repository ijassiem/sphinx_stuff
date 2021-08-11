""" This is a docstring for the module 'classthings.py'
"""
#https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html#
class person:
    """This class person represents an employee with several attributes.
     
     :param name: Name of person 
     :type name: str 
     :param staffno: Staff or employee number of person 
     :type staffno: int 
     :param height_cm: Height of person in cm 
     :type height_cm: float 
     :param weight_kg: Weight of person in kg 
     :type weight_kg: float 
     :param bmi: Calculated BMI of person 
     :type bmi: float
     """

    group = 'Beginner' #class attribute
    number = 0
    
    def __init__(self, name='Unknown', height_cm = None, weight_kg = None): #constructor
        """Constructor method
        """
        person.number += 1
        self.staffno = person.number
        self.name = name #instance attribute
        self.height_cm = height_cm #instance attribute
        self.weight_kg = weight_kg
        self.bmi = None
    
    def displayInfo(self): #method
        """Prints all attributes of person
        
        :param [ParamName]: [ParamDescription] 
        :type [ParamName]: [ParamType] 
        :raises [ErrorType]: [ErrorDescription] 
        :return: [ReturnDescription] 
        :rtype: [ReturnType]
        """
        print('Name : {}'.format(self.name))
        print('Staff No : {}'.format(self.staffno))
        print('Height : {}'.format(self.height_cm))
        print('Weight : {}'.format(self.weight_kg))
        print('BMI : {}'.format(self.bmi))
        print('Group : {}\n'.format(person.group))
    
    def calc_bmi(self):
        """Calculates BMI.
        """
        self.bmi = self.weight_kg / self.height_cm ** 2
    
    def kg_to_lbs(self):
        """Converts weight from in kg to lbs.
        
        :param [ParamName]: [ParamDescription] 
        :type [ParamName]: [ParamType] 
        :raises [ErrorType]: [ErrorDescription] 
        :return: value of weight in pounds (lbs) 
        :rtype: float, None
        """
        try:
            a = self.weight_kg*2,20462
            return self.weight_kg * 2, 20462
        except:
            return None 

def welcome():
    """This function prints welcome statement.
        
        :param [ParamName]: [ParamDescription] 
        :type [ParamName]: [ParamType] 
        :raises [ErrorType]: [ErrorDescription] 
        :return: [ReturnDescription] 
        :rtype: [ReturnType]
    """
    print ('Welcome to Python.\n')
 
