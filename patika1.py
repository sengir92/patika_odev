sample_list = [[1,"a",["cat"],2],[[3]],"dog",4,5]
flat_list = []

def flatten_list (n):
    for i in n:
        if isinstance(i,list):
            flatten_list(i)
        else:
            flat_list.append(i)
            
flatten_list(sample_list)
print(flat_list)
    
