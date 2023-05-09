# Data_Engineering_coding_challenge

<a name="readme-top"></a>

<!-- PROJECT LOGO -->

<br />
<div align="center">
  <a href="https://github.com/rwurdig/Data_Engineering_coding_challenge">
    <img src="img/Globant_logo.png" alt="Globant_logo" width="224" height="66">
  </a>

  <h3 align="center">Globant Project</h3>
  
  <p align="center">
    This project of PoC will demonstrate how to store CSV files to Storage Account from Azure.
    <br />
    <a href="https://github.com/rwurdig/Globant_project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/rwurdig/Globant_project">View Demo</a>
    ·
    <a href="https://github.com/rwurdig/Globant_project/issues">Report Bug</a>
    ·
    <a href="https://github.com/rwurdig/Globant_project/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-author">About The Author</a>
      <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
    </li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#documentation">Documentation</a></li>
    <li><a href="#enviroment-info">Enviroment Info</a></li>
    <li><a href="#architecture-design">Architecture Design</a></li>
    <li><a href="#important-notes">Important Notes</a></li>
  </ol>
</details>

<!-- ABOUT THE AUTHOR -->

## About The Author

👤 ** Rodrigo Wurdig **

- Linkedin: [@rodrigo-soares-wurdig](https://www.linkedin.com/in/rodrigo-soares-wurdig)
- Github: [@rwurdig](https://github.com/rwurdig)

<!-- ABOUT THE PROJECT -->

## About The Project

This project of PoC will demonstrate how to manage CSV files to create historical copies of information and daily transactions for a database migration involving three different tables (departments, jobs, employees). The solution includes:

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* Azure Cloud
* Python
* Databricks

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See [License](./Weavebio_project/LICENCE.txt) for more information.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

👤 Rwurdig:  [E-mail](rwurdig@gmail.com)

   Project Link: [https://github.com/rwurdig/Data_Engineering_coding_challenge](https://github.com/rwurdig/Data_Engineering_coding_challenge)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DOCUMENTATION -->

## Documentation 

# Documentation of the Data Engineering Coding Challenge

> *tl;dr*: The challenge is to create a DB migration with 3 different tables (departments, jobs, employees), and create a local REST API that must:
1. Receive historical data from CSV files
2. Upload these files to the new DB
3. Be able to insert batch transactions (1 up to 1000 rows) with one request.

## Enviroment Info

The solution will be deployed in the Azure Cloud environment, and there are some important considerations to keep in mind:

The CSV files will be stored in an Azure Storage Account, which offers low costs.

For this proof-of-concept (PoC), the chosen database will be Azure SQL Database, which is also cost-effective with a basic plan priced at $4.99 USD per month.

The required features for the solution will be implemented using Azure Functions as a REST API, providing low costs and serverless capabilities.

The primary programming language used for code development will be Python.

## Architecture Design

In this PoC, we propose a modern architecture that is both flexible and scalable for future growth. The architecture will involve several steps to ultimately structure and migrate the information. 
There are a few key aspects to consider:

![Diagrama ArquitecturaGlobantChallenge drawio]([https://user-images.githubusercontent.com/81250098/230745098-3cd96d3a-abe7-4c7e-8ef5-4d3df1d5b7f2.png](https://github.com/rwurdig/Data_Engineering_coding_challenge/blob/main/img/Azure_POC.drawio.png))

After loading data into the Storage Account during the ingestion step, development work will commence. Although visualization is not part of this Proof of Concept (PoC), the data will be prepared for easy consumption in various report design tools like Power BI, Tableau Server, and more.

- For the present challenge, the API will serve data directly from the database, which is not the recommended approach as it goes against the best practice for data warehouse systems. Instead, a processed data warehouse with a GOLD zone should be established to serve API data.

- To ensure data organization, we will implement data lake zoning with Bronze, Silver, and Gold levels.

## Important Notes

- In this scenario, Development, QA, and Production will not be separated into distinct environments. Instead, all aspects will be managed within a single production environment. While best practices recommend having three separate environments and configurations for CI/CD, this approach will not be implemented in the PoC due to constraints on time and cost.

- Add additional notes..
