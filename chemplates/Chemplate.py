from pprint import pformat
import json
import CHEMBOX.refdata.DataValue as DV
class Chemplate():
    """Chemplate class for ChemBox to manipulate information in Chemplates
    (chemistry question templates). It's basically like a library of Python
    dictionaries

    Attributes
    ----------
    data : dictionary of dictionaries

    Public Methods
    --------------
    __init__ create a new Chemplate with the supplied id, attribute and value:
                - ID : ID of the dictionary to manipulate
                - attribute : attribute in the ditctionary
                - value : the value the attriburte should have. (None by default)
                - DoD : initalize data from a dictionary of dictionaries
         Raises: TypeError for invalid parameter name

    __str__  give a code like representation of the Chemplate
    __repr__ give a code like representation of the Chemplate
    Chemplate.setID(ID=str, attribute=str,value=any) or
    Chemplate.setID(ID=str, dict=dictionary )
        set the value for a chemplate ID
    """
    def __set(self, ID=None, attribute=None, value=None ):
        if not ID in self.data:
            self.data[ID]={}
        self.data[ID][attribute]=value

    def __setFromDict(self, ID=None, dict=None ):
        if not ID in self.data:
            self.data[ID]={}
        for attr in dict:
            self.data[ID][attr]=dict[attr]

    def __init__(self, ID=None, attribute=None, value=None, DoD=None ):
        self.data = {}
        if DoD is not None:
            for ID1 in DoD:
                for attr1 in DoD[ID1]:
                    self.__set(ID1, attr1, DoD[ID1][attr1])
        elif (ID is not None and attribute is not None):
            self.__set(ID, attribute, value)

    def __repr__(self):
        string=pformat(self.data)
        return string

    def __str__(self):
        string=pformat(self.data)
        return string

    def setID(self, ID=None, attribute=None,value=None, dict=None):
        """Set a Chemplate ID from a string

        Parameters
        ----------
        ID: str (required)
        a string indicating which ID should be set. If the ID exists, its
            contents are replaced, otherwise it is created.

        attribute, value: str, any
        an attribute value pair to set for ID. the value is any legit Python value.

        dict: dictionary
        a dictionary to set the ID to.

        If both dict and attribute,value are specified, the dictionary is set
            first, then the attribute,value, potentially replacing the attribute
            if it is given in the dictionary

        Raises
        ------
        AttributeError
            if no attribute, value pair or dict is specified.

        """
        if dict is not None:
            self.__setFromDict(ID=ID, dict=dict)
        if (ID is not None and attribute is not None):
            self.__set(ID, attribute, value)

    def getID(self, ID=None):
        """get the value of a Chemplate ID

        Parameters
        ----------
        ID: str (required)
        a string indicating which ID should be used to get the dictionary.

        Returns
        -------
        a dictionary with the contents of the ID

        Raises
        ------
        KeyError
            if the ID doesn't exist

        """
        return self.data[ID]

    def getIDattr(self, ID=None, attribute=None):
        """get the value of a Chemplate ID

        Parameters
        ----------
        ID: str (required)
        a string indicating which ID should be used to choose the dictionary.
        attribute: str (required)
        a string indicating which attribute should be use to get the value.

        Returns
        -------
        the contents of the attribute in dictionary ID

        Raises
        ------
        KeyError
            if the ID or attribute doesn't exist

        """
        return self.data[ID][attribute]

    def getIDs(self):
        """get the IDs in a Chemplate

        Parameters
        ----------
        None

        Returns
        -------
        A list of all the IDs in a Chemplate

        Raises
        ------
        None

        """
        return self.data.keys()

    def updateWith(self,new=None):
        """update a Chemplate with the contents of another

        Parameters
        ----------
        new : Chemplate
        the values in the specified Chemplate replace those in the current
        Chemplate, or create new ones if they don't exist.

        Returns
        -------
        None

        Raises
        ------
        None

        """
        assert isinstance(new, Chemplate)
        for id in new.data:
            self.data[id] = new.data[id]

    def delID(self,ID=None):
        """delete a Chemplate ID's values

        Parameters
        ----------
        ID : str (required)
        the ID in the specified Chemplate to remove

        Returns
        -------
        the dictionary of the contents of ID

        Raises
        ------
        KeyError if ID doesn't exist
        TypeError if given extra paramters

        """
        return self.data.pop(ID)

    def delIDattr(self,ID=None,attribute=None):
        """delete a Chemplate ID's attribute value

        Parameters
        ----------
        ID : str (required)
        the ID in the specified Chemplate to remove the attribute from
        attribute : str (required)
        which attribute to remove from ID

        Returns
        -------
        the value of ID's attribute

        Raises
        ------
        KeyError if ID doesn't exist or attribute doesn't exist in ID

        """
        return self.data[ID].pop(attribute)

    def existsIDattr(self,ID=None,attribute=None):
        """check if a Chemplate ID's attribute value exists

        Parameters
        ----------
        ID : str (required)
        the ID in the specified Chemplate to remove the attribute from
        attribute : str (required)
        which attribute to check for existance in ID

        Returns
        -------
        the True if ID's attribute exists

        Raises
        ------
        KeyError if ID doesn't exist

        """
        return attribute in self.data[ID]

    def existsID(self,ID=None):
        """check if a Chemplate ID exists

        Parameters
        ----------
        ID : str (required)
        the ID in the specified Chemplate to check

        Returns
        -------
        the True if the ID exists in self.data

        Raises
        ------
        None

        """
        return ID in self.data

    def asdict(self):
        """return chemplate data as a dict

        Parameters
        ----------
        None

        Returns
        -------
        chemplate data

        Raises
        ------
        None

        """
        return self.data

    def equalTo(self,other):
        for key in self.getIDs():
            if isinstance(self.getIDattr(key,'value'),str):
                filled_val = json.dumps(self.getID(key), sort_keys=True)
                correct_val = json.dumps(other.getID(key), sort_keys=True)
                assert filled_val == correct_val, f"filled {key} not equal to correct item ({filled_val}, {correct_val})"
            elif isinstance(self.getIDattr(key,'value'),DV.DataValue):
                filled_val = str(self.getIDattr(key,'value'))
                correct_val = str(other.getIDattr(key,'value'))
                assert filled_val == correct_val, f"filled {key} not equal to correct item ({filled_val}, {correct_val})"
        return True
            #print("TEMPLATE:",pformat(answer_template_1))
            #print("ANSWERS:",pformat(filled))
