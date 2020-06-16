class Solution:
    def check_ipv4(self, ip):
        if ':' in ip:
            return False

        sub_ips = ip.split('.')
        is_4_sub_ips = len(sub_ips) == 4
        is_lead_zero = functools.reduce(lambda x, y: x or y, map(lambda s: s.startswith('0') and len(s) > 1, sub_ips))
        is_all_digit = functools.reduce(lambda x, y: x and y, map(lambda s: re.match("^[0-9]*$", s), sub_ips))
        try:
            is_range_ok = functools.reduce(lambda x, y: x and y, map(lambda s: 0 <= int(s) <= 255, sub_ips))

        except:
            return False

        return is_4_sub_ips and is_all_digit and not is_lead_zero and is_range_ok

    def check_ipv6(self, ip):
        if '.' in ip:
            return False

        sub_ips = ip.split(':')
        is_8_sub_ips = len(sub_ips) == 8
        is_4_char = functools.reduce(lambda x, y: x and y, map(lambda s: len(s)<=4, sub_ips))
        is_valid = functools.reduce(lambda x, y: x and y, map(lambda s: re.match("^[A-Za-z0-9]*$", s), sub_ips))
        try:
            list(map(lambda s: hex(int(s, 16)), sub_ips))

        except:
            return False

        return is_8_sub_ips and is_4_char and is_valid

    def validIPAddress(self, IP: str) -> str:
        if self.check_ipv4(IP):
            return "IPv4"

        if self.check_ipv6(IP):
            return "IPv6"

        return "Neither"
