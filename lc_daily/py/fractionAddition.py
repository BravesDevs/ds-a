from fractions import Fraction


class Solution:
    def fractionAddition(self, expression):
        res = Fraction(eval(expression))

        if res.numerator == 0:
            return "0/1"
        # Evaluate the expression and return the result in the form of a fraction
        evaluation = eval(res.numerator / res.denominator)
        return str(evaluation)


sln = Solution()

print(sln.fractionAddition("-1/2+1/2+1/3"))
