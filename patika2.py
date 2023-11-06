input_list = [[1,2],[3,4],[5,6,7]]
def reverse_list(liste):
    new_list = []
    for x in liste:
        x.reverse()
        new_list.append(x)
    new_list.reverse()
    return(new_list)
