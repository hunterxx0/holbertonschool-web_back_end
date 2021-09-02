-- Old school band
SELECT * 
FROM (
	SELECT band_name,
	(IFNULL(split, 2021) - formed) as lifespan
	FROM metal_bands
	WHERE style LIKE "%Glam rock%"
	) sub
ORDER BY lifespan DESC;
