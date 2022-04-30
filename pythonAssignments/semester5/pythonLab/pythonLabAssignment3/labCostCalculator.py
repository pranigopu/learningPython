# The university is setting up a new lab at their premises.
# Write a Python function to determine the approximate cost of setting up the lab.
# Total cost = Cost of computers + Cost of chairs + Cost of tables
# If we require 50 computers, chairs and tables, and
# Cost of computer = 50'000
# Cost of chair = 200
# Cost of table = 300
# calculate the total cost

# This program can be done in much simpler ways.
# However, this is now a practice of the concepts of lambda, map and zip.
def labCostCalculator(quantities, costs):
    try: totalCost = sum(tuple(map(lambda x : x[0] * x[1], tuple(zip(quantities, costs)))))
    except: return "Input error!"
    return totalCost
print(labCostCalculator([50, 50, 50], [50000, 200, 300]))
# If the sizes are mismatched, it will only return the total cost until the last element of the smaller iterable object.