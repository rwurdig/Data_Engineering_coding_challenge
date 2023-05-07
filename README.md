# Data_Engineering_coding_challenge

<a name="readme-top"></a>

<!-- PROJECT LOGO -->

<br />
<div align="center">
  <a href="https://github.com/rwurdig/Data_Engineering_coding_challenge\img\Globant_logo.png">
    <img src="img/Globant_logo.png" alt="Globant_logo" width="80" height="80">
  </a>

<h3 align="center">Globant Project</h3>

  <p align="center">
    This project import data from CSV files stored in Azure Blob Storage to an Azure Database for MySQL instance
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
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation-and-prerequisites">Installation and Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#documentation">Documentation</a></li>
  </ol>
</details>

<!-- ABOUT THE AUTHOR -->

## About The Author

👤 ** Rodrigo Wurdig **

- Linkedin: [@rodrigo-soares-wurdig](https://www.linkedin.com/in/rodrigo-soares-wurdig)
- Github: [@rwurdig](https://github.com/rwurdig)

<!-- ABOUT THE PROJECT -->

## About The Project

This project import data from CSV files stored in Azure Blob Storage to an Azure Database for MySQL instance.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* Docker and Docker-Compose
* Python (docker container)
* Airflow (docker container)
* Bash scripting

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This is how you setting up your project locally.
```
- To get a local copy up and running follow these simple steps bellow.
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- INSTALLATION AND PREREQUISITES -->

### Installation and Prerequisites

#### To run this code, you will need to have the following softwares and libraries installed:

* Airflow 2.5.2
* Neo4j  5.6.0
* pendulum 2.1.2
* pip 23.0.1
* postgres:14.0
* Python 3.x
* py2neo 2021.2.3
* xmltodict 0.13.0

#### After installing Python and pip, run the following command to install the necessary Python packages:

### 1. Install  packages:
```bash
  pip install neo4j xml airflow etc
```

### 2. Clone the repository
```bash
   git clone https://github.com/rwurdig/Weavebio_project.git
```

```bash
   cd Weavebio_project
```

### 3. Run the build.sh file with admin privileges.

```bash
  chmod +x build.sh
  ./build.sh
```

### 4. The project will start and it will build all the images on the docker compose and run it.

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

   Project Link: [https://github.com/rwurdig/Weavebio_project](https://github.com/rwurdig/Weavebio_project)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DOCUMENTATION -->

## Documentation 

# Documentation of the Data Engineering Coding Challenge

> *tl;dr*: The challenge is to create a DB migration with 3 different tables (departments, jobs, employees), and create a local REST API that must:
1. Receive historical data from CSV files
2. Upload these files to the new DB
3. Be able to insert batch transactions (1 up to 1000 rows) with one request.
> XXX
## Task
xxxxxxxx

## Requirements & Tools
- Use Apache Airflow or a similar workflow management tool to orchestrate the pipeline
- The pipeline should run on a local machine
- Use open-source tools as much as possible

## Source Data
Use the CSVs files provided in the `data` directory.

xxxxxxxx

## Docker
Please run a Neo4j database locally. You can download Neo4j from https://neo4j.com/download-center/ or run it in Docker:

```
docker run \
  --publish=7474:7474 --publish=7687:7687 \
  --volume=$HOME/neo4j/data:/data \
  neo4j:latest
```

Getting Started with Neo4j: https://neo4j.com/docs/getting-started/current/


## Data Model
The data model should be a graph data model. The graph should contain nodes for proteins, genes, organisms, references, and more. The graph should contain edges for the relationships between these nodes. The relationships should be based on the XML schema. For example, the `protein` element contains a `recommendedName` element. The `recommendedName` element contains a `fullName` element. The `fullName` element contains the full name of the protein. The graph should contain an edge between the `protein` node and the `fullName` node.

Here is an example for the target data model:

![Example Data Model](./img/example_data_model.png)


## Assessed Criteria

> :warning: The solution will not be assessed based on correctness of the data model with respect to biological entities. This requires domain knowledge that we do not expect you to have. 
We will assess the solution based on the following criteria:

- The solution captures most of the data from the XML
- The solution makes use of general purpose open-source tools
- The solution can be scaled to handle larger datasets

## Example Code
In the `example_code` directory, you will find some example Python code for loading data to Neo4j.

## Submission
**Please commit your solution to a new repository on GitHub**.

Feel free to use this repository as a starting point or to start from scratch. Include a `README.md` file that describes how to run the solution. 
Please also include a description how to set up and reproduce the environment required to run the solution.

Finally, email join@weave.bio with 1) the link to your solution repo and 2) your resume
