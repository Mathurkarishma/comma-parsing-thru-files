<!-- PROJECT LOGO -->
<p align="center">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">List Unique IDs Separated by Commas in Multiple Files</h3>

  <p align="center">
    Using a loop function to read in similarly named files and listing out unique ID's in each that have been separated by commas on a single line.
    <br />
    <a href="https://github.com/Mathurkarishma/comma-parsing-thru-files"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Mathurkarishma/comma-parsing-thru-files/issues">Report Bug</a>
    ·
    <a href="https://github.com/Mathurkarishma/comma-parsing-thru-files/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
      <ul>
        <li><a href="#altering-code">Altering Code</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

We will be utilizing multiple datasets that contain ID information on each line separated by commas.  The number of IDs per line varies.  Each dataset is a CSV file for a different code and different year. The code written will parse through each of these files by identifying the codes and years in a list then separating the IDs by commas and converting this into a columned list format in a CSV output that also contains the code and year from each file.

### Built With

* [Python](https://www.python.org/)
* [Spyder](https://www.spyder-ide.org/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, download the code CSV files (`code100022.csv`, `code100122.csv`, etc.) and the `comma_parser.py` Python file. Then run the code in an IDE software, such as Spyder.  Save them in the same folder.

<!-- USAGE EXAMPLES -->
## Usage

The code guides you through the following:

1. Create a list each of the codes and years in the multiple CSV file names
2. Ensure that the number of values in each list match so the loop can work correctly
3. Loop through each code and year file combination 
4. Split the IDs by commas and add into a list
5. Convert list into an ID column within a dataframe
6. Add columns for the code and year from the file name
7. Export to a CSV file

## Altering Code

This code can be transformed to parse through any character aside from a comma, by replacing the ',' with the new character in line 12.

The code list and code year lists can be renamed to what the file names are named as, with as many values within, and the user can add multiple lists but ensure that variable and list parameter is added into the loop in line 10.

<!-- CONTACT -->
## Contact

Karishma Mathur - karishma324@gmail.com

Project Link: [https://github.com/Mathurkarishma/comma-parsing-thru-files](https://github.com/Mathurkarishma/comma-parsing-thru-files)
