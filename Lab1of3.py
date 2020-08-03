#Note that this code uses scientific notation to define large numbers. 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall_decrease = 0.1 * rainfall
runoff = rainfall - rainfall_decrease


# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall 


# increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm
reservoir_increase = 0.05 * reservoir_volume
storm_water = reservoir_volume + reservoir_increase


# decrease reservoir_volume by 5% to account for evaporation
reservoir_decrease = 0.05 * reservoir_volume
evaporation = reservoir_volume - reservoir_decrease


# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.
arid_regions_water = reservoir_volume - 2.5e5


# print the new value of the reservoir_volume variable
print (reservoir_volume)
