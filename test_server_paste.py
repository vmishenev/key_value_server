#!/usr/bin/python
# -*- coding: utf-8 -*-

from paste.fixture import TestApp

from server import app
import unittest



class TestServer(unittest.TestCase):

    def test_notfound(self):
        middleware = []
        testApp = TestApp(app.wsgifunc(*middleware))
        r = testApp.get('/storage/test', status="*")
        self.assertEqual(r.status, 404)

    def test_add(self):
        middleware = []
        testApp = TestApp(app.wsgifunc(*middleware))
        key = 'test'
        message = 'jhfsdf'
        obj_data = {'key': key, 'msg': message}
        r1 = requests.post('/storage/' + key, json=obj_data)
        r = requests.get('/storage/' + key)
        self.assertEqual(r1.status, 200)
        self.assertEqual(r.status, 200)


if __name__ == '__main__':
    unittest.main()

