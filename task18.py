nums = input("Введите список целых значений через пробел: ").split(" ")
k = input("Введите целое число: ")
nums1 = [abs(int(i)-int(k)) for i in nums] 
print(f"Cамый близкий по величине элемент к заданному числу {k}: {min([nums[i] for i in range(1, len(nums)) if nums1[i]==min(nums1)])}")