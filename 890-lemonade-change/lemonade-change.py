class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five_dollars = 0  # To track the number of $5 bills
        ten_dollars = 0   # To track the number of $10 bills

        for bill in bills:
            if bill == 5:
                five_dollars += 1  # Collect a $5 bill

            elif bill == 10:
                if five_dollars > 0:
                    five_dollars -= 1  # Give change with one $5 bill
                    ten_dollars += 1   # Collect the $10 bill
                else:
                    return False  # No $5 bill to give change

            elif bill == 20:
                if ten_dollars > 0 and five_dollars > 0:
                    ten_dollars -= 1  # Give change with one $10 bill
                    five_dollars -= 1 # and one $5 bill
                elif five_dollars >= 3:
                    five_dollars -= 3  # Give change with three $5 bills
                else:
                    return False  # Not enough bills to give change

        return True  # Successfully provided change for all customers
