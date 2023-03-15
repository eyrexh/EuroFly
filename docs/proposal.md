# Proposal

## Section 1: Motivation and Purpose

### Our role

We are a data scientist consultancy firm.

### Target Audience

Our target audience is flight aviation fans who enjoy visiting different airports and checking flights in Europe.

### Purpose


Flight aviation fans who enjoy visiting the different airports and checking the flights dream about having unforgettable experiences in an airport that is busy and contains various flights at a certain time! Since traveling is expensive so exploring the busiest airports at their busiest time will be time efficient and money-saving. Our proposed dashboard would be a reliable tool that can help fans who love airports and flights to embark on memorable adventures in a European airport by providing them with the information. The proposed dashboard is a one-stop shop for finding relevant information like the number of flights in every airport in a European country to find the busiest airport. The departure, arrival and the total number of flights in a country per month to find the busiest time. We aim to enable fans to take informed decisions on which airport they can find the most airplanes to visit.

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

Tina, a flight aviation enthusiast, is looking to explore various flights at a European airport during a specific time. Living in Croatia, which has only two airports, she plans to travel to either the United Kingdom or France to fulfill her desire. Although the Paris Air show is a must-go event, Tina is a Boeing fan and believes the United Kingdom may have more Boeing flights from the US. With only one chance to visit an airport that will potentially contain the most diverse flights, Tina is keen to save both time and money.

Our dashboard's map feature is the perfect tool for Tina. She can easily visualize the departure and arrival, as well as the total number of flights in the United Kingdom and France for each month she plans to visit. By analyzing this information, Tina can decide on the best time to travel and which airport to fly to based on the total number of flights per airport. The plot displays the pattern of flights per month, and the sorting color bar plot provides an easy way to differentiate between each airport. Tina can quickly identify the busiest time and airport for her desired flight experience.

After analyzing the data, Tina decides to visit Paris-Charles-de-Gaulle, which had 10,000 more flights than the busiest airport in the UK in 2019. Additionally, the Air Show is scheduled for June, the airport's busiest month. Tina is thrilled with the results she obtained from our dashboard.
