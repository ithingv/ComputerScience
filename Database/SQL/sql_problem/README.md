<div align='center'>
  <h1> SQL 문제풀이 </h1>
  <h5>제목을 클릭하면 문제를 확인하실 수 있습니다.</h5>
</div>

## SELECT
## SUM, MAX, MIN
## JOIN
## String, Date



## IS NULL
[이름이 없는 동물의 아이디](https://programmers.co.kr/learn/courses/30/lessons/59039)
```
# Level 1
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
```
[이름이 있는 동물의 아이디](https://programmers.co.kr/learn/courses/30/lessons/59407)
```
# Level 1
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
```
[NULL 처리하기](https://programmers.co.kr/learn/courses/30/lessons/59410)
```
# Level 2
SELECT ANIMAL_TYPE,IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```


## GROUP BY
   [고양이와 개는 몇 마리 있을까](https://programmers.co.kr/learn/courses/30/lessons/59040)

```
# Level 2
SELECT ANIMAL_TYPE, COUNT(*) count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE
```

   [동명 동물 수 찾기](https://programmers.co.kr/learn/courses/30/lessons/59041)
```
# Level 2
SELECT NAME, COUNT(*) COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME
```

   [입양 시간 구하기](https://programmers.co.kr/learn/courses/30/lessons/59412)
```
# Level 2
SELECT HOUR(DATETIME) HOUR, COUNT(*) COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR > 8 AND HOUR < 20
ORDER BY HOUR
```

   [입양 시각 구하기(2)]()

----