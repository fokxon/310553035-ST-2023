import unittest
from unittest.mock import patch, Mock
import app

class fake_mail:
    def write(self, name):
        context = 'Congrats, ' + name + '!'
        return context

    def send(self, name, context):
        print(context)


class ApplicationTest(unittest.TestCase):

    def setUp(self):
        # stub
        people = ["William", "Oliver", "Henry", "Liam"]
        selected = ["William", "Oliver", "Henry"]
        return (people, selected)

    @patch('app.Application.get_random_person')
    @patch('app.Application.get_names')
    def test_app(self, mock_get_names, mock_get_random_person):
        # mock
        mock_get_names.side_effect = self.setUp
        mock_get_random_person.side_effect = ['William', 'Oliver', 'Henry', 'Liam']
        # spy
        App = app.Application()
        selected = App.select_next_person()
        self.assertEqual(selected, "Liam")
        print(selected, "selected")

        App.mailSystem = Mock()
        App.mailSystem.write.side_effect = fake_mail().write
        App.mailSystem.send.side_effect = fake_mail().send
        App.notify_selected()
        print("\n\n")

        print(App.mailSystem.write.call_args_list)
        print(App.mailSystem.send.call_args_list)
        self.assertEqual(App.mailSystem.write.call_count, len(App.selected))
        self.assertEqual(App.mailSystem.send.call_count, len(App.selected))


if __name__ == "__main__":
    unittest.main()
