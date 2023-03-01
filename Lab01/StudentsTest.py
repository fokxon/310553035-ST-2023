import unittest
import Students

class Test(unittest.TestCase):
    students = Students.Students()

    user_name = ['John', 'Mary', 'Thomas', 'Jane']
    user_id = dict()

    # test case function to check the Students.set_name function
    def test_0_set_name(self):
        print("Start set_name test\n")

        for name in self.user_name:
            id = self.students.set_name(name)
            self.assertFalse(id < 0)
            self.assertFalse(id in self.user_id)
            self.user_id[id] = name
            print(id, name)
        
        print("\nFinish set_name test\n")

    # test case function to check the Students.get_name function
    def test_1_get_name(self):
        print("Start get_name test\n")

        for id, name in self.user_id.items():
            self.assertEqual(self.students.get_name(id), name)
            print("id", id, ":", name)
        firstNonExistId = 0
        while firstNonExistId in self.user_id:
            firstNonExistId += 1
        self.assertEqual(self.students.get_name(firstNonExistId), "There is no such user")
        print("id", firstNonExistId, ":", "There is no such user")
        
        print("\nFinish get_name test")

if __name__ == '__main__':
    unittest.main()
