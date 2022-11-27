from mtree import MTree
import math
def d_int(a, b): # define a distance function for numbers
    return math.sqrt ((b.x-a.x)**2 + (b.y-a.y)**2)
class Country: 
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
def main():
    mtree = MTree(d_int,max_node_size=4)# create an empty M-tree
    Peru = Country("Peru",66477,5983)
    Bulgaria = Country("Bulgaria",101106,4139)
    Bosnia = Country("Bosnia and Herzegovina",84584,3870)
    Montenegro = Country("Montenegro" ,250528,3673)
    Macedonia = Country( "North Macedonia" ,103485 ,3639)
    Hungary = Country("Hungary" ,114600 ,3586)
    Czechia = Country("Czechia",200245 ,3080)
    Georgia = Country("Georgia" ,212561 ,3030)
    Romania = Country( "Romania",93390 ,2966)
    Gibraltar = Country("Gibraltar", 215221 ,2910)
    Brazil = Country("Brazil", 102912, 2863)
    Marino = Country("San Marino", 175688, 2733)
    Croatia = Country("Croatia", 149455 ,2678)
    Slovakia= Country("Slovakia", 124480 ,2639)
    Argentina = Country("Argentina", 116439, 2547)
    Armenia = Country("Armenia" ,113938 ,2547)
    Lituania = Country("Lithuania" ,176235, 2525)
    Slovenia= Country("Slovenia", 202419 ,2512)
    Colombia = Country("Colombia" ,98156 ,2489)
    USA = Country("USA ",148104 ,2406)
    mtree.add(Peru)
    mtree.add(Bulgaria)
    mtree.add(Bosnia)
    mtree.add(Montenegro)
    mtree.add(Macedonia)
    #mtree.draw()
    mtree.add(Hungary)
    mtree.add(Czechia)
    mtree.add(Georgia)
    mtree.add(Romania)
    mtree.add(Gibraltar)
    mtree.add(Brazil)
    mtree.add(Marino)
    mtree.add(Croatia)
    mtree.add(Slovakia)
    mtree.add(Argentina)
    mtree.add(Armenia)
    mtree.add(Lituania)
    mtree.add(Slovenia)
    mtree.add(Colombia)
    mtree.add(USA)
    result = mtree.search(Hungary)
    for i in result:
        print(i.name + ' at (' + str(i.x) + ', ' + str(i.y) + ') with ' + str(d_int(Hungary, i)))
    
    lista = list(result)
    
    print(d_int(Peru,Bulgaria))
if __name__ == '__main__':
	main()