import unittest
from app import create_app
from app.models import db_session, Notification

class TestSchema(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        db_session.remove()

    def test_send_notification(self):
        response = self.client.post('/graphql', json={'query': '''
            mutation {
                sendNotification(userId: 1, message: "Your order has been shipped!") {
                    notification {
                        id
                        userId
                        message
                        status
                    }
                }
            }
        '''})
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json)

    def test_get_notification(self):
        # First, send a notification
        self.test_send_notification()
        
        response = self.client.post('/graphql', json={'query': '''
            query {
                getNotification(id: 1) {
                    id
                    userId
                    message
                    status
                }
            }
        '''})
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json)

if __name__ == '__main__':
    unittest.main()
