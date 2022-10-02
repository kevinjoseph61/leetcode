class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for i in emails:
            pre, suff = i.split('@')
            pre = pre.replace(".", "")
            index = pre.find("+")
            pre = pre[:index] if index!=-1 else pre
            unique.add(pre + "@" + suff)
        return len(unique)