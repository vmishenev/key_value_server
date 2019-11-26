#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import requests

# from server import app

class TestServer(unittest.TestCase):

    def test_add_get_remove(self):

      # #r = app.get('/storage/keyv')
      # print(r)
        key = 'test'
        message = 'jhfsdf'
        obj_data = {'key': key, 'msg': message}
        r1 = requests.post('http://localhost/storage/' + key, json=obj_data)
        r = requests.get('http://localhost/storage/' + key)
        print(r1)
        response = r.json()
        self.assertEqual(response['Status'], 'OK')
        #self.assertEqual(response['message'], message)


if __name__ == '__main__':
    unittest.main()

			
