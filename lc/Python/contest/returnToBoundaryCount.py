
class Solutions:
    def returnToBoundaryCount(self, nums):
        count = 0
        path = 0

        for i in nums:
            path += i
            if path == 0:
                count += 1
        return count


# Path: returnToBoundaryCountTest.py
sln = Solutions()
print(sln.returnToBoundaryCount([2, 3, -5]))

# class TestReturnToBoundaryCount(unittest.TestCase):
#     def test_returnToBoundaryCount(self):
#         s = Solutions()
#         self.assertEqual(s.returnToBoundaryCount([0, 0, 1, 1, 0, 0, 1, 1]))
#         self.assertEqual(s.returnToBoundaryCount(
#             [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]))


# if __name__ == '__main__':
#     unittest.main()
