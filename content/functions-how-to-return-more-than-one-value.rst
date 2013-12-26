Functions: How to return more than one value.
#############################################
:date: 2011-09-09 13:46
:author: aesptux
:category: Programming
:tags: c, development, how to, JavaScript, more, one, php, Programming, return, several, two values, value
:slug: functions-how-to-return-more-than-one-value

We cannot return two variables from a function, but **we could use an
array for that**.

So for example, in JavaScript, it would be like this:

::

    function foo() {
        // do something here
        // whatever
        return [myvalue, myothervalue, otherthing];
    }

And then, for use those values:

::

    foo()[0] // this is myvalue
    foo()[1] // this is myothervalue
    foo()[2] // this is otherthing

This can be applied to any other language  you may know. And that's how
we return more than one value from a function
