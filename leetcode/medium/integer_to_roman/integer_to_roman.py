
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        nums = {
            "I":1,   "II":2,   "III":3,   "IV":4,   "V":5,   "IX":9, 
            "X":10,  "XX":20,  "XXX":30,  "XL":40,  "L":50,  "XC":90,
            "C":100, "CC":200, "CCC":300, "CD":400, "D":500, "CM":900,
            "M":1000,"MM":2000,"MMM":3000
        }
        
        s = ""
        while num > 0:
            picked = None
            
            for letters, weight in nums.items():
                if weight <= num:
                    if picked is None:
                        picked = letters
                    elif weight > nums[picked]:
                        picked = letters

            num -= nums[picked]
            s += picked
            
        return s

