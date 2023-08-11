# TestShop

### Setup

The first thing to do is to clone the repository

```shell
$ git clone https://github.com/mikiedev07/TestShop.git
$ cd gis-kg
```

Run the project via Docker (docker compose). Go to directory gis_kg_dj with Dockerfile and docker-compose.yml files.

```shell
docker compose up -d
```

Type in your browser 127.0.0.1:8000 and you should see Swagger documentation.

### API

The API to application is described below

#### User Register

```shell
http://127.0.0.1:8000/api/register/
```
If success, client should receive a message "User registered successfully."

#### User Login

```shell
http://127.0.0.1:8000/api/login/
```
The client receives a pair of JWT tokens.

#### Get the list of Products

To get the list of products client should provide an access token as Bearer token type.
```shell
http://127.0.0.1:8000/api/products/
```

###  Export product data

To export the list of products in XLSX format, client should provide an access token as Bearer token type.

```shell
http://127.0.0.1:8000/api/products/export/
```

As a result, XLSX format data will be gathered.
Client also can save this data as Excel file.
