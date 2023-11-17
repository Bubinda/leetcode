delete all expired medicines wihtou using CTE or SELECT statments

table "public.stock" -> medicines

Column          type            Nullable
stock_id        integer         not null
medicine_id     integer         not null
quantity        integer         not null
expiry_date     date            not null

# conventional approach
DELETE FROM medicines
WHERE medicine_id IN (
    SELECT medicine_id
    FROM stock
    WHERE medicine_id = medicines.medicine_id
        AND expiry_date <= CURRENT_DATE
)


# without SELECT
DELETE FROM
    medicines
USING stock
WHERE 
    medicines.medicine_id = stock.medicine_id
    AND stock.expiry_date <= CURRENT_DATE