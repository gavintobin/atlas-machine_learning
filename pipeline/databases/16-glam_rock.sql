-- glam rock
SELECT
    band_name,
    (CASE
        WHEN split IS NOT NULL THEN split - formed
        ELSE 2020 - formed
    END) AS lifespan_until_2020
FROM
    bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan_until_2020 DESC
