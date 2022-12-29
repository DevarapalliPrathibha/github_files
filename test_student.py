from student import student
import unittest
class teststudent(unittest.TestCase):
    def test_email(self):
        obj1 = student("devarapalli", "prathibha",50,20)
        self.assertEqual(obj1.email, 'devarapalli.prathibha@gmail.com')
        obj1.first = "jin"
        self.assertEqual(obj1.email, 'jin.prathibha@gmail.com')
    def test_fullname(self):
        obj1 = student("devarapalli", "prathibha",50,20)
        self.assertEqual(obj1.fullname, 'devarapalli prathibha')
        obj1.first = "jin"
        self.assertEqual(obj1.fullname, 'jin prathibha')
    def test_apply_bonus(self):
        obj1 = student("devarapalli","prathibha",50,20)
        self.assertEqual(obj1.marks,50)
        obj1.apply_bonus()
        self.assertEqual(obj1.marks,75 )
   # def setup(self):
        #print("\nsetup")
    #def teardown(self):
       # print("\ntearDown")
    def test_somevalue(self):
        obj1 = student("devarapalli","prathibha",50,20)
        self.assertEqual(obj1.somevalue," ")
        obj1.some_value("blue")
        self.assertEqual(obj1.somevalue,"devarapalli.prathibha@gmail.comdevarapalli prathibhablue")
    def test_read(self):
        obj1 =student("devarapalli","prathibha",50,20)
        self.assertEqual(obj1.read,20)
        obj1.Read("mani")
        self.assertEqual(obj1.read,"devarapalli.prathibha@gmail.comdevarapalli prathibhamani")
    def test_readvalue(self):
        obj1 =student("devarapalli","prathi",50,20)
        self.assertEqual(obj1.read_value,"jk")
        obj1.readvalue("pinky","jin")
        self.assertEqual(obj1.read_value,"jkpinkyjin")




if __name__ == "__main__":
     unittest.main()



