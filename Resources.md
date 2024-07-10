# Resources

[Example of ML Stellar Classification (Only object types)](https://towardsdatascience.com/stellar-classification-a-machine-learning-approach-5e23eb5cadb1)

[ML Code for above](https://github.com/mohd-saifuddin/Stellar-Classification-Problem)

[ML Web App for above](https://github.com/mohd-saifuddin/Stellar-Classification-App)

[Paper 1](https://link.springer.com/article/10.1007/s11633-014-0789-2)

[Paper 2](https://arxiv.org/pdf/2404.10757)

[Paper 3](https://www.jsr.org/hs/index.php/path/article/download/4375/1918/26335)

[SDSS DR18 Database SQL Query](https://skyserver.sdss.org/dr18/SearchTools/sql) (PhotoObj, SpecObj (same ID is objid, and bestobjid respectively))

```sql
-- For DR18 ^
SELECT
*
FROM SpecObj
WHERE class = "STAR" OR class = "QSO" OR class = "GALAXY"
```
