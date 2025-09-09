# 개념과 예시

## SQL 기본

- SELECT, WHERE, ORDER BY, GROUP BY, HAVING
- JOIN: INNER/LEFT/RIGHT/FULL, ON vs USING
- 집계: COUNT/SUM/AVG/MIN/MAX, GROUPING 주의점

Hook: "HAVING 없이 GROUP BY만으로 그룹 필터링이 가능할까?"

### SELECT 절 구조 요약

- SELECT: 반환할 컬럼/표현식 선택 (별칭 AS)
- FROM: 기본 테이블/서브쿼리/CTE 지정
- WHERE: 로우 필터 (집계 이전 단계)
- GROUP BY: 그룹 단위로 로우를 묶음
- HAVING: 그룹 필터 (집계 이후 단계)
- ORDER BY: 정렬
- LIMIT/OFFSET: 페이징

예시:

```sql
SELECT d.name AS dept, COUNT(*) AS cnt
FROM emp e JOIN dept d ON e.dept_id = d.dept_id
WHERE e.salary >= 5000
GROUP BY d.name
HAVING COUNT(*) >= 1
ORDER BY cnt DESC, dept ASC
LIMIT 10;
```

### JOIN 요약과 예시

- INNER JOIN: 양쪽 모두 매칭되는 로우만
- LEFT JOIN: 왼쪽은 모두 유지, 오른쪽 미매칭은 NULL

예시 비교:

```sql
-- INNER JOIN: Sales에 직원이 없으면 부서가 표시되지 않음
SELECT d.name, e.name
FROM dept d INNER JOIN emp e ON d.dept_id=e.dept_id;

-- LEFT JOIN: 직원이 없어도 부서는 유지되며 e.*는 NULL
SELECT d.name, e.name
FROM dept d LEFT JOIN emp e ON d.dept_id=e.dept_id;
```

### 집계와 GROUPING 주의점

- SELECT에 집계가 아닌 컬럼이 있다면 반드시 GROUP BY에 포함
- WHERE는 집계 전, HAVING은 집계 후
- COUNT(\*)는 로우 수, COUNT(col)은 NULL 제외

함정 예시:

```sql
-- 오류: name은 GROUP BY에 없고 집계도 아님
SELECT d.name, e.name, AVG(e.salary)
FROM emp e JOIN dept d ON e.dept_id=d.dept_id
GROUP BY d.name;
```

퀵체크(정답: 4번 문서)

- Q1. WHERE와 HAVING의 적용 시점 차이는?
- Q2. LEFT JOIN에서 NULL이 생기는 위치는?

## 정규화

- 이상현상(삽입/갱신/삭제)과 함수적 종속성
- 1NF/2NF/3NF/BCNF 정의와 예시
- 후보키/기본키/대체키

Hook: "전화번호를 콤마로 묶어 한 컬럼에 저장하면 뭐가 문제일까?"

### 핵심 용어

- 함수적 종속성 X→Y: X 값이 같으면 Y 값이 반드시 같다 (Y가 X에 의해 결정)
- 후보키: 모든 로우를 유일하게 식별하는 최소 속성 집합
- 기본키: 후보키 중 선택된 키, 대체키: 그 외 후보키

### 1NF, 2NF, 3NF, BCNF

- 1NF: 원자성. 반복/다중 값 컬럼 금지 (예: phone1, phone2 → 별도 행)
- 2NF: 부분 함수 종속 제거 (복합키의 부분집합이 결정자가 되지 않게)
- 3NF: 이행적 종속 제거 (키가 아닌 속성이 다른 키가 아닌 속성에 의존 금지)
- BCNF: 모든 결정자가 후보키 (3NF보다 강함)

### 예시로 보는 정규화

비정규 테이블 예:

```
Order(order_id, customer, customer_city, product, price, city_tax)
```

문제:

- customer_city는 customer에 의해 결정 (이행적 종속)
- city_tax는 customer_city에 의해 결정 (이행적 종속)

3NF 분해:

```
Customer(customer, customer_city)
City(city, city_tax)
Order(order_id, customer, product, price)
```

장점: 갱신/삽입/삭제 이상 제거, 데이터 일관성 향상
주의: 과도한 분해는 조인 비용 증가 → 조회 패턴 고려(정규화+반정규화 균형)

퀵체크(정답: 4번 문서)

- Q1. 2NF에서 제거하려는 종속성은 무엇인가?
- Q2. BCNF에서 모든 "무엇"이 후보키여야 하는가?
