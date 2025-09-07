PRAGMA foreign_keys=ON;
CREATE TABLE dept(dept_id INTEGER PRIMARY KEY, name TEXT UNIQUE);
CREATE TABLE emp(
  emp_id INTEGER PRIMARY KEY,
  name TEXT, dept_id INTEGER, salary INTEGER,
  FOREIGN KEY(dept_id) REFERENCES dept(dept_id)
);
