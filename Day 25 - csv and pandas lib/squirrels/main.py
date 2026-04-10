# Create a csv called squirrel_count which contains primary fur colour
# Build a new data frame of how many grey, cinnamon and black ones there are
import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colours = squirrel_data["Primary Fur Color"]
gray_count = fur_colours[fur_colours == "Gray"].count()
cinnamon_count = fur_colours[fur_colours == "Cinnamon"].count()
black_count = fur_colours[fur_colours == "Black"].count()

fur_count = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

df = pandas.DataFrame(fur_count)
df.to_csv("squirrel_count.csv")


# Alternative solution
counts = squirrel_data["Primary Fur Color"].value_counts()
counts.to_csv("squirrel.csv")