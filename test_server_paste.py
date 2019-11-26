#!/usr/bin/python
# -*- coding: utf-8 -*-

from paste.fixture import TestApp

from server import app
import unittest



class TestServer(unittest.TestCase):

    def test_notfound(self):
        middleware = []
        testApp = TestApp(app.wsgifunc(*middleware))
        r = testApp.get('/storage/test')
        self.assertEqual(r.status, 404)



if __name__ == '__main__':
    unittest.main()

