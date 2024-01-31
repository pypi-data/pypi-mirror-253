import unittest
from src.DLMS_SPODES_client.client import Client, SerialPort


class TestType(unittest.TestCase):
    def test_init(self):
        client = Client()
        client.media = SerialPort(
            port="COM13",
            inactivity_timeout=1
        )
        client.connect()
        client.init_type()
        client.close()
        print(client.objects)
        client.SAP.set(0x30)
        client.secret = b'0000000000000000'
        client.connect()
        p = client.objects.get_object("0.0.40.0.1.255")
        # p = client.objects.get_object("1.0.99.1.0.255")
        client.read_attribute(p, 2)
        client.close()
        for el in p.object_list:
            print(el)
        print(client.reply.value)

