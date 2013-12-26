Transactions with MySQL.
########################
:date: 2012-01-19 13:53
:author: aesptux
:category: Databases, MySQL
:tags: acid, database, how to, mysql, rollback, savepoint, transactions, use
:slug: transactions-with-mysql

If you want to use transactions with MySQL, you will have to use InnoDB
engine, because the default engine on MySQL 5.1 (MyISAM) does not
support transactions. Otherwise, if you use MySQL 5.5 you do not have to
worry about it, because default engine is InnoDB.

A transaction is a set of SQL instructions which are run as a unit and
can be cancelled if it is required.There are confirm and cancel
operations

Transactional systems are characterized by their features:

-  Atomicity: Transaction's instructions form a logic unit.

-  Coherence: Database must coherent before and after transaction. Can't
   affect negatively.

-  Isolation: Transactions are not affected among them

-  Durability: If the transaction was executed succesfully, changes will
   be stored permanently.

   To start a transaction you can use **BEGIN**\ or **START
   TRANSACTION**

   To create a savepoint use **SAVEPOINT savepointname**

   And for rollback use whether **ROLLBACK**\ (to return to the BEGIN
   point) or **ROLLBACK TO savepointname**\ (to return another specific
   point)

   Example of use:

   .. raw:: html

      <div class="mceTemp mceIEcenter" style="text-align: justify;">

   `|Example of transactions use with MySQL|`_
       Example of transactions use with MySQL

   .. raw:: html

      </div>

   .. raw:: html

      <p style="text-align: justify;">

.. _|image1|: http://aesptux.com/wp-content/uploads/2012/01/Selection_205.png

.. |Example of transactions use with
MySQL| image:: http://aesptux.com/wp-content/uploads/2012/01/Selection_205.png
.. |image1| image:: http://aesptux.com/wp-content/uploads/2012/01/Selection_205.png
