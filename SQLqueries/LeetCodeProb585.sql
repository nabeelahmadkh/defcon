SELECT ROUND(SUM(TIV_2012),2) FROM INSURANCE 
    WHERE TIV_2011 IN
        (
            SELECT TIV_2011 FROM INSURANCE
            GROUP BY TIV_2011
            HAVING COUNT(*)>1
        )
    AND CONCAT(LAT, LON) NOT IN
        (
            SELECT CONCAT(LAT, LON)
            FROM INSURANCE
            GROUP BY LAT,LON
            HAVING COUNT(*)>1
        );