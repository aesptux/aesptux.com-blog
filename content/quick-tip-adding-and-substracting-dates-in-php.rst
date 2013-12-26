Quick tip: Adding and substracting dates in PHP
###############################################
:date: 2012-05-06 12:24
:author: aesptux
:category: Php, Programming
:tags: add, bug, date, dates, easy, function, php, substract, unix
:slug: quick-tip-adding-and-substracting-dates-in-php

More simple than it may seems. It will take care of adjusting months and
days automatically:

\ **Working with days:**\ 

::

    // My date Y-m-d
    $mydate = "2012-05-06";
    //Adding five days
    $newdate = date(“Y-m-d”, strtotime($mydate. " +5 days”));
    // Substracting five days
    $newdate = date(“Y-m-d”, strtotime($mydate. " -5 days”));

**Working with weeks:**

::

    // My date Y-m-d
    $mydate = "2012-05-06";
    //Adding two weeks
    $newdate = date(“Y-m-d”, strtotime($mydate. " +2 weeks”));
    // Substracting one week
    $newdate = date(“Y-m-d”, strtotime($mydate. " -1 week”));

**Working with months**

::

    // My date Y-m-d
    $mydate = "2012-05-06";
    //Adding six months
    $newdate = date(“Y-m-d”, strtotime($mydate. " +6 months”));
    // Substracting three months
    $newdate = date(“Y-m-d”, strtotime($mydate. " -3 months”));

**Working with years**

::

    // My date Y-m-d
    $mydate = "2012-05-06";
    //Adding ten years
    $newdate = date(“Y-m-d”, strtotime($mydate. " +10 years”));
    // Substracting two years
    $newdate = date(“Y-m-d”, strtotime($mydate. " -2 years”));

Be aware of the `Unix Millenium Bug`_

.. _Unix Millenium Bug: https://en.wikipedia.org/wiki/Year_2038_problem
