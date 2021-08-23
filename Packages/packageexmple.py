# from Packages.packageintro import add  # using add function from a module in Packages package
# add(7,3)

from Packages.packageintro import *  # can use all functions from a module in Packages package
add(7,3)
sub(8,3)

from package1.printEXample import *  # importing another packge
printinfo()
