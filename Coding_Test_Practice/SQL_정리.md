## SQL 요약 노트

### 1. 기본 SELECT 문법
- **SELECT 문**: 특정 열을 조회할 때 사용
  ```sql
  SELECT 열이름 FROM 테이블이름;
  ```
- **DISTINCT**: 중복된 값을 제거하고 고유한 값만 조회
  ```sql
  SELECT DISTINCT 열이름 FROM 테이블이름;
  ```

### 2. 조건 필터링
- **WHERE 절**: 행(row) 단위로 데이터를 필터링
  ```sql
  SELECT 열이름 FROM 테이블이름 WHERE 조건;
  ```
- **NULL 값 비교**: `IS NULL` 또는 `IS NOT NULL`을 사용하여 NULL 값 확인
  ```sql
  SELECT 열이름 FROM 테이블이름 WHERE 열이름 IS NULL;
  ```

### 3. 집계 함수
- 데이터 그룹화와 함께 사용하는 함수들:
  - **COUNT**: 개수 세기
  - **SUM**: 합계 계산
  - **AVG**: 평균 계산
  - **MAX/MIN**: 최대/최소 값
  
  예시:
  ```sql
  SELECT COUNT(*) FROM 테이블이름;
  SELECT MAX(열이름) FROM 테이블이름;
  ```

### 4. GROUP BY와 HAVING
- **GROUP BY**: 특정 열을 기준으로 데이터를 그룹화
  ```sql
  SELECT 열이름, COUNT(*) FROM 테이블이름 GROUP BY 열이름;
  ```
- **HAVING**: `GROUP BY` 이후 집계 결과에 조건을 걸 때 사용
  ```sql
  SELECT 열이름, COUNT(*) FROM 테이블이름 GROUP BY 열이름 HAVING COUNT(*) > 1;
  ```

### 5. ORDER BY와 LIMIT
- **ORDER BY**: 결과를 오름차순(`ASC`, 기본값) 또는 내림차순(`DESC`)으로 정렬
  ```sql
  SELECT 열이름 FROM 테이블이름 ORDER BY 열이름 DESC;
  ```
- **LIMIT**: 결과 행의 개수를 제한
  ```sql
  SELECT 열이름 FROM 테이블이름 LIMIT 10;
  ```

### 6. JOIN (테이블 결합)
- **INNER JOIN**: 두 테이블에서 일치하는 행만 결합
  ```sql
  SELECT a.열이름, b.열이름
  FROM 테이블A AS a
  INNER JOIN 테이블B AS b ON a.기준열 = b.기준열;
  ```
- **LEFT JOIN**: 왼쪽 테이블의 모든 행을 포함하고, 오른쪽 테이블에 일치하는 값이 없으면 `NULL`
  ```sql
  SELECT a.열이름, b.열이름
  FROM 테이블A AS a
  LEFT JOIN 테이블B AS b ON a.기준열 = b.기준열;
  ```

### 7. CASE WHEN (조건에 따른 값 설정)
- **CASE WHEN**: 특정 조건에 따라 다른 값을 표시
  ```sql
  SELECT 열이름,
    CASE
      WHEN 조건1 THEN '결과1'
      WHEN 조건2 THEN '결과2'
      ELSE '기본값'
    END AS 새열이름
  FROM 테이블이름;
  ```
- 예시 (길이에 따른 크기 구분):
  ```sql
  SELECT LENGTH,
    CASE 
      WHEN LENGTH <= 3 THEN '작음'
      WHEN LENGTH > 3 AND LENGTH <= 10 THEN '중간'
      ELSE '큼'
    END AS SIZE_CATEGORY
  FROM 테이블이름;
  ```

### 8. 서브쿼리와 SELF JOIN
- **서브쿼리**: `SELECT` 문 안에 또 다른 `SELECT` 문을 포함하여 쿼리 실행
  ```sql
  SELECT 열이름 FROM (SELECT 열이름 FROM 테이블이름 WHERE 조건) AS 서브쿼리;
  ```
- **SELF JOIN**: 동일한 테이블을 여러 번 참조하여 연결
  ```sql
  SELECT a.ID, b.PARENT_ID
  FROM 테이블이름 AS a
  LEFT JOIN 테이블이름 AS b ON a.ID = b.PARENT_ID;
  ```

### 9. 실행 순서
SQL 쿼리의 실제 실행 순서:
1. **FROM**: 테이블을 선택하고 `JOIN` 수행
2. **ON**: `JOIN` 조건 적용
3. **WHERE**: 행 단위로 필터링
4. **GROUP BY**: 데이터 그룹화
5. **HAVING**: 집계 결과에 조건 필터링
6. **SELECT**: 열 선택 및 집계 함수 적용
7. **ORDER BY**: 결과 정렬
8. **LIMIT**: 행 수 제한

---

이 요약 노트를 바탕으로 SQL 쿼리 작성과 최적화를 쉽게 학습할 수 있을 것입니다! 추가 질문이 있다면 언제든지 물어보세요.