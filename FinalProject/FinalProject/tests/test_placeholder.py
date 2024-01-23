from flask import Flask, jsonify
import requests
import pytest

class Parameters_used():
    BASE_URL = "https://jsonplaceholder.typicode.com"
    ENDPOINTS = ["/posts", "/comments", "/todos", "/users"]

params_object = Parameters_used()

class Test_EndpointTester:

    @pytest.mark.parametrize("param_name, expected_status",
                             [("posts", 200), ("comments", 200), ("todos", 200), ("users", 200)])
    def test_get_posts(self, param_name, expected_status):
        response = requests.get(f"{params_object.BASE_URL}{params_object.ENDPOINTS}")
        assert response.status_code == expected_status, f"Failed to fetch data from {params_object.BASE_URL}{params_object.ENDPOINTS}. Status code: {response.status_code}"
        data = response.json()
        assert len(data) > 0, f"No data received from {params_object.BASE_URL}{params_object.ENDPOINTS}"
        return data


class Test_APITestingApp:
        app = Flask(__name__)

        def index(self):
            return "API Testing Script using Flask with Python"

        def test_endpoint(self, tester):
            data = tester.test("posts", 200)
            return jsonify(data)

        def add_rule(self):
            for endpoint in params_object.ENDPOINTS:
                self.app.add_url_rule(endpoint, f"endpoint_{endpoint}",view_func=lambda tester='tester': self.test_endpoint(tester))
                self.app.add_url_rule('/', 'index', self.index)

        def run(self):
        # Run the Flask app on http://127.0.0.1:5000/
          self.app.run(debug=False)


if __name__ == '__main__':
    api_testing_app = Test_APITestingApp()
    api_testing_app.run()
    # Run the tests and generate an HTML report
    pytest.main(['-v', '--html=report.html'])
