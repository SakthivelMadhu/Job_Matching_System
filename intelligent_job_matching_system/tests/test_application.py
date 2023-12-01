import json
import unittest
from app import app, db
from app.models import Application
from flask_mongoengine.json import JSONEncoder

class ApplicationTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['MONGODB_SETTINGS'] = {'db': 'job_matching_system_db', 'host': 'localhost', 'port': 27017}
        self.app = app.test_client()
        db.init_app(app)

    def test_get_applications(self):
        response = self.app.get('/api/applications')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', data)
