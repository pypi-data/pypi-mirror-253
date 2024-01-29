import unittest
from xml.etree import ElementTree

from midpoint_cli.client.objects import MidpointUser, MidpointObjectList


class ClientModeltest(unittest.TestCase):
    def test_model_user01(self):
        with open('sample-user-01.xml', 'r') as f:
            tree = ElementTree.fromstring(f.read())
            user = MidpointUser(xml_entity=tree)
            self.assertEqual(None, user['FullName'])

    def test_model_user02(self):
        with open('sample-user-02.xml', 'r') as f:
            tree = ElementTree.fromstring(f.read())
            user = MidpointUser(xml_entity=tree)
            self.assertEqual('Lieutenant Templeton Arthur Peck', user['FullName'])

    def test_model_list(self):
        with open('sample-user-01.xml', 'r') as f1, open('sample-user-02.xml', 'r') as f2:
            user1 = MidpointUser(xml_entity=(ElementTree.fromstring(f1.read())))
            user2 = MidpointUser(xml_entity=(ElementTree.fromstring(f2.read())))

            list = MidpointObjectList()
            list.append(user1)
            list.append(user2)
            self.assertEqual(len(list),2)
            self.assertEqual(user2,list.find_object('566cff7d-f2e1-4669-b9bc-1988bbe4be5c'))
            self.assertEqual(None,list.find_object('BOGUS_ID'))



if __name__ == '__main__':
    unittest.main()
