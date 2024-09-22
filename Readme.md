# Data Oriented Programming

## Description
Experimentation with Data-Oriented Programming. Data-Oriented Programming (DOP) focuses on organizing data in a way that optimizes memory access patterns, improving cache efficiency and performance. It emphasizes processing large, homogeneous datasets in bulk by separating data storage from the logic that operates on it. Unlike Object-Oriented Programming, which groups behavior with data, DOP prioritizes how data is structured in memory to maximize performance, particularly for high-throughput or parallelizable tasks.

Data-Oriented Programming (DOP) organizes data in a way that optmizies memory access patterns, improving cache efficiency and performance. It allows processing datasets in bulk by separating data storage from the logic that operates on it. Unlike Object-Oriented Programming (OOP), DOP prirotizies how data is structured in memory versus grouping behavior with data (Struct of Arrays vs Array of Structs). DOP outperforms OOP in specific scenarios:

1) Batch Processing of Large Data Sets: Processing large arrays of data, such as totaling employee salaries in one go.

2) Iterating over fields separately: The fields are available in a contiguous array, improving cache hits.

3) Sorting and searching: Sorting salaries or performing range queries across a large dataset can be faster when the data is stored in a contiguous array.

4) Parallel processing: Different fields can be worked on separately without having to depend on objects.

5) Memory access patterns: Only relevant data (i.e, names, salaries) is loaded into memory instead of loading entire objects, which reduces amount of memory transferred between CPU and RAM.

## Motivation
Practicing Data-Oriented Programming allows a developer to think of solving problems differently. While Object-Oriented Programming is more intuitive for humans, Data-Oriented Programming aligns more with how the hardware works.

## Design
The EmployeeData class fully encapsulates employee-related data management. The Controller class manages operations on that data. Separating data from control logic allows for single responsibility, flexibility, and extensibility. For example, new fields or methods can be added to EmployeeData without affecting other parts of the program. Likewise, you can easily add new retrieval functions or updating existing ones without affecting the EmployeeData class.

## Usage

### Quick Start

### Working on the Application


&emsp;*API gateway/security.* \
&emsp;*Goroutine/multithreading.* \
&emsp;*Database interactions.* \
&emsp;*Data serialization/deserialization.* \
&emsp;*Full error handling.* \
&emsp;*Unit testing.* \
&emsp;*Pagination for "all" retrieval.* \
&emsp;*Redis caching.* \
&emsp;*Containerization orchestration.* \
&emsp;*Full Rest API CRUD functionalities.*

[^1]: The .env file is not encrypted and all secrets are visible for ease of use. If you intend to use this for production, please encrypt the .env file and change the variable values!

## Motivation
Go is widely used for backend programming. It is essential to know how to create a backend API server with basic functionalities. I wanted to take it further by making the project as robust and production ready as possible.

## Quick Start

You don't need Go installed on your computer, but you must have Docker up and running.

Clone the repo:

```
git clone https://github.com/capgainschristian/go_api_ds.git
```

Start the application:

```
docker compose up
```

## Usage

### Adding customers
After you have the application up and running, you will notice that you have no customers to view. I have created a function to generate 100 random customers. To run it, open another terminal and do the following:

```
docker exec -it go_api_ds-web-1 bash
```
Once you are inside the container, run:

```
go run fake_data_generation/fake_data.go
```

### View customers
To verify that the customers have been added successfully, you can run:

```
curl http://localhost:3000/listcustomers
```

Or open a browser and go to:

```
http://localhost:3000/listcustomers
```

Since pagination is used to make data retrieval more efficient and user friendly, you will only see 10 customers listed per page by default. You can change this by appending:

```
listcustomers?limit=100&offset=0
```

Example:

```
http://localhost:3000/listcustomers?limit=100&offset=0
```

### Run unit tests
If you want to run the unit tests, run the following inside the *go_api_ds-web-1* container:

```
cd handlers

go test -v
```
### Adding, deleting, and updating a user manually

Make sure that the application is running. Open another terminal and follow the instructions below. If a user with the same information is already created, the examples will not work. In that situation, change the customer information.

**NOTE:** You must be authenticated to add, update, or delete customers. Once you signup for an account, you will receive a token for authentication. The token is added to your cookie automatically. Therefore, it is easier to run these APIs with Postman or VSCode Thunder Client. Otherwise, you will need to include your token in all of your curl requests.

To signup for an account:

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"email":"alexander.graham@grahamsummitllc.com,","password":"thisisaverystrongpassword"}' \
  http://localhost:3000/signup
```

To login/auithenticate with your new account:

```
curl --header "Content-Type: application/json" \
  --verbose \
  --request POST \
  --data '{"email":"alexander.graham@grahamsummitllc.com,","password":"thisisaverystrongpassword"}' \
  http://localhost:3000/login
```

To add a customer:

```
curl --header "Content-Type: application/json" \
  --request POST \
  -b "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjI0NTI3OTMsInN1YiI6ImFsZXhhbmRlci5ncmFoYW1AZ3JhaGFtc3VtbWl0bGxjLmNvbSwifQ.tO7v42pkJHqeX81g4yG2apuRGv1YGtGpN9Wrmre4NBg" \
  --data '{"name":"Christian Graham,","email":"christian.graham@grahamsummitllc.com","address":"777 Summit LLC Drive","number":2222}' \
  http://localhost:3000/addcustomer
```

To update a customer:

```
curl -X PUT http://localhost:3000/updatecustomer \
      -b "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjI0NTI3OTMsInN1YiI6ImFsZXhhbmRlci5ncmFoYW1AZ3JhaGFtc3VtbWl0bGxjLmNvbSwifQ.tO7v42pkJHqeX81g4yG2apuRGv1YGtGpN9Wrmre4NBg" \
     -H "Content-Type: application/json" \
     -d '{
           "email": "christian.graham@grahamsummitllc.com",
           "name": "Christian Graham",
           "address": "888 Summit LLC Drive",
		   "number": 1111
         }'
```

To delete a customer:

```
curl --header "Content-Type: application/json" \
  --request DELETE \
  -b "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjI0NTI3OTMsInN1YiI6ImFsZXhhbmRlci5ncmFoYW1AZ3JhaGFtc3VtbWl0bGxjLmNvbSwifQ.tO7v42pkJHqeX81g4yG2apuRGv1YGtGpN9Wrmre4NBg" \
  --data '{"email":"christian.graham@grahamsummitllc.com"}' \
  http://localhost:3000/deletecustomer
```
### PostgreSQL

If you ever need to get into the PostgreSQL container, run the following:

```
docker exec -it go_api_ds-db-1 psql -U capgainschristian -d customers
```
Once you're inside, you can run queries normally like:

```
SELECT * FROM customers;
```

### Working on the application

As stated above, you don't need Go installed but you do need Docker to run the application. The same can be said when working on the project. If you want to further develop, or edit, any of Go code, simply run:

```
docker compose run --service-ports web bash
```
This will take you into a container with Go already installed. After making your changes, you can run the app from the container:

```
go run cmd/main.go -b 0.0.0.0
```
