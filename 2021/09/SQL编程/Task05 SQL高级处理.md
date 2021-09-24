课程链接:[DataWhale/wonderful-sql](https://github.com/datawhalechina/wonderful-sql/blob/main/ch05:%20SQL高级处理.md)

### 1. 窗口函数

语法:

```sql
<窗口函数> OVER ([PARTITION BY <列名>]
                     ORDER BY <排序用列名>)  
```

其中[ ]中的内容可以省略。

**PARTITON BY** 是用来分组，即选择要看哪个窗口，类似于 GROUP BY 子句的分组功能，但是 PARTITION BY 子句并不具备 GROUP BY 子句的汇总功能，并不会改变原始表中记录的行数。

**ORDER BY** 是用来排序，即决定窗口内，是按那种规则(字段)来排序的。

例子:

```sql
SELECT product_name
       ,product_type
       ,sale_price
       ,RANK() OVER (PARTITION BY product_type
                         ORDER BY sale_price) AS ranking
  FROM product;  
```

#### 1.1 专用窗口函数

- **RANK函数**

计算排序时，如果存在相同位次的记录，则会跳过之后的位次。

例）有 3 条记录排在第 1 位时：1 位、1 位、1 位、4 位……

- **DENSE_RANK函数**

同样是计算排序，即使存在相同位次的记录，也不会跳过之后的位次。

例）有 3 条记录排在第 1 位时：1 位、1 位、1 位、2 位……

- **ROW_NUMBER函数**

赋予唯一的连续位次。

例）有 3 条记录排在第 1 位时：1 位、2 位、3 位、4 位

例子:

```sql
SELECT  product_name
       ,product_type
       ,sale_price
       ,RANK() OVER (ORDER BY sale_price) AS ranking
       ,DENSE_RANK() OVER (ORDER BY sale_price) AS dense_ranking
       ,ROW_NUMBER() OVER (ORDER BY sale_price) AS row_num
  FROM product;  
```

#### 1.2 聚合窗口函数

聚合函数在开窗函数中的使用方法和之前的专用窗口函数一样，但是出来的结果是一个**累计**的聚合函数值。

例子:

```sql
SELECT  product_id
       ,product_name
       ,sale_price
       ,SUM(sale_price) OVER (ORDER BY product_id) AS current_sum
       ,AVG(sale_price) OVER (ORDER BY product_id) AS current_avg  
  FROM product;  
```

#### 1.3 窗口函数应用 - 计算移动平均

聚合函数在窗口函数使用时，计算的是累积到当前行的所有的数据的聚合。 实际上，还可以指定更加详细的**汇总范围**。该汇总范围成为**框架(frame)。**

`ROWS <n> PRECEDING`（“之前”）， 将框架指定为 “截止到之前 n 行”，加上自身行

`ROWS <n> FOLLOWING`（“之后”）， 将框架指定为 “截止到之后 n 行”，加上自身行

`ROWS BETWEEN <n> PRECEDING AND n FOLLOWING`，将框架指定为 “之前1行” + “之后1行” + “自身”

语法:

```sql
<窗口函数> OVER (ORDER BY <排序用列名>
                 ROWS n PRECEDING )  
                 
<窗口函数> OVER (ORDER BY <排序用列名>
                 ROWS BETWEEN n PRECEDING AND n FOLLOWING)
```

### 2 GROUPING运算符

#### 2.1 ROLLUP - 计算合计及小计

常规的GROUP BY 只能得到每个分类的小计，有时候还需要计算分类的合计，可以用 ROLLUP关键字。

例子:

```sql
SELECT  product_type
       ,regist_date
       ,SUM(sale_price) AS sum_price
  FROM product
 GROUP BY product_type, regist_date WITH ROLLUP;  
```



### 练习题

#### 1

请说出针对本章中使用的 product（商品）表执行如下 SELECT 语句所能得到的结果。

```sql
SELECT  product_id
       ,product_name
       ,sale_price
       ,MAX(sale_price) OVER (ORDER BY product_id) AS Current_max_price
  FROM product;
```

`Current_max_price`列为按照product_id排序的累计最大值

#### 2

继续使用product表，计算出按照登记日期（regist_date）升序进行排列的各日期的销售单价（sale_price）的总额。排序是需要将登记日期为NULL 的“运动 T 恤”记录排在第 1 位（也就是将其看作比其他日期都早）

```sql
SELECT SUM(sale_price) OVER (ORDER BY regist_date) AS Current_sum_price
FROM product
ORDER BY regist_date
```

#### 3

思考题

① 窗口函数不指定PARTITION BY的效果是什么？

② 为什么说窗口函数只能在SELECT子句中使用？实际上，在ORDER BY 子句使用系统并不会报错。



① 不分组, 按照原表的数据累计

② 执行顺序会造成影响从而可能得到错误的结果
