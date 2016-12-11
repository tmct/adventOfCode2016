from IP import IP


class Solver7:
    def count_ips_supporting_tls(self, ip_file_name):
        tls_count = 0
        with open(ip_file_name, 'r') as ip_file:
            for line in ip_file:
                ip = IP(line.strip())
                if ip.supports_tls:
                    tls_count += 1
        return tls_count

    def count_ips_supporting_ssl(self, ip_file_name):
        tls_count = 0
        with open(ip_file_name, 'r') as ip_file:
            for line in ip_file:
                ip = IP(line.strip())
                if ip.supports_ssl:
                    tls_count += 1
        return tls_count
