课程链接:[DataWhale/wonderful-sql](https://github.com/datawhalechina/wonderful-sql/blob/main/ch04:集合运算.md)



### 1 集合运算

#### 1.1 并集( UNION )

UNION 等集合运算符通常都会除去重复的记录. 使用UNION ALL进行包含重复行的集合运算.

语法:

```mysql
<query1> UNION <query2>;
```

例子:

```mysql
SELECT product_id, product_name
  FROM Product
 UNION
SELECT product_id, product_name
  FROM Product2;
```

#### 1.2 交集( INTERSECT )

MySQL8.0仍不支持INTERSECT操作. 使用INNER JOIN进行交集运算.

语法:

```mysql
<query> FROM <tb_1> INNER JOIN <tb_2> ON <condition(s)>
```

例子:

```mysql
SELECT p1.product_id, p1.product_name
  FROM Product p1
 INNER JOIN Product2 p2
    ON p1.product_id=p2.product_id
```

#### 1.3 补集( EXCEPT )

MySQL8.0仍不支持EXCEPT操作. 使用NOT IN进行补集运算.

语法:

```mysql
<query1> FROM <tb_1> WHERE <column> NOT IN (<query2> FROM <tb_2>)
```

例子:

```mysql
SELECT * 
  FROM Product
 WHERE product_id NOT IN (SELECT product_id 
                            FROM Product2)
```

#### 1.4 对称差

两个集合A,B的对称差是指那些仅属于A或仅属于B的元素构成的集合. 

例子:

```mysql
SELECT * 
  FROM Product
 WHERE product_id NOT IN (SELECT product_id FROM Product2)
UNION
SELECT * 
  FROM Product2
 WHERE product_id NOT IN (SELECT product_id FROM Product)
```

### 2 连结( JOIN )

#### 2.1 内连结( INNER JOIN )

语法:

```mysql
FROM <tb_1> INNER JOIN <tb_2> ON <condition(s)>
```

例子:

```mysql
SELECT SP.shop_id
       ,SP.shop_name
       ,SP.product_id
       ,P.product_name
       ,P.product_type
       ,P.sale_price
       ,SP.quantity
  FROM ShopProduct AS SP
 INNER JOIN Product AS P
    ON SP.product_id = P.product_id;
```

#### 2.2 自然连结( NATURAL JOIN )

自然连结并不是区别于内连结和外连结的第三种连结, 它其实是内连结的一种特例--当两个表进行自然连结时, 会按照两个表中都包含的列名来进行等值内连结, 此时无需使用 ON 来指定连接条件。

语法:

```mysql
<query> FROM <tb_1> NATURAL JOIN <tb_2>
```

例子:

```mysql
SELECT *  FROM shopproduct NATURAL JOIN Product
```

#### 2.3 外连结( OUTER JOIN )

语法:

```mysql
-- 左连结     
FROM <tb_1> LEFT  OUTER JOIN <tb_2> ON <condition(s)>
-- 右连结     
FROM <tb_1> RIGHT OUTER JOIN <tb_2> ON <condition(s)>
-- 全外连结
FROM <tb_1> FULL  OUTER JOIN <tb_2> ON <condition(s)>
```

例子:

```mysql
SELECT SP.shop_id
       ,SP.shop_name
       ,SP.product_id
       ,P.product_name
       ,P.sale_price
  FROM Product AS P
  LEFT OUTER JOIN ShopProduct AS SP
    ON SP.product_id = P.product_id;
```



### 练习题

#### 1

找出 product 和 product2 中售价高于 500 的商品的基本信息。

```mysql
SELECT *
FROM product
WHERE sale_price > 500

UNION

SELECT *
FROM product2
WHERE sale_price > 500
```



#### 2

借助对称差的实现方式, 求product和product2的交集。

```mysql
SELECT *
FROM product
WHERE product_id IN (SELECT product_id FROM product2)

UNION

SELECT *
FROM product2
WHERE product_id IN (SELECT product_id FROM product)
```



#### 3

每类商品中售价最高的商品都在哪些商店有售 ？

```mysql
-- 参考:https://zhuanlan.zhihu.com/p/380413866
SELECT SP.product_id, shop_name, product_type

FROM (
SELECT product_id, max_price.product_type
FROM (SELECT * FROM product UNION SELECT * FROM product2) AS all_product

LEFT JOIN (
SELECT max(sale_price) AS max, product_type
FROM (SELECT * FROM product UNION SELECT * FROM product2) AS all_product
GROUP BY product_type) AS max_price
ON all_product.product_type = max_price.product_type
WHERE sale_price = max ) AS i

LEFT JOIN shopproduct AS SP
on i.product_id = SP.product_id
```



#### 4

分别使用内连结和关联子查询每一类商品中售价最高的商品。

```mysql
-- 内连结
SELECT
	product_id 
FROM
	( SELECT * FROM product UNION SELECT * FROM product2 ) AS all_product
INNER JOIN ( 
	SELECT product_type, MAX( sale_price ) AS max 
	FROM ( SELECT * FROM product UNION SELECT * FROM product2 ) AS all_product 
	GROUP BY product_type ) AS max_price 
ON 
	all_product.product_type = max_price.product_type 
WHERE
	sale_price = max;
```

```mysql
-- 关联子查询
SELECT product_id
FROM
	( SELECT * FROM product UNION SELECT * FROM product2 ) p1 
WHERE
	sale_price = (
	SELECT
		max( sale_price ) 
	FROM
		( SELECT * FROM product UNION SELECT * FROM product2 ) p2 
	WHERE
		p2.product_type = p1.product_type 
	GROUP BY
	product_type 
	);
```



#### 5

用关联子查询实现：在 product 表中，取出 product_id, produc_name, slae_price, 并按照商品的售价从低到高进行排序、对售价进行累计求和。

```mysql
SELECT
	product_id,
	product_name,
	sale_price,
	( SELECT SUM( sale_price ) FROM product p2 WHERE p2.sale_price <= p.sale_price ) AS s_sale 
FROM
	product p 
ORDER BY
	sale_price;
```

