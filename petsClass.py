class Pets:
    # Private Properties
    __petAge: int = 1
    __petName: str = ""

    __ownerName: str = ""
    __animalType: str = ""
    __animalId: int = 1

    ########################
    # Instantiate a copy of this class
    def __init__(self,
                petAge = 1,
                petName = "Bailey",
                ownerName = "Hunter",
                animalType = "chicken",
                animalId = 1):

        # Set all our properties
        self.setPetAge(petAge)
        self.setPetName(petName)
        self.setOwnerName(ownerName)
        self.setAnimalType(animalType)
        self.setAnimalId(animalId)


###############################################
    def getPetAge(self) -> int:
        return(self.__petAge)

    def setPetAge(self, petAge) -> None:
        if petAge:
            self.__petAge = petAge

###############################################
    def getPetName(self) -> str:
        return(self.__petName)

    def setPetName(self, petName) -> None:
        if petName:
            self.__petName = petName

###############################################
    def getOwnerName(self) -> str:
        return (self.__ownerName)

    def setOwnerName(self, ownerName) -> None:
        if ownerName:
            self.__ownerName = ownerName

###############################################
    def getAnimalType(self) -> str:
        return (self.__animalType)

    def setAnimalType(self, animalType) -> None:
        if animalType:
            self.__animalType = animalType

###############################################
    def getAnimalId(self) -> int:
        return (self.__animalId)

    def setAnimalId(self, animalId) -> None:
        if animalId:
            self.__animalId = animalId
