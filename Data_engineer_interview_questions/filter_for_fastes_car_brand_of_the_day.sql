Write a query on the given tables to get the car model with the fastest average times for the current day.

In this two-part table schema question, we’re tracking not just enter/exit times but also car make, model, and license plate info.

The car model for licensing plate information will be one-to-many, given that each license plate represents a single car, and each car model can replicate many times. Here’s an example for crossings (left) and model/license plate (right):

Column	Type
id	INTEGER
license_plate	VARCHAR
enter_time	DATETIME
exit_time	DATETIME
car_model_id	INTEGER


Column	Type
id	INTEGER
model_name	VARCHAR



SELECT
    cm.model_name,
    AVG(TIMESTAMPDIFF(SECOND, c.enter_time, c.exit_time)) AS avg_time
FROM
    crossings c
JOIN
    car_models cm ON c.car_model_id = cm.id
WHERE
    DATE(c.enter_time) = CURDATE() -- Filter for the current day
GROUP BY
    cm.model_name
ORDER BY
    avg_time ASC
LIMIT 1;


explanation:
SELECT cm.model_name: Select the car model name.
AVG(TIMESTAMPDIFF(SECOND, c.enter_time, c.exit_time)) AS avg_time: Calculate the average time in seconds for each car model.
FROM crossings c JOIN car_models cm ON c.car_model_id = cm.id: Join the crossings table with the car_models table based on the car_model_id.
WHERE DATE(c.enter_time) = CURDATE(): Filter the records for the current day.
GROUP BY cm.model_name: Group the results by car model.
ORDER BY avg_time ASC: Order the results by average time in ascending order.
LIMIT 1: Limit the result to the first row, which represents the car model with the fastest average time.