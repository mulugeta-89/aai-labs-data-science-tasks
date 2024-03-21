import unittest
import json
from app import app


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict_gdp_endpoint(self):
        """
        Test the /predict_gdp endpoint.

        Sends a POST request to the /predict_gdp endpoint with sample input data
        and verifies that the response contains 'predicted_gdp_per_capita'.
        """
        # Prepare sample input data
        input_data = {
            "PCPIPCH": 2.93,
            "TM_RPCH": 4.355,
            "LE": 0,
            "PCPIEPCH": 3,
            "NGSD_NGDP": 15.746,
            "continent": "Europe"
        }

        # Send a POST request to the predict_gdp endpoint with sample input data
        response = self.app.post('/predict_gdp', json=input_data)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Convert response data from bytes to dictionary
        response_data = json.loads(response.data)

        # Check if the response contains predicted_gdp_per_capita
        self.assertIn('predicted_gdp_per_capita', response_data)

    def test_invalid_continent(self):
        """
        Test the behavior when an invalid continent is provided in the input data.

        Sends a POST request to the /predict_gdp endpoint with sample input data
        containing an invalid continent. Verifies that the response status code is 404
        (Not Found) and checks if the response contains an error message indicating
        that the model was not found for the specified continent.
        """
        # Prepare sample input data with an invalid continent or valid continent with invalid features
        input_data = {
            "PCPIPCH": 2.93,
            "TM_RPCH": 4.355,
            "LE": 0,
            "PCPIEPCH": 3,
            "NGSD_NGDP": 15.746,
            "continent": "Eurasia"
        }

        # Send a POST request to the predict_gdp endpoint with sample input data
        response = self.app.post('/predict_gdp', json=input_data)

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Check if the response contains an error message indicating the model was not found
        self.assertEqual(response.data.decode('utf-8'), "Model not found for the specified continent!")

    def test_valid_continent_but_invalid_features(self):
        """
        Test the behavior when valid continent is provided but with invalid features.

        Sends a POST request to the /predict_gdp endpoint with sample input data
        containing a valid continent but with invalid features. Verifies that the
        response status code is 500 (Internal Server Error) and checks if the response
        contains an error message indicating that invalid features were given.
        """
        # Prepare sample input data with a valid continent but invalid features
        input_data = {
            "PCPIPCH": 2.93,
            "TM_RPCH": 4.355,
            "LE": 0,
            "PCPIEPCH": 3,
            "NGSD_NGDP": 15.746,
            "continent": "Asia"
        }

        # Send a POST request to the predict_gdp endpoint with sample input data
        response = self.app.post('/predict_gdp', json=input_data)

        # Check if the response status code is 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)

        # Check if the response contains an error message indicating that invalid features were given
        self.assertEqual(response.data.decode('utf-8'), "Invalid Features Given")


if __name__ == '__main__':
    unittest.main()
