import unittest
import uuid

from toolkit import validation


class IsEmailTests(unittest.TestCase):
    def test_ordinary_address(self):
        self.assertTrue(validation.is_email("a@b.com"))

    def test_domain_needs_a_dot(self):
        self.assertFalse(validation.is_email("a@b"))

    def test_spaces_are_not_allowed(self):
        self.assertFalse(validation.is_email("a b@c.com"))


class IsIpv4Tests(unittest.TestCase):
    def test_ordinary_address(self):
        self.assertTrue(validation.is_ipv4("192.168.0.1"))

    def test_octet_out_of_range(self):
        self.assertFalse(validation.is_ipv4("256.0.0.1"))

    def test_leading_zero_is_refused(self):
        self.assertFalse(validation.is_ipv4("01.2.3.4"))

    def test_wrong_number_of_octets(self):
        self.assertFalse(validation.is_ipv4("1.2.3"))


class IsHexColorTests(unittest.TestCase):
    def test_both_lengths(self):
        self.assertTrue(validation.is_hex_color("#FFF"))
        self.assertTrue(validation.is_hex_color("#ffffff"))

    def test_wrong_length(self):
        self.assertFalse(validation.is_hex_color("#ff"))


class IsUuidTests(unittest.TestCase):
    def test_a_real_one(self):
        self.assertTrue(validation.is_uuid(str(uuid.uuid4())))

    def test_not_one(self):
        self.assertFalse(validation.is_uuid("nope"))


if __name__ == "__main__":
    unittest.main()
