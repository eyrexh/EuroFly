# Proposal

## Section 1: Motivation and Purpose

Our role: Data scientist consultancy firm

Target audience: Flight aviation fans who would like to explore various flights in a Europe airport at a certain time.

Flight aviation fans who enjoy visiting different airport and check the flights dream about having unforgettable experiences in an airport that is busy and contains various flight at a certain time! Since travelling is expensive so exploring the busiest airports at their busiest time will be time efficiency and money saving! Our proposed dashboard would be a reliable tool that can help fans who love airports and flights to embark on memorable adventures in a European airport by providing them with the information. The proposed dashboard is a one-stop shop for finding relevant information like numbers of flights in every airport in a European country to find the busiest airport. The depature, arrival and total number of flights in a country per month to find the busiest time. We aim to enable fans to take informed decisions on which airport they can find most airplanes to visit.

## Section 2: Description of the data

In this project, we are using the the data collected from [Eurocontrol](https://ansperformance.eu/data/), including the data of flights information in Europe from January 1st, 2016 to May 5th, 2022. The dataset contains 688099 registers including daily number of departure flights, arrival flights and total number of flights for each airport in Europe.

The data set is public and can be found in [tidytuesday](https://github.com/rfordatascience/tidytuesday/tree/master/data/2022/2022-07-12). Follow this link to access to the source dataset [flights.csv](https://github.com/rfordatascience/tidytuesday/blob/master/data/2022/2022-07-12/flights.csv).

The aim of our dashboard is to find the busiest airport at the busiest month, and thus we have only utilized the following columns:

`Year` Year of the flight \
`Month` Month of the flight \
`Airport` Airport name \
`Counrty` Country that the airport belongs to \
`Departure` Number of departure flights in the airport \
`Arrival` Number of arrival flights in the airport \
`Total` Number of total flights(Departure+Arrival) in the airport


## Section 3: Research questions and usage scenarios

Our project answers the broad research question of: “What is the busiest airport in a European country in a certain year?”. Below we have provided a usage scenario of our product by a member of our target audience:

Tina is a flight aviation fans who would like to explore various flights in a Europe airport at a certain time. To save money and time, she only has one chance to visit one airport that will potentially contain most varios flights.
That's where our proposed dashboard comes in.

Using the dashboard's map feature, Tina can easily visualize the departure and arrival and also the total number of flights in the country per month she plans to visit to set a good time, and the total flights per airport also gives her a better idea of which airport should she fly to. The the plot is easy to see the pattern of the flights per month, and the sorting color bar plot makes it easy to distinguish for every airport, so Tina can quickly
identify which time and which airport is the busiest.

Overall, our proposed dashboard provides Tina with the information she needs to plan her trip effectively and be prepared for the nice exploring experience. It's an
invaluable tool for any flights aviation fans who want to make the most out of their adventures while saving time and moneys.