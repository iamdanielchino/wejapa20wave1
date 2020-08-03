#Quiz: Calculate
#In this quiz you're going to do some calculations for a tiler.
#Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

#1. How many tiles are needed?
#2. You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?



#Fill this in with an expression that calculates how many tiles are needed.
length_one= 7
width_one= 9
part_one = length_one * width_one

length_two= 7
width_two= 5
part_two= length_two * width_two

total_tiles_needed = part_one + part_two
print(total_tiles_needed)

# Fill this in with an expression that calculates how many tiles will be left over.
package_tiles= 6
no_packages= 17
total_tiles = package_tiles * no_packages
leftover_tiles = total_tiles - total_tiles_needed
print(leftover_tiles)
