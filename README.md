# Data Visualization 

2018 course project 

## Title
Exploring the relationship between National Education Expenditure and Youth Literacy Rate

## Objective of the project
#### a brief context of the project, and what tasks you're aiming to solve using visualizations, domain(target user) and task abstraction.
This visualization project serves mainly as an educational tool. The primary function of this project is to demonstrate how the government expenditure on education (% of GDP) and the Youth (15 - 24) Literacy rate of every country in the world change over time, from 1990 to 2017. Readers can make comparison among different countries as well as comparing how was the perfornamce one particular country in terms of the aformensioned two indicators in different years. 
It can be used in several contexts described below: 
* Helping World Bank to improve the user-friendliness of its data hub website by adding interactive visualization so that visitors can dig more insightful information ot of the datasets;
* Providing visualization tools for scholars in thier research on the effects of education on iliteracy on a global scale;
* Assisting economic or sociology lecturers in Universities to show students how educational expenditure and literacy rate change over time, and to inspire students to explore the possible interactions between these two factors. 
The target users are scholars, students, policy makers in international organizations, and general users of World Bank datasets, etc.


## Overview

![Alt text](ScreenShot_1.png)

![Alt text](ScreenShot_2.png)

__Team Member__

 Fangshu Lin[(fangshulin)](https://github.com/fangshulin)

Hongkai He[(davidhhk1994)](https://github.com/davidhhk1994)

 Yixuan Tang[(yixuantang)](https://github.com/yixuantang)

## Visualization description
This visualization project consists of two choropleth maps. The top map depicts how much each country in the world spent (% of GDP)on education in a particular year. The bottom map tells reader the how many people between 15 and 24 in each country in the world can read and write. 

interaction: Each map has a corresponding slider bar. By dragging the slider bars from left to right, a reader can see the change of the two factors over time from 1990 to 2016 by observing the change in color lightness (or value) in each country. The reader can also compare the two factors in the same year by abchoring the two slider bars at the same position. In addition, below each map there is a bar chart changing synchronically with the map. The bar chart shows the absolute education expenditure or literacy rate value of each country with the height and the color lightness of a signle bar represent the value of the corresponding country. It is worth noticing that number of bars also changes depending on how many countries have or do not have data in a given year. For example, if in a year there are 54 countries have actual data entries and the other countries does not have, there will be only 54 bars displayed in the bar chart. the x ticks of the bar charts are three-letter country name abbreviations. Another interaction is that if the reader moves his/her curser onto one category in the legend, the map will only display the countries that fall in this category in color. Countries in all other categories will be in light grey.



## Datasets

all the datasets are obtained from World Bank data hub. The name and link of each dataset are listed as follows:

[Government expenditure on education, total (% of GDP)](https://data.worldbank.org/indicator/SE.XPD.TOTL.GD.ZS?view=chart)
[Literacy rate, youth female (% of females ages 15-24)](https://data.worldbank.org/indicator/SE.ADT.1524.LT.FE.ZS)

The datasets have a time span from 1960 to now. However we only select data after 1990 because there is great absence of observations before 1990 in both datasets and this will lead to poor visualization effects. 


## Outcome and Evaluation


## Link to the Visualization
* Check our Website [here](http://vis2018g16.pythonanywhere.com) !

## Possible Future Work


