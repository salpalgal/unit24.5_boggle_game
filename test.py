from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def test_gamepage(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text = True)

            self.assertEqual(res.status_code, 200)
            self.assertIn( '<label for="played">Games played :</label>' , html)
            

    def test_
        
