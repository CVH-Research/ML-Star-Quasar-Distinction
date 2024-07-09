[Example of ML Stellar Classification (Only object types)](https://towardsdatascience.com/stellar-classification-a-machine-learning-approach-5e23eb5cadb1)

[ML Code for above](https://github.com/mohd-saifuddin/Stellar-Classification-Problem)

[ML Web App for above](https://github.com/mohd-saifuddin/Stellar-Classification-App)

[Research Paper for ML Stellar Classification](https://arxiv.org/abs/2404.10757)

[SDSS DR18 Database SQL Query](https://skyserver.sdss.org/dr18/SearchTools/sql) (PhotoObj, SpecObj (same ID is objid, and bestobjid respectively))

```sql
-- For DR18 ^
-- This query does a table JOIN between the imaging (PhotoObj) and spectra
--(SpecObj) tables and includes the necessary columns in the SELECT to upload
--the results to the SAS(Science Archive Server) for FITS file retrieval.
SELECT TOP 10
p.objid,p.ra,p.dec,p.u,p.g,p.r,p.i,p.z,
p.run, p.rerun, p.camcol, p.field,
s.specobjid, s.class, s.z as redshift,
s.plate, s.mjd, s.fiberid
FROM PhotoObj AS p
JOIN SpecObj AS s ON s.bestobjid = p.objid
WHERE class = "STAR"
```

```sql
-- For DR18 ^
SELECT TOP 10
*
FROM SpecObj
WHERE class = "STAR"
```

[SDSS DR9 Database SQL Query](https://skyserver.sdss.org/dr9/en/tools/search/sql.asp)

```sql
-- For DR9 ^
SELECT TOP 50 s.elodieSpType,s.fiberID,s.plateID
FROM BESTDR9..SpecObj as s
	JOIN dbo.fGetNearbySpecObjEq(180,0.2,5.0) AS b ON b.SpecobjID = S.SpecobjID
WHERE  s.zWarning = 0
```