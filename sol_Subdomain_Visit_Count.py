"""
Example 2:
Input:
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output:
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation:
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
"""


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        stat = {}
        ret = []

        for d in cpdomains:
            cnt, domain = d.split(' ')
            cnt = int(cnt)
            domain = domain.split('.')
            for i in range(len(domain)):
                d = '.'.join(domain[len(domain) - i - 1:])
                stat.setdefault(d, 0)
                stat[d] += cnt

        for k in stat:
            ret.append('{} {}'.format(stat[k], k))

        return ret


sol = Solution()
ret = sol.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
print(ret)
