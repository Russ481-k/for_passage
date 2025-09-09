-- Q1: 부서별 평균 급여 (정답: Dev 6250, HR 4500, Sales 5100)
SELECT d.name AS dept, ROUND(AVG(e.salary), 0) AS avg_salary
FROM emp e
    JOIN dept d ON e.dept_id = d.dept_id
GROUP BY
    d.name
ORDER BY d.name;
-- Q2: Sales 소속 직원 수
SELECT d.name AS dept, COUNT(*) AS cnt
FROM emp e
    JOIN dept d ON e.dept_id = d.dept_id
WHERE
    d.name = 'Sales';
-- Q3: salary 상위 2명
SELECT name, salary FROM emp ORDER BY salary DESC, name ASC LIMIT 2;
-- Q4: Dev 부서 직원의 평균보다 급여 높은 직원
SELECT name, salary
FROM emp
WHERE
    salary > (
        SELECT AVG(e.salary)
        FROM emp e
            JOIN dept d ON e.dept_id = d.dept_id
        WHERE
            d.name = 'Dev'
    )
ORDER BY salary DESC, name ASC;