class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def validateIPv4(s):
            IPv4_list = s.split('.')
            if len(IPv4_list) != 4:
                return False
            for num in IPv4_list:
                if not num.isdigit() or len(num) == 0:
                    return False
                if int(num) < 0 or int(num) > 255:
                    return False
                if len(num) > 1 and num[0] == '0': 
                    return False
            return True
        
        def validateIPv6(s):
            IPv6_list = s.split(':')
            if len(IPv6_list) != 8:
                return False
            for num in IPv6_list:
                if len(num) == 0 or len(num) > 4:
                    return False
                if not all(c in "0123456789abcdefABCDEF" for c in num):
                    return False
            return True
        
        if '.' in queryIP:
            return "IPv4" if validateIPv4(queryIP) else "Neither"
        elif ':' in queryIP:
            return "IPv6" if validateIPv6(queryIP) else "Neither"
        else:
            return "Neither"
