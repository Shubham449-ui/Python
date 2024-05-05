grade_dict = {"Average":5,"Bad":3,"Good":6,"Outstanding":9,"Below Average":4,"Excellent":8,"Very Good":7}

grade_dict_sort = dict(sorted(grade_dict.items(),key=lambda item:item[1]))

print("<----- Sorted Keys in terms of values --->")
for key,values in grade_dict_sort.items():
    print(f"{key}:{values}")

grade_dict_sort = dict(sorted(grade_dict.items()))
print("<----- Sorted Keys in terms of keys --->")
for key,values in grade_dict_sort.items():
    print(f"{key}:{values}")
