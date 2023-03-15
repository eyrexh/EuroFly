[<img src="https://img.shields.io/badge/License-MIT-yellow.svg"
alt="License:MIT" />](https://opensource.org/licenses/MIT)

# 🛫️ EuroFly 🛬️

Welcome! Thank you for visiting the EuroFly project repository.

If you are a fan of flights or just want to be prepared for your next coming flight to Europe, our app is for you! 

[Link to the EuroFly app](https://eurofly.onrender.com)

To learn more about the app, you can jump to one of the sections below or keep scrolling.

* [Purpose and Motivation](#purpose-and-motivation)
* [Preview and Description](#dashboard-preview-and-description)
* [Data](#data)
* [Installation](#installation)
* [Contributor](#contributor)
* [Contributing](#contributing)
* [Support](#support)
* [Code of Conduct](#code-of-conduct)
* [License](#license)

## Purpose and Motivation

Air travel is an integral part of modern life, connecting people and businesses across the world. Flight aviation fans who enjoy visiting the different airports and checking the flights dream about having unforgettable experiences in an airport that is busy and contains various flights at a certain time! 

Since traveling is expensive so exploring the busiest airports at their busiest time will be time efficient and money-saving! Our proposed dashboard would be a reliable tool that can help fans who love airports and flights to embark on memorable adventures in a European airport by providing them with the information. The proposed dashboard is a one-stop shop for finding relevant information like the number of flights in every airport in a European country to find the busiest airport. The departure, arrival and the total number of flights in a country per month to find the busiest time. We aim to enable fans to take informed decisions on which airport they can find the most airplanes to visit.

Please read my detailed [`proposal.md`](https://github.com/eyrexh/EuroFly/blob/main/docs/proposal.md) to have a more general idea about how this dashboard can provide the solution for a specific scenario.

## Description

Our dashboard `EuroFly` provides users with interactive visualizations of flight data from various countries and airports. Users can select a year and a European country, and view the total number of flights for each airport in the selected country, as well as the monthly number of departures, arrival and total flights in all the airports for a selected country. The app aims to provide insights into global air travel patterns and trends, as well as serve as a tool for travel planning and research.

## Data

In this project, we are using the data collected from [Eurocontrol](https://ansperformance.eu/data/), including the data of flights information in Europe from January 1st, 2016 to May 5th, 2022. The dataset contains 688099 registers including daily number of departure flights, arrival flights and total number of flights for each airport in Europe.

The data set is public and can be found in [tidytuesday](https://github.com/rfordatascience/tidytuesday/tree/master/data/2022/2022-07-12). Follow this link to access to the source dataset [flights.csv](https://github.com/rfordatascience/tidytuesday/blob/master/data/2022/2022-07-12/flights.csv).

## Installation

To install `EuroFly` locally, you can:

1.  Clone this repository to your local directory.

2.  We have created an environment (eurofly.yaml), using which our app can be reproduced locally. To create this environment locally, go to the root of this repository and run:

    ``` bash
    conda env create -f eurofly.yaml
    ```

3.  Activate it by running:

        conda activate eurofly

4.  In the `src/` folder of this repository run the following command:

        python app.py

5.  Copy the address and paste it in your browser to load the dashboard.

## Contributor

The creators of `EuroFly` are students of the MDS Program at the University of British Columbia. This project was created for the DSCI 532 (Data Visualization II) course. 

* [Eyre Hong](https://github.com/eyrexh)

## Contributing

Feedback and suggestions are always welcome! 

Please read [the contributing guidelines] (https://github.com/eyrexh/EuroFly/blob/main/CONTRIBUTING.md)to get started.

## Support

If you run into trouble, please [check the issue
list](https://github.com/eyrexh/EuroFly/issues) to see
if your problem has already been reported or to open new issues.

## Code of conduct

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation. Detailed descriptions
of these points can be found in [`CODE_OF_CONDUCT.md`](https://github.com/eyrexh/EuroFly/blob/main/CODE_OF_CONDUCT.md).

## License
The EuroFly Dashboard is licensed under the terms of the MIT license.
