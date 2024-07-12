-- trigger
DELIMITER $$
CREATE TRIGGER DQUANTITY
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
END$$

DELIMITER ;