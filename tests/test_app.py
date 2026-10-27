import unittest
from app import draft_outreach
class OutreachTests(unittest.TestCase):
    def setUp(self):
        self.prospect={"name":"Jordan Rivera","company":"Acme Travel","context":"your team recently expanded its partner network","relevance":"manual partner onboarding can slow launches"}
    def test_email_is_draft_only(self):
        result=draft_outreach(self.prospect,offer="workflow automation",sender="Hardik")
        self.assertIn("Hi Jordan",result["message"]); self.assertFalse(result["sent"]); self.assertEqual(result["status"],"draft_pending_human_review")
    def test_linkedin_channel(self):
        self.assertIn("Open to connecting?",draft_outreach(self.prospect,offer="AI workflow reviews",sender="Hardik",channel="linkedin")["message"])
    def test_missing_context_rejected(self):
        with self.assertRaises(ValueError): draft_outreach({"name":"Jordan"},offer="automation",sender="Hardik")
if __name__=="__main__": unittest.main()
