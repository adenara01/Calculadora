from mean_var_std import calculadora
import unittest

# El caso de prueba
class UnitTests(unittest.TestCase):
    def test_calculate_with_valid_input(self):
        # Caso de prueba con una entrada válida
        result = calculadora([0, 1, 2, 3, 4, 5, 6, 7, 8])
        expected_output = {
            'media': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'varianza': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'desviacion estandar': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'maximo': [[6, 7, 8], [2, 5, 8], 8],
            'minimo': [[0, 1, 2], [0, 3, 6], 0],
            'suma': [[9, 12, 15], [3, 12, 21], 36]
        }
        self.assertEqual(result, expected_output)

    def test_calculate_with_invalid_input(self):
        # Caso de prueba con una entrada no válida
        with self.assertRaises(ValueError) as context:
            calculadora([1, 2, 3])  # Menos de 9 elementos
        self.assertEqual(str(context.exception), "La lista debe contener nueve numeros")

if __name__ == "__main__":
    try:
        unittest.main(argv=[''], exit=False)
    except SystemExit as e:
        print("Pruebas ejecutadas exitosamente")