class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        last= len(nums1)-1
        while m>0 and n>0:
            if nums1[m-1]> nums2[n-1]:
                nums1[last]=nums1[m-1]
                m-=1
            else:
                nums1[last]=nums2[n-1]
                n-=1
            last-=1

        while n>0:
            nums1[last] = nums2[n-1]
            last-=1
            n-=1
        
        return nums1

    def merge1(self, nums1, m: int, nums2, n: int) -> None:
        last= len(nums1)-1
        while n>0:
            if m<=0 or nums2[n-1]>=nums1[m-1]:
                nums1[last] = nums2[n-1]
                n-=1
            else:
                nums1[last] = nums1[m-1]
                m-=1
            last-=1
        return nums1



item  = Solution()
print(item.merge1([0], 0,[1],1))