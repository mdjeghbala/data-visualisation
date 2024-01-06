# Data visualisation project

The aim of this project is to create a dashboard for visualizing radars in France and overseas territories, using maps, histograms and diagrams.

# User Guide

## Installation

Clone the repository 

```bash
git clone https://github.com/mdjeghbala/data-visualisation.git
```
## Change directory

```bash
cd data-visualisation
```
## Create environment

Execute this commande to create an environment for all the packages to don't loose your packages versions already installed in your computer

```bash
python -m venv env
```
## Activate environment

Execute this commande to activate the environment 

```bash
env/Scripts/activate
```
You need to always activate the environment which contains all python depedencies project

If you want to deactivate the environment you can execute this command but after you can't execute the project because the packages will be missing 

```bash
deactivate
``` 
## Requirements

Install the requirements

```bash
python -m pip install -r requirements.txt
```
Be patient, as it may take some time

## Launch

Execute this command

```bash
python main.py
```
## Run the dashboard

In the console you can access to the dashboard if you `CTRL + Click`  in the link 
or you can click in this server link http://127.0.0.1:8050/
You can stop the server with `CTRL + C` in the console

# Developer Guide

This guide helps developers understand the project, 
including its **architecture**, **dependencies**, **coding standards**, **workflows** and **file organization**.

## Architecture

**Code Structure**: 

In our code, each functionality is put in a separeted file containing a class and functions. 

These classes have a method for generating a diagram or a map.

**Interactions and Data Flow**:

To generate the maps and the diagrams, we use the csv file "***radars.csv***" and for the histogram, we use the csv file "***opendata-vitesse.csv***" 

The maps and the diagrams are then created in "***main.py***" and integrated to the user interface (dashboard)

## Dependencies

***Dash***: For creating interactive web applications.

***Pathlib***: Used for handling file paths.

***Pandas***: For data manipulation (reading CSV files).

***Folium***: For creating interactive maps

***Plotly.express***: For creating data visualization like histogram

## Coding Standards

***PEP 8***: Follow the Python's PEP 8 style guide for consistent code formatting, naming conventions, and readability. 

***Variable Naming***: Including in Python's PEP 8 style guide : Use of snake_case for variables, functions, and methods.

***Comments and Docstrings***: Use of comments for code explanations and docstrings for function/class documentation.

## Workflows

1. Application initialization
2. Radar Map Generation
3. Visualization Generation
4. Building the User Interface 
5. Integration of Visualizations into the Interface
6. Dynamic Update Handling
7. Launching the Application

## File Organisation

### Diagrams:

***histogramme_exces_de_vitesse.py***: Contains Histogramme class for generating histogram based on speeding violations.

***diagram_date_installation.py***: Contains DiagramDate class for generating radar installation date diagrams.

***diagram_max_speed.py***: Contains DiagramSpeed class for generating diagrams of maximum recorded speeds.

### Maps:

***all_radars_map.py***: Contains AllRadarsMap class for generating a map displaying all radars in France.

***radar_map_by_department.py***: Contains RadarMapByDepartment class for generating maps showing radar count per department.

### Integration in main.py:

Importing functionalities (diagrams, histogram, maps) into the Dash dashboard.

Creation of class instances to generate visual elements within the dashboard.