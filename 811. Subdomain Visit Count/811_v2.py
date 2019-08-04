class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split(' ')
            count = int(count)
            domains = domain.split('.')
            for i in range(len(domains)):
                ans['.'.join(domains[i:])] += count

        return ["{count} {domain}".format(count=v, domain=k) for k, v in ans.items()]