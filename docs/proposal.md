# Proposal

## Section 1: Motivation and Purpose

### Our role

We are a data scientist consultancy firm.

### Target Audience

Our target audience is flight aviation fans who enjoy visiting different airports and checking flights in Europe.

### Purpose


Flight aviation fans who enjoy visiting the different airports and checking the flights dream about having unforgettable experiences in an airport that is busy and contains various flights at a certain time! Since travelling is expensive so exploring the busiest airports at their busiest time will be time efficient and money-saving! Our proposed dashboard would be a reliable tool that can help fans who love airports and flights to embark on memorable adventures in a European airport by providing them with the information. The proposed dashboard is a one-stop shop for finding relevant information like the number of flights in every airport in a European country to find the busiest airport. The departure, arrival and the total number of flights in a country per month to find the busiest time. We aim to enable fans to take informed decisions on which airport they can find the most airplanes to visit.

## Section 2: Description of the data

### Data Source

We are using the data collected from Eurocontrol, including the data of flights information in Europe from January 1st, 2016, to May 5th, 2022. The dataset contains 688099 records, including daily numbers of departure flights, arrival flights, and the total number of flights for each airport in Europe.

### Data Availability

The dataset is public and can be found on tidytuesday. The source dataset flights.csv can be accessed at [tidytuesday](https://github.com/rfordatascience/tidytuesday/tree/master/data/2022/2022-07-12). Follow this link to access to the source dataset [flights.csv](https://github.com/rfordatascience/tidytuesday/blob/master/data/2022/2022-07-12/flights.csv).

### Data Selection

The aim of our dashboard is to find the busiest airport at the busiest month, and thus we have only utilized the following columns:

`Year` Year of the flight \
`Month` Month of the flight \
`Airport` Airport name \
`Counrty` Country that the airport belongs to \
`Departure` Number of departure flights in the airport \
`Arrival` Number of arrival flights in the airport \
`Total` Number of total flights(Departure+Arrival) in the airport

## Section 3: Research questions and usage scenarios

### Research questions

Below are some of the questions that will be answered through interaction with our dashboard:
- Which airport has the most flights in the United Kingdom in 2019?
- What is the number of flights in Nantes-Atlantique airport in 2018?
- Which month does Germany have the most flights in 2021?
- Did the pandemic affect the number of flights in Turkey airports in 2020 compared to 2019?

### Usage scenarios

Our dashboard answers the research question, "What is the busiest airport in a European country in a certain year?" Below is an example usage scenario:

Tina is a flight aviation fan who wants to explore various flights in a European airport at a certain time. She lives in Croatia, which only has two airports, and wants to travel to the United Kingdom or France to explore flights. To save time and money, she only has one chance to visit an airport that will potentially contain the most various flights.

Using our dashboard's map feature, Tina can easily visualize the departure and arrival and the total number of flights in the United Kingdom and France per month she plans to visit. She can then set a good time, and the total flights per airport will give her a better idea of which airport she should fly to. The plot is easy to see the pattern of flights per month, and the sorting color bar plot makes it easy to distinguish for every airport. Tina can quickly identify which time and which airport is the busiest.

Overall, our proposed dashboard provides Tina with the information she needs to plan her trip effectively and be prepared for an enjoyable exploring experience. It's an invaluable tool for any flight aviation fan who wants to make the most out of their adventures while saving time and money.