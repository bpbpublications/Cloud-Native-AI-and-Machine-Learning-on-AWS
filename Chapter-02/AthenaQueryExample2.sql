    SELECT DATE, CATEGORY, CONSTELLATION
      avg(stellar_coordinate) as coordinate,
      avg(stellar_coordinate/stellar_size) as average_stellar_momentum,
      avg(stars_in_constellation) as average_stars, 
      stellar_size (stars_in_constellation, .99) 99th_percentile
    FROM stellar_coordinate_data_table
    WHERE DATE > ‘2002%’ AND (TYPE = 'O' OR TYPE = 'A'
    GROUP BY CONSTELLATION
    ORDER BY 99th_percentile

