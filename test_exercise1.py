import unittest

def str_to_bool(value):    # recebe uma cadeia de caracteres e retorna True ou False
    try:
        value = value.lower()          # transforma os caracteres em lower case
    except AttributeError:
        raise AttributeError(f"{value} must be of type string")       # gera uma mensagem de erro caso o valor inserido não seja string
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False
    
class TestStrToBool(unittest.TestCase):

    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('Yes')
        self.assertTrue(result)

    def test_invalid_input(self):             # esse teste verifica se AttributeError é gerado pela entrada n cadeia de caracteres
        with self.assertRaises(AttributeError):
            str_to_bool(1)

if __name__ == '__main__':
    unittest.main()