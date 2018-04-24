# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import unittest
from udp_test import show_info

class TestUdpTest(unittest.TestCase):

    def test01(self):
        remote = ("127.0.0.1", 5005)
        if sys.version.startswith("2"):
            message = "hello world"
        else:
            message = b"hello world"
        show_info(message, remote, "Get a message from")

    def test02(self):
        remote = ("127.0.0.1", 5005)
        message = "测试数据".encode("utf-8")
        show_info(message, remote, "Get a message from")
