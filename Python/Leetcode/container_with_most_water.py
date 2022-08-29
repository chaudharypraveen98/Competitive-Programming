def max_area(height):
  i, j = 0, len(height) - 1
  water = 0
  while i < j:
      water = max(water, (j - i) * min(height[i], height[j]))
      if height[i] < height[j]:
          i += 1
      else:
          j -= 1
  return water
  
if __name__ == "__main__":
  nums = [1,1]
  print(max_area(nums))