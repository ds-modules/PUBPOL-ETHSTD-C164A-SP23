from datascience import *
import numpy as np


# import the widgets module
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual

wages_ethnicity = Table.read_table("Data/YouthEarningsByEthnicity.csv")


#run this cell 

#function used to graph line plots comparing the Median Weekly Earning for two demographic groups over time
def demographics_comparison(s1, e1, s2, e2):
    group1 = wages_ethnicity.where("Ethnicity", are.equal_to(e1)).where("Sex", are.equal_to(s1))
    group2 = wages_ethnicity.where("Ethnicity", are.equal_to(e2)).where("Sex", are.equal_to(s2))
        
    label1 = e1 + " " + s1
    label2 = e2 + " " + s2

    plt.plot(group1["Year"], group1["Median Weekly Earnings"], label = label1)
    plt.plot(group2["Year"], group2["Median Weekly Earnings"], label = label2)
    plt.legend(loc='upper left');
    plt.title('Comparison of Two Demographic Groups')
    plt.xlabel("Year")
    plt.ylabel("Median Weekly Earnings")


    plt.show()

interact(demographics_comparison, 
         s1=widgets.Dropdown(
            options=['All', 'Male', 'Female'],
            value='All',
            description='Sex 1:',
            disabled=False),
         e1=widgets.Dropdown(
            options=['Asian', 'Black', 'Latinx', 'White'],
            value='Asian',
            description='Ethnicity 1:',
            disabled=False),
        s2=widgets.Dropdown(
            options=['All', 'Male', 'Female'],
            value='All',
            description='Sex 2:',
            disabled=False),
         e2=widgets.Dropdown(
            options=['Asian', 'Black', 'Latinx', 'White'],
            value='Black',
            description='Ethnicity 2:',
            disabled=False));
