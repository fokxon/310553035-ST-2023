import unittest
from unittest.mock import patch, Mock
import course_scheduling_system

class SystemTest(unittest.TestCase):
    @patch('course_scheduling_system.CSS.check_course_exist')
    def test_q1_1(self, mock_check_course_exist):
        mock_check_course_exist.return_value = True
        
        css = course_scheduling_system.CSS()
        self.assertTrue(css.add_course(('Algorithms', 'Monday', 3, 4)))
        self.assertEqual(css.get_course_list(), [('Algorithms', 'Monday', 3, 4)])

    @patch('course_scheduling_system.CSS.check_course_exist')
    def test_q1_2(self, mock_check_course_exist):
        mock_check_course_exist.return_value = True

        css = course_scheduling_system.CSS()
        self.assertTrue(css.add_course(('OS', 'Monday', 4, 5)))  
        self.assertFalse(css.add_course(('Algorithms', 'Monday', 3, 4)))
        self.assertEqual(css.get_course_list(), [('OS', 'Monday', 4, 5)])
    
    @patch('course_scheduling_system.CSS.check_course_exist')
    def test_q1_3(self, mock_check_course_exist):
        mock_check_course_exist.return_value = False

        css = course_scheduling_system.CSS()
        self.assertFalse(css.add_course(('Algorithms', 'Monday', 3, 4)))
        self.assertEqual(css.get_course_list(), [])

    @patch('course_scheduling_system.CSS.check_course_exist')
    def test_q1_4(self, mock_check_course_exist):
        mock_check_course_exist.return_value = True

        css = course_scheduling_system.CSS()
        self.assertRaises(TypeError, css.add_course, (1, 2, 3))

    @patch('course_scheduling_system.CSS.check_course_exist')
    def test_q1_5(self, mock_check_course_exist):
        mock_check_course_exist.return_value = True

        css = course_scheduling_system.CSS()
        self.assertTrue(css.add_course(('OS', 'Monday', 4, 5)))
        self.assertTrue(css.add_course(('Algorithms', 'Tuesday', 3, 4)))
        self.assertTrue(css.add_course(('Compiler', 'Monday', 6, 6)))
        self.assertTrue(css.remove_course(('Algorithms', 'Tuesday', 3, 4)))
        self.assertEqual(css.get_course_list(), [('OS', 'Monday', 4, 5), ('Compiler', 'Monday', 6, 6)])
        self.assertEqual(css.check_course_exist.call_count, 4)
        print(str(css))

    @patch('course_scheduling_system.CSS.check_course_exist')
    def test_q1_6(self, mock_check_course_exist):
        mock_check_course_exist.return_value = True

        css = course_scheduling_system.CSS()    
        self.assertRaises(TypeError, css.add_course, (1, 2, 3, 4))
        self.assertRaises(TypeError, css.add_course, ('Algorithms', 'Saturday', 3, 4))
        self.assertRaises(TypeError, css.add_course, ('Algorithms', 'Friday', 'C', 'D'))
        self.assertFalse(css.remove_course(('Algorithms', 'Tuesday', 3, 4)))
        mock_check_course_exist.return_value = False
        self.assertFalse(css.remove_course(('Algorithms', 'Tuesday', 3, 4)))



if __name__ == "__main__":
    unittest.main()