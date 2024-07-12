from astroquery.sdss import SDSS


def query():
    # PhotoObj, SpecObj : The same ID is objid, and bestobjid respectively
    SDSS_query = """
SELECT TOP 100000 p.objID, p.ra, p.dec, p.u, p.g, p.r, p.i, p.z, p.mjd, p.fieldID, p.run, p.rerun, p.camcol, s.class, s.specObjID, s.plateID, s.fiberID, s.z AS redshift
FROM SpecObj AS s
JOIN PhotoObj AS p ON s.bestObjID = p.objID
WHERE s.class = "STAR" OR s.class = "QSO"
                 """
    SDSS_data = SDSS.query_sql(SDSS_query % (), timeout=None)
    SDSS_data.write("SDSS_Data.csv", format="csv", overwrite=True)
    print("Saved data to SDSS_Data.csv")


query()
