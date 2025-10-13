-- 코드를 작성해주세요
/* ID: 개체의 ID
PARENT_ID: 부모 개체 ID
SIZE_OF_COLONY: 개체의 크기
DIFFERENTIATION_DATE: 분화되어 나온 날짜
GENOTYPE: 개체의 형질

연도(year), 대장균 크기의 편차(year_dev), 개체의 id(id)
편차 = 가장 큰 대장균의 크기 - 각 대장균의 크기
*/

select year(DIFFERENTIATION_DATE) as year,
(select max(size_of_colony) from ecoli_data where year(DIFFERENTIATION_DATE) = year) - size_of_colony as year_dev,
id from ecoli_data
order by year, year_dev