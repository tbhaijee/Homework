-- DROP Tables for Pewlett Hackardd employee database
DROP TABLE salaries;
DROP TABLE dept_manager;
DROP TABLE dept_emp;
DROP TABLE departments;
DROP TABLE titles;
DROP TABLE employees;

--Create employee table
CREATE TABLE employees(
    emp_no int   NOT NULL,
    birth_date date   NOT NULL,
    first_name VARCHAR(30)   NOT NULL,
    last_name VARCHAR(30)   NOT NULL,
    gender VARCHAR(2)   NOT NULL,
   	hire_date date   NOT NULL,
    CONSTRAINT pk_employee PRIMARY KEY (
       emp_no
     )
);

--create titles table
CREATE TABLE titles (
    emp_no int   NOT NULL,
    title VARCHAR(30)  NOT NULL,
    from_date date   NOT NULL,
    to_date date   NOT NULL
);

--create department table
CREATE TABLE departments (
    dept_no VARCHAR(10)   NOT NULL,
    dept_name VARCHAR(30)   NOT NULL,
    CONSTRAINT pk_departments PRIMARY KEY (
        dept_no
     )
);

--create employee department table

CREATE TABLE dept_emp (
    emp_no int   NOT NULL,
    dept_no VARCHAR(10)   NOT NULL,
    from_date date   NOT NULL,
    to_date date   NOT NULL
);

--create department manager table
CREATE TABLE dept_manager (
    dept_no VARCHAR(10)  NOT NULL,
	emp_no int   NOT NULL,
    from_date date   NOT NULL,
    to_date date   NOT NULL
);

--create salary table
CREATE TABLE salaries (
    emp_no int   NOT NULL,
    salary int  NOT NULL,
    from_date date   NOT NULL,
    to_date date   NOT NULL
);

--alter title table for foreign key to employee table
ALTER TABLE titles ADD CONSTRAINT fk_titles_emp_no FOREIGN KEY(emp_no)
REFERENCES employees (emp_no);

--alter employee department table for foreign key to employee table
ALTER TABLE dept_emp ADD CONSTRAINT fk_dept_emp_emp_no FOREIGN KEY(emp_no)
REFERENCES employees (emp_no);

--alter employee department table for foreign key to department table
ALTER TABLE dept_emp ADD CONSTRAINT fk_dept_emp_dept_no FOREIGN KEY(dept_no)
REFERENCES departments (dept_no);

--alter manager department table for foreign key to employee table
ALTER TABLE dept_manager ADD CONSTRAINT fk_dept_manager_emp_no FOREIGN KEY(emp_no)
REFERENCES employees (emp_no);

--alter manager department table for foreign key to department table
ALTER TABLE dept_manager ADD CONSTRAINT fk_dept_manager_dept_no FOREIGN KEY(dept_no)
REFERENCES departments (dept_no);

--alter salaries table for foreign key to employee table
ALTER TABLE salaries ADD CONSTRAINT fk_salaries_emp_no FOREIGN KEY(emp_no)
REFERENCES employees (emp_no);

