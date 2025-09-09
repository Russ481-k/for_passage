# 풀이와 해설

정답만 확인하고 넘어가면 금방 잊혀집니다. 왜 그 답이 맞는지, 그리고 다른 선택지는 왜 헷갈렸는지를 짚어보면 실력이 단단해져요. 해설을 읽을 때 “내 말로 다시 설명해보기”를 꼭 해보세요.

- Q1~Q4는 `sql/exercises.sql` 스키마 기준으로 작성.
- Q5~Q10은 개념 서술형 풀이로 작성.

## Q1: 부서별 평균 급여

핵심: JOIN 후 GROUP BY. 집계는 `AVG`, 표시 정렬은 부서명 기준.
정답 결과: Dev 6250, HR 4500, Sales 5100

```sql
SELECT d.name AS dept, ROUND(AVG(e.salary), 0) AS avg_salary
FROM emp e JOIN dept d ON e.dept_id = d.dept_id
GROUP BY d.name
ORDER BY d.name;
```

## Q2: Sales 소속 직원 수

핵심: 조건은 WHERE에서 처리. 집계는 COUNT(\*)

```sql
SELECT d.name AS dept, COUNT(*) AS cnt
FROM emp e JOIN dept d ON e.dept_id = d.dept_id
WHERE d.name = 'Sales';
```

## Q3: 급여 상위 2명

핵심: ORDER BY salary DESC, 동률은 name ASC로 안정적 정렬 후 LIMIT 2

```sql
SELECT name, salary
FROM emp
ORDER BY salary DESC, name ASC
LIMIT 2;
```

## Q4: Dev 평균보다 높은 급여

핵심: 서브쿼리로 Dev의 AVG를 구해 비교.

```sql
SELECT name, salary
FROM emp
WHERE salary > (
  SELECT AVG(e.salary)
  FROM emp e JOIN dept d ON e.dept_id = d.dept_id
  WHERE d.name = 'Dev'
)
ORDER BY salary DESC, name ASC;
```

---

오답키워드 제안: GROUP BY vs HAVING 혼동, JOIN 조건 누락, 서브쿼리 스코프
재복습 일정: 1D/3D/7D 간격으로 동일 문제 재풀이 권장

## Q5: LEFT vs INNER JOIN 차이

설명: INNER JOIN은 양쪽 테이블에서 매칭되는 로우만, LEFT JOIN은 왼쪽 모든 로우 유지.
예시:

```sql
-- 특정 부서가 직원을 아직 채용하지 않은 경우
SELECT d.name, e.name
FROM dept d LEFT JOIN emp e ON d.dept_id=e.dept_id
ORDER BY d.name, e.name;
```

포인트: LEFT에서 e.\*는 NULL 가능. 보고서에서 기준 목록(부서)을 유지할 때 LEFT가 필요.

## Q6: HAVING vs WHERE

설명: WHERE는 그룹핑 이전 로우 필터, HAVING은 그룹핑 이후 그룹 필터.
예시:

```sql
-- 급여 5000 이상 직원들만 대상으로, 부서별 인원수가 1 이상인 그룹만
SELECT d.name, COUNT(*) AS cnt
FROM emp e JOIN dept d ON e.dept_id=d.dept_id
WHERE e.salary >= 5000
GROUP BY d.name
HAVING COUNT(*) >= 1;
```

## Q7: 1NF 위반 정규화

문제 예: `Student(id, name, phones)`에서 `phones`에 다중 값 저장.
해결: 전화번호를 행 분리.

```
Student(id, name)
Phone(id, phone)
```

장점: 원자성 확보, 전화번호 추가/삭제가 간단해짐. 실제로는 검색도 훨씬 쉬워져요. "010-"로 시작하는 번호만 찾기, 이런 작업이 깔끔해집니다.

## Q8: 2NF 위반 분해

문제 예: `Score(student_id, subject_id, subject_name, score)`에서 키가 (student_id, subject_id)이고 `subject_name`이 `subject_id`에 부분 종속.
분해:

```
Subject(subject_id, subject_name)
Score(student_id, subject_id, score)
```

## Q9: 3NF vs BCNF

비교: 3NF는 비주요 속성이 비주요 속성에 의존하지 않게(이행 종속 제거). BCNF는 모든 결정자가 후보키여야 함.
암기: BCNF ⊃ 3NF (더 강한 제약). "결정자는 모두 후보키"라는 문장을 떠올리면 됩니다.

## Q10: X→Y와 키 결정

해석: X 값이 같으면 Y 값이 반드시 같다 → X가 Y를 결정.
키 결정 방법: 함수적 종속성으로 폐포 X+를 구해 모든 속성을 포함하면 X는 슈퍼키. 최소성을 만족하면 후보키.

---

## 퀵체크 정답

- (1_Introduction Q1) HAVING
- (1_Introduction Q2) NULL
- (1_Introduction Q3) BCNF는 모든 결정자가 후보키여야 함
- (2_Concepts Q1) WHERE는 집계 전, HAVING은 집계 후
- (2_Concepts Q2) LEFT JOIN의 오른쪽 테이블 컬럼들
- (정규화 Q1) 부분 함수 종속
- (정규화 Q2) 결정자(Determinant)

## 복습 키워드(1D/3D/7D 권장 루프)

- GROUP BY vs HAVING, INNER vs LEFT
- COUNT(\*) vs COUNT(col), 스칼라 서브쿼리
- 1NF/2NF/3NF/BCNF, 함수적 종속성, 후보키/대체키
