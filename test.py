from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):
        self.client = app.test_client()
        app.config["TESTING"] =True
    def test_gamepage(self):
        with self.client:
            res = self.client.get("/")
            html = res.get_data(as_text = True)

            self.assertEqual(res.status_code, 200)
            self.assertIn( '<label for="played">Games played :</label>' , html)
            self.assertIn("board", session)
            self.assertIsNone(session.get("played"))

    def test_check_word(self):
        with self.client:
            with self.client.session_transaction() as sess:
                sess["board"]= [["A", "A", "D", "E", "F"], 
                                 ["S", "A", "T", "R", "C"], 
                                 ["H", "E", "L", "L", "O"], 
                                 ["V", "Z", "X", "", "B"], 
                                 ["X", "A", "C", "B", "X"]]
        res = self.client.get("/check-word?word=hello")
        self.assertEqual(res.json["result"], "ok")
    def test_post(self):
        with self.client:
            with self.client.session_transaction() as sess:
                sess["points"] =25

            res = self.client.post("/post-score", json={"points":25})

            self.assertEqual(res.status_code, 200)
        
