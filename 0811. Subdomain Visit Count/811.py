class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = {}
        for case in cpdomains:
            ct, domains = case.split(' ')
            domains = domains.split('.')[::-1]
            for i in range(1, len(domains) + 1):
                uni_domain = '.'.join(domains[:i][::-1])

                if ans.get(uni_domain):
                    ans[uni_domain] += int(ct)

                else:
                    ans[uni_domain] = int(ct)

        return ["{ct} {domain}".format(ct=v, domain=k) for k, v in ans.items()]
