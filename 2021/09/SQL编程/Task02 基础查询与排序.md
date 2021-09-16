课程链接: [DataWhale/wonderful-sql](https://github.com/datawhalechina/wonderful-sql)

### 1 语句基础

#### 1.1 SELECT语句

语法:

```mysql
SELECT <列名>, 
  FROM <表名>;
```

相关法则:

- 星号（*）代表全部列的意思。
- SQL中可以随意使用换行符，不影响语句执行（但不可插入空行）。
- 设定汉语别名时需要使用双引号（"）括起来。
- 在SELECT语句中使用DISTINCT可以删除重复行。
- 注释是SQL语句中用来标识说明或者注意事项的部分。分为1行注释"-- "和多行注释两种"/* */"。

#### 1.2 WHERE语句

语法:

```mysql
SELECT <列名>, ……
  FROM <表名>
 WHERE <条件表达式>;
```

#### 1.3 常用聚合函数

- COUNT：计算表中的记录数（行数）
- SUM：计算表中数值列中数据的合计值
- AVG：计算表中数值列中数据的平均值
- MAX：求出表中任意列中数据的最大值
- MIN：求出表中任意列中数据的最小值

例子:

```mysql
-- 计算全部数据的行数（包含NULL）
SELECT COUNT(*)
  FROM product;
-- 计算NULL以外数据的行数
SELECT COUNT(purchase_price)
  FROM product;
-- 计算销售单价和进货单价的合计值
SELECT SUM(sale_price), SUM(purchase_price) 
  FROM product;
-- 计算销售单价和进货单价的平均值
SELECT AVG(sale_price), AVG(purchase_price)
  FROM product;
-- MAX和MIN也可用于非数值型数据
SELECT MAX(regist_date), MIN(regist_date)
  FROM product;
```

#### 1.4 GROUP BY语句

语法:

```mysql
SELECT <列名1>,<列名2>, <列名3>, ……
  FROM <表名>
 GROUP BY <列名1>, <列名2>, <列名3>, ……;
```

例子:

```mysql
-- 按照商品种类统计数据行数
SELECT product_type, COUNT(*)
  FROM product
 GROUP BY product_type;
```

书写顺序:

SELECT → FROM → WHERE → GROUP BY

#### 1.5 HAVING语句

将表使用GROUP BY分组后, 可以通过HAVING取出其中的组, 用法和WHERE类似.

语法:

```mysql
SELECT <列名1>,<列名2>, <列名3>, ……
  FROM <表名>
 GROUP BY <列名1>, <列名2>, <列名3>, ……;
HAVING <条件表达式>;
```

例子:

```mysql
SELECT product_type, COUNT(*)
  FROM product
 GROUP BY product_type
HAVING COUNT(*) = 2;
```

#### 1.6 ORDER BY语句

语法:

```mysql
SELECT <列名1>, <列名2>, <列名3>, ……
  FROM <表名>
 ORDER BY <排序基准列1>, <排序基准列2>, ……
```

例子:

```mysql
-- 降序排列
SELECT product_id, product_name, sale_price, purchase_price
  FROM product
 ORDER BY sale_price DESC;
-- 多个排序键
SELECT product_id, product_name, sale_price, purchase_price
  FROM product
 ORDER BY sale_price, product_id;
-- 当用于排序的列名中含有NULL时，NULL会在开头或末尾进行汇总。
SELECT product_id, product_name, sale_price, purchase_price
  FROM product
 ORDER BY purchase_price;
```



### 2 运算符

#### 2.1 算数运算符

| 含义 | 运算符 |
| ---- | ------ |
| 加法 | +      |
| 减法 | -      |
| 乘法 | *      |
| 除法 | /      |

#### 2.2 比较运算符

| 运算符 | 含义     |
| ------ | -------- |
| =      | 相等     |
| <>     | 不相等   |
| >=     | 大于等于 |
| >      | 大于     |
| <=     | 小于等于 |
| <      | 小于     |

相关代码:

- SELECT子句中可以使用常数或者表达式。
- 使用比较运算符时一定要注意不等号和等号的位置。
- 字符串类型的数据原则上按照字典顺序进行排序，不能与数字的大小顺序混淆。
- 希望选取NULL记录时，需要在条件表达式中使用IS NULL运算符。希望选取不是NULL的记录时，需要在条件表达式中使用IS NOT NULL运算符。

例子:

```mysql
-- SQL语句中也可以使用运算表达式
SELECT product_name, sale_price, sale_price * 2 AS "sale_price x2"
  FROM product;
-- WHERE子句的条件表达式中也可以使用计算表达式
SELECT product_name, sale_price, purchase_price
  FROM product
 WHERE sale_price-purchase_price >= 500;
/* 对字符串使用不等号
首先创建chars并插入数据
选取出大于‘2’的SELECT语句*/
-- DDL：创建表
CREATE TABLE chars
（chr CHAR（3）NOT NULL, 
PRIMARY KEY（chr））;
-- 选取出大于'2'的数据的SELECT语句('2'为字符串)
SELECT chr
  FROM chars
 WHERE chr > '2';
-- 选取NULL的记录
SELECT product_name, purchase_price
  FROM product
 WHERE purchase_price IS NULL;
-- 选取不为NULL的记录
SELECT product_name, purchase_price
  FROM product
 WHERE purchase_price IS NOT NULL;
```

#### 2.4 逻辑运算符

| 运算符 | 含义 |
| ------ | ---- |
| NOT    | 非   |
| AND    | 与   |
| OR     | 或   |

### 练习题

1. 编写一条SQL语句，从 `product`(商品) 表中选取出“登记日期(`regist`)在2009年4月28日之后”的商品，查询结果要包含 `product name` 和 `regist_date` 两列。

   ```mysql
   SELECT product_name, regist_date
   FROM product
   WHERE regist_date > 2009-4-28
   ```

2. 请说出对product 表执行如下3条SELECT语句时的返回结果。

   ```mysql
   SELECT *
     FROM product
    WHERE purchase_price = NULL;
   ```

   ```mysql
   SELECT *
     FROM product
    WHERE purchase_price = NULL;
   ```

   ```mysql
   SELECT *
     FROM product
    WHERE product_name > NULL;
   ```

   均为空

3. 代码清单2-22（2-2节）中的SELECT语句能够从product表中取出“销售单价（saleprice）比进货单价（purchase price）高出500日元以上”的商品。请写出两条可以得到相同结果的SELECT语句。执行结果如下所示。

   ```
   product_name | sale_price | purchase_price 
   -------------+------------+------------
   T恤衫         | 　 1000    | 500
   运动T恤       |    4000    | 2800
   高压锅        |    6800    | 5000
   ```

   ①

   ```mysql
   SELECT product_name, sale_price, purchase_price
     FROM product
    WHERE purchase_price >= 500 AND product_type = "衣服" OR purchase_price >= 3000;
   ```

   ②

   ```mysql
   SELECT product_name, sale_price, purchase_price
     FROM product
    WHERE purchase_price >= 3000 OR product_type = "衣服";
   ```

4. 请写出一条SELECT语句，从product表中选取出满足“销售单价打九折之后利润高于100日元的办公用品和厨房用具”条件的记录。查询结果要包括product_name列、product_type列以及销售单价打九折之后的利润（别名设定为profit）。

   提示：销售单价打九折，可以通过saleprice列的值乘以0.9获得，利润可以通过该值减去purchase_price列的值获得。

   ```mysql
   SELECT prouduct_name, product_type, (0.9 * sale_price - purchase_price) AS profit
     FROM product
    WHERE 0.9 * sale_price - purchase_price > 100 AND (product_type = "办公用品" OR product_type = "厨房用具");
   ```

5. 请指出下述SELECT语句中所有的语法错误。

   ```mysql
   SELECT product_id, SUM（product_name）
   --本SELECT语句中存在错误。
     FROM product 
    GROUP BY product_type 
    WHERE regist_date > '2009-09-01';
   ```

   ① WHERE的位置应在GROUP BY前, 或使用HAVING;

   ② 使用了全角括号

6. 请编写一条SELECT语句，求出销售单价（ `sale_price` 列）合计值大于进货单价（ `purchase_price` 列）合计值1.5倍的商品种类。执行结果如下所示。

   ```
   product_type | sum  | sum 
   -------------+------+------
   衣服         | 5000 | 3300
   办公用品      |  600 | 320
   ```

   ```mysql
   SELECT product_type, SUM(sale_price) AS sum, SUM(purchase_price) AS sum
   FROM product
   GROUP BY product_type
   HAVING SUM(sale_price) > 1.5 * SUM(purchase_price);
   ```

7. 此前我们曾经使用SELECT语句选取出了product（商品）表中的全部记录。当时我们使用了 `ORDER BY` 子句来指定排列顺序，但现在已经无法记起当时如何指定的了。请根据下列执行结果，思考 `ORDER BY` 子句的内容。

   ```mysql
   SELECT *
   FROM product
   ORDER BY - regist_date 
   ```