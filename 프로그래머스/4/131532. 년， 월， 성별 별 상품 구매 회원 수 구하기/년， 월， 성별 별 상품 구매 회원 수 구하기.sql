-- 코드를 입력하세요
SELECT YEAR(B.SALES_DATE) as YEAR, MONTH(B.SALES_DATE) as MONTH, A.GENDER, COUNT(DISTINCT B.USER_ID) as USERS FROM USER_INFO A 
JOIN ONLINE_SALE B ON A.USER_ID = B.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER 
