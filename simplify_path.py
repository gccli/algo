#! /usr/bin/env python


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        s = []
        for i in path.split('/'):
            if i == '.' or len(i)==0:
                continue
            elif i == '..':
                if s: s.pop()
            else:
                s.append(i)

        return '/'+'/'.join(s).rstrip('/')

print Solution().simplifyPath('/a/./b/../../c/')
print Solution().simplifyPath('/..//a')
print Solution().simplifyPath('/home//a')
