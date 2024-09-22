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

The tests module will create fake data for you to verify that the application runs.

If you have Docker installed, just run:

```
docker compose up
```

If you don't, while you're in the root directory, run:

```
python -m tests.test_main
```

### Working on the Application
You can directly edit the Python files and run the Python executable, or you can use Docker if you don't have Python installed:

```
docker compose run app bash
```

Once you're in the Python container, you'll have access to all of the application files and Python executable.