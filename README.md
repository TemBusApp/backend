<!-- <p align="center"><img src="#" alt="TemBusApp"></p> -->
<img src="https://img.shields.io/github/languages/code-size/TemBusApp/backend?label=Repo%20size" height="20">
<img src="https://img.shields.io/github/license/TemBusApp/backend?style=flat-square" height="20">

# Description

This project aims to help people with information about buses that travel between cities.


# 🤞 Motivation

The idea of the application is to help people around the world who want to travel from one city to another using paid public transport. The idea came about because whenever I needed to travel to cities near the city where I live, I needed to ask my friends if there is any public transport available, what time it is and where it leaves from. This app should serve to help people who had the same difficulties I had.


# 🖌️ Design

The link to design in [Figma](https://www.figma.com/file/5juPDMWCJQ2tAZws0EQDJo/TemBus?node-id=0%3A1)


# 🔨 Stack

* API - Backend application in **[Django Rest Framework](https://www.django-rest-framework.org/)**
* APP - App mobile in **[React Native](https://reactnative.dev/)**
* Web - Webpage in **[ReactJS](https://pt-br.reactjs.org/)** 

# 🏁 Get Start

Go to api folder

```
cd api
```

Create docker-compose.override.yml for configure database credenteials(optional)
 
```
version: '3.5'
services: 
    postgres:
        environment: 
            - POSTGRES_PASSWORD=postgres
            - POSTGRES_USER=postgres
            - POSTGRES_DB=tembus
```

Now create .env file and configure data base 

```
cd src 
cp .env.example .env
```

Start the containers

```
docker-compose up -d
```

and enjoy 