# Vertical Concatenation in Matrix
# ================================\n
'''
Input : [[“Gfg”, “good”], [“is”, “for”]] 
Output : [‘Gfgis’, ‘goodfor’] 
Explanation : Column wise concatenated Strings, “Gfg” concatenated with “is”, and so on. 

Input : [[“Gfg”, “good”, “geeks”], [“is”, “for”, “best”]] 
Output : [‘Gfgis’, ‘goodfor’, “geeksbest”] 
Explanation : Column wise concatenated Strings, “Gfg” concatenated with “is”, and so on.

'''
# Using numpy.transpose() and numpy.ravel()
# =======================================\n
import numpy as np
 
test_list = [["Gfg", "good"], ["is", "for"], ["Best"]]
 
max_len = max(len(sublist) for sublist in test_list)
 
padded_list = [sublist + [''] * (max_len - len(sublist)) for sublist in test_list]
 
arr = np.array(padded_list)
 
arr_t = arr.T
 
res = [''.join(row) for row in arr_t]
 
print("List after column concatenation: " + str(res))
