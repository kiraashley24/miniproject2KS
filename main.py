# INF 601 - Advanced Programming in Python
# Kira Selucky
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt

#(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.

#What Countries are the happiest?


#(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.

#Create pandas dataframe
data = pd.read_csv('happiness.csv', index_col='Countries')

#Create series data to focus on "Happiness index, 2022" values
seriesData = pd.Series(data["Happiness index, 2022"])

#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.

#Graph 1 showing top 5 happiest countries according to the index
def topRankedGraph():
    #Take top 5 countries
    dataFive = seriesData.head(5)

    #Plot graph
    dataFive.plot()
    plt.ylim(7.3, 7.9)

    #Add labels
    plt.xlabel("Global rank", color='blue')
    plt.ylabel("Happiness Index", color= 'green')
    plt.title("Countries Ranked by Happiness")

    #Show graph
    plt.show()

#Graph 2 showing stats
def statsGraph():
    #Get mean, median, min, and max values
    meanValue = seriesData.mean()
    medianValue = seriesData.median()
    minValue = seriesData.min()
    maxValue = seriesData.max()

    #Create bar graph
    plt.bar(['Mean', 'Median', 'Minimum', 'Maximum'], [meanValue, medianValue, minValue, maxValue])
    plt.ylim(1, 8)

    #Add labels
    plt.xlabel("Stat Values")
    plt.ylabel("Happiness Index")
    plt.title("Statistics of Global Happiness Index")

    #Show graph
    plt.show()

#Graph 3 of ranges/count of happiness index
def rangeGraph():
    #Seperate series data into two ranges of data to use for two subplots
    lowerRange = seriesData[seriesData < 5]
    higherRange = seriesData[seriesData >= 5]

    # Create a figure with two subplots
    fig, axes = plt.subplots(2)
    fig.suptitle('Number of Countries Range Subplots')

    #Setting axes 0 and 1 values/colors
    axes[0].plot(higherRange, color='green')
    axes[1].plot(lowerRange, color='red')

    #Set titles
    axes[0].set_title("Happiness Index of 5 or greater", color='green')
    axes[1].set_title("Happiness Index of less than 5", color='red')

    #Remove country tick labels
    axes[0].set_xticklabels([])
    axes[1].set_xticklabels([])

    #Create count legends
    axes[0].legend([len(higherRange)])
    axes[1].legend([len(lowerRange)])

    # Show the subplots
    plt.show()

#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.



#Start of program
topRankedGraph()
statsGraph()
rangeGraph()



#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.


