# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        infodict = dict()
        importance = 0

        for e in employees:
            infodict[e.id] = e

        queue = [id, ]

        while queue:
            info = infodict[queue.pop(0)]
            importance += info.importance
            queue.extend(info.subordinates)

        return importance
