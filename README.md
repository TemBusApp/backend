# Description

This project aims to help people with information about buses that travel between cities.

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