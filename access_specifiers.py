class Public_Sample_AccessModifier:
    def _init_(self, course, duration):
        self.course = course
        self.duration = duration

    def display_public_class_method(self):
        print("Course: {} - Duration: {}".format(self.course, self.duration))


publicObj = Publ
publicObj.display_public_class_method()


# Protected Method -- Only to accessible to a class derived from it. We use _ to declare protected methods

class Protected_Sample_Class:
    _tutor = None
    _place = None
    _experience = None

    def _init_(self, tutor, place, experience):
        self._tutor = tutor
        self._place = place
        self._experience = experience

    def _displayTutorDetails(self):
        print("Tutor: {} - Place: {} - Experience: {}".format(self._tutor, self._place, self._experience))


class Derived_Protected_Class(Protected_Sample_Class):
    def display_protected_method_variables(self):
        self._displayTutorDetails()


class Non_Derived_Class(Derived_Protected_Class):
    def tryToDisplayProtectedMethod(self):
        self._displayTutorDetails()


derivedClassObj = Derived_Protected_Class("Shree", "Bangalore", 12)
derivedClassObj.display_protected_method_variables()

nonDerivedObj = Non_Derived_Class("James", "C", 2)
nonDerivedObj.tryToDisplayProtectedMethod()


# Private -- The members of class declared private are accessbile to its own class

class Private_class_sample:
    __tutor = None
    __place = None
    __experience = None

    def _init_(self, tutor, place, experience):
        self.__tutor = tutor
        self.__place = place
        self.__experience = experience
        #

    def __displayTutorDetails(self):
        print("Tutor: {} - Place: {} - Experience: {}".format(self._tutor, self.place, self._experience))

    def _displayTutorDetailsProtected(self):
        # print("Look it won't display private methods")
        print("Tutor: {} - Place: {} - Experience: {}".format(self._tutor, self.place, self._experience))
        return self._tutor, self._place

    def displayTutorDetailsPublic(self):
        # print("Can display public")
        print("Tutor: {} - Place: {} - Experience: {}".format(self._tutor, self.place, self._experience))
        self.__displayTutorDetails()


class Derived_Private_Class(Private_class_sample):
    def display_parent_private_method(self):
        self.__displayTutorDetails()

    def display_parent_protected_method(self):
        tutor, place = self._displayTutorDetailsProtected()
        print(tutor, place)

    def display_parent_public_method(self):
        self.displayTutorDetailsPublic()


derivedPrivateObj = Derived_Private_Class("Shree", "Vijayawada", 5)
derivedPrivateObj.display_parent_private_method()
derivedPrivateObj.display_parent_protected_method()
derivedPrivateObj.display_parent_public_method()

ic_Sample_AccessModifier("Python", 6)