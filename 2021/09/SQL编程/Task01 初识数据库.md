课程链接: [DataWhale/wonderful-sql](https://github.com/datawhalechina/wonderful-sql)

### 1 SQL的基本语法

#### 1.1 语句规则

- SQL语句要以分号（ ; ）结尾
- SQL 不区分关键字的大小写，但是插入到表中的数据是区分大小写的
- win 系统默认不区分表名及字段名的大小写, linux / mac 默认严格区分表名及字段名的大小写
- 单词需要用半角空格或者换行来分隔

#### 1.2 命名规则

- 只能使用半角英文字母, 数字, 下划线作为数据库, 表和列的名称
- 名称必须以半角英文字母开头

#### 1.3 基本数据类型

- INTEGER 型

用来指定存储整数的列的数据类型（数字型），不能存储小数。

- CHAR 型

用来存储定长字符串，当列中存储的字符串长度达不到最大长度的时候，使用半角空格进行补足，由于会浪费存储空间，所以一般不使用。

- VARCHAR 型

用来存储可变长度字符串，定长字符串在字符数未达到最大长度时会用半角空格补足，但可变长字符串不同，即使字符数未达到最大长度，也不会用半角空格补足。

- DATE 型

用来指定存储日期（年月日）的列的数据类型（日期型）。

#### 1.4 约束设置

约束是除了数据类型之外，对列中存储的数据进行限制或者追加条件的功能。

- `NOT NULL`: 非空约束，即该列必须输入数据。

- `PRIMARY KEY`: 主键约束，代表该列是唯一值，可以通过该列取出特定的行的数据。

### 2 SQL基础语句

#### 2.1 数据库的创建( CREATE DATABASE )

语法: 

```mysql
CREATE DATABASE < 数据库名称 > ;
```

例子:

```mysql
CREATE DATABASE shop;
```

#### 2.2 表的创建( CREATE TABLE )

语法:

```mysql
CREATE TABLE < 表名 >
( < 列名 1> < 数据类型 > < 该列所需约束 > ,
  < 列名 2> < 数据类型 > < 该列所需约束 > ,
  < 列名 3> < 数据类型 > < 该列所需约束 > ,
  < 列名 4> < 数据类型 > < 该列所需约束 > ,
  .
  .
  .
  < 该表的约束 1> , < 该表的约束 2> ,……);
```

例子:

```mysql
CREATE TABLE product
(product_id CHAR(4) NOT NULL,
 product_name VARCHAR(100) NOT NULL,
 product_type VARCHAR(32) NOT NULL,
 sale_price INTEGER ,
 purchase_price INTEGER ,
 regist_date DATE ,
 PRIMARY KEY (product_id));
```

#### 2.3 表的删除

- 整张表删除( DROP TABLE )

  语法:

  ```mysql
  DROP TABLE < 表名 > ;
  ```

  例子:

  ``` mysql
  DROP TABLE product;
  ```

- 整列删除( ALTER TABLE )

  语法:

  ```mysql
  ALTER TABLE < 表名 > DROP COLUMN < 列名 >;
  ```

  例子:

  ```mysql
  ALTER TABLE product DROP COLUMN product_name_pinyin;
  ```

- 删除行

  所有行:

  ```mysql
  DELETE FROM < 表名 >;
  ```

  特定行:

  ```mysql
  DELETE FROM < 表名 > WHERE < 条件 >;
  ```

- 清空表( TRUNCATE TABLE )

  语法:

  ```mysql
  TRUNCATE TABLE < 表名 >;
  ```

#### 2.4 表的更新

- 添加列

  语法:

  ```mysql
  ALTER TABLE < 表名 > ADD COLUMN < 列的定义 >;
  ```

  例子:

  ```mysql
  ALTER TABLE product DROP COLUMN product_name_pinyin;
  ```

- 更新数据

  语法:

  ```mysql
  UPDATE <表名>
     SET <列名> = <表达式> [, <列名2>=<表达式2>...];  
   WHERE <条件>;   -- 可选，非常重要。
   ORDER BY 子句;  -- 可选
   LIMIT 子句;     -- 可选
  ```

  例子:

  ```mysql
  -- 修改所有的注册时间
  UPDATE product
     SET regist_date = '2009-10-10';  
  -- 仅修改部分商品的单价
  UPDATE product
     SET sale_price = sale_price * 10
   WHERE product_type = '厨房用具';  
  -- 将商品编号为0008的数据（圆珠笔）的登记日期更新为NULL(只有未设置NOT NULL和非主键的列才可以)
  UPDATE product
     SET regist_date = NULL
   WHERE product_id = '0008';  
  -- 多列更新
  UPDATE product
     SET sale_price = sale_price * 10,
         purchase_price = purchase_price / 2
   WHERE product_type = '厨房用具';  
  ```

- 插入数据

  语法:

  ```mysql
  INSERT INTO <表名> (列1, 列2, 列3, ……) VALUES (值1, 值2, 值3, ……);  
  ```

  例子:

  ```mysql
  -- 包含列清单
  INSERT INTO productins (product_id, product_name, product_type, sale_price, purchase_price, regist_date) VALUES ('0005', '高压锅', '厨房用具', 6800, 5000, '2009-01-15');
  -- 省略列清单
  INSERT INTO productins VALUES ('0005', '高压锅', '厨房用具', 6800, 5000, '2009-01-15');  
  -- 多行INSERT （ DB2、SQL、SQL Server、 PostgreSQL 和 MySQL多行插入）
  INSERT INTO productins VALUES ('0002', '打孔器', '办公用品', 500, 320, '2009-09-11'),
                                ('0003', '运动T恤', '衣服', 4000, 2800, NULL),
                                ('0004', '菜刀', '厨房用具', 3000, 2800, '2009-09-20');  
  
  ```

  

## 练习题

- 1.1 编写一条 CREATE TABLE 语句，用来创建一个包含表 1-A 中所列各项的表 Addressbook （地址簿），并为 regist_no （注册编号）列设置主键约束。
  ```mysql
  CREATE TABLE 	Addressbook
  (regist_no INTEGER NOT NULL,
   name VARCHAR(128) NOT NULL,
   address VARCHAR(256) NOT NULL,
   tel_no CHAR(10),
   mail_address CHAR(20),
   PRIMARY KEY (regist_no));
  ```
  
- 1.2 假设在创建练习1.1中的 Addressbook 表时忘记添加如下一列 postal_code （邮政编码）了，请把此列添加到 Addressbook 表中。

  列名 ： postal_code

  数据类型 ：定长字符串类型（长度为 8）

  约束 ：不能为 NULL
  ```mysql
  ALTER TABLE addressbook ADD COLUMN postal_code CHAR(8) NOT NULL;
  ```
  
 - 1.3 请补充如下 SQL 语句来删除 Addressbook 表。

   ```mysql
   ( DROP ) TABLE addressbook;
   ```

 - 1.4 是否可以编写 SQL 语句来恢复删除掉的 Addressbook 表？

    不可以. 无法直接恢复, 如果有备份则可以恢复.