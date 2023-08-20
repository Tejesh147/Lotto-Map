# Lotto Winners Map Web App

This project is a web application that visualizes the locations of OLG lottery winners in the province of Ontario, Canada. It allows users to explore the distribution of winning tickets, the prize amounts, and additional information about the winning locations.

## Features

- Interactive map with markers that represent the locations of winning lotto tickets.
- Toggleable Heat Map layer to visualize the density of winning tickets across Ontario
- Markers scale in size and change color hue based on the prize amount won.
- Clickable markers display information about the winning ticket, including store name, prize amount, and more.
- Aggregate information is displayed when multiple winning tickets are sold at the same location.

## Data Sources

The data for this visualization was taken publicly from [OLG's official website](https://about.olg.ca/winners-and-players/ticket-information/where-winning-tickets-were-sold/) which gives information on winning tickets sold in the past 6 months. Currently, this web app shows data on winning tickets sold between February 1, 2023 - August 1, 2023.

The Ontario boundary was taken from [this public dataset](https://public.opendatasoft.com/explore/dataset/georef-canada-province/map/?disjunctive.prov_name_en&dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6Imdlb3JlZi1jYW5hZGEtcHJvdmluY2UiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLnByb3ZfbmFtZV9lbiI6dHJ1ZX19LCJjaGFydHMiOlt7ImFsaWduTW9udGgiOnRydWUsInR5cGUiOiJsaW5lIiwiZnVuYyI6IkNPVU5UIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiI0ZGNTE1QSJ9XSwieEF4aXMiOiJ5ZWFyIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoieWVhciIsInNvcnQiOiIifV0sImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9&location=4,61.83541,-107.8418&basemap=jawg.light). I only included the Ontario boundary on the map as physical OLG tickets are sold solely in stores across the province. However, the dataset includes boundary information for all provinces and territories of Canada.

## Notes

You may notice a few bubbles around the world map in strange places... (a winning ticket sold in NEW ZEALAND!?!?)
To convert the address data into lat/long coordinates, I utilized the [Bing Maps API](https://www.microsoft.com/en-us/maps/choose-your-bing-maps-api) and batch geocoded all of the addresses. The service was pretty accurate and got the corrent location for almost all of the addresses, however there seems to be a few stragglers which you can find on the map if you zoom out. I could manually geocode the incorrect locations but I'll leave them for now. Just know that all the tickets sold *within the Ontario boundary* are actually correct!