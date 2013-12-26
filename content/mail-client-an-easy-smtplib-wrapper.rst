Mail client: An easy smtplib wrapper.
#####################################
:date: 2013-08-08 20:14
:author: aesptux
:category: Programming, Python
:tags: easy, email, mailclient, module, pip, python, send, smtpd, wrapper
:slug: mail-client-an-easy-smtplib-wrapper

I published to github `mailclient`_, a wrapper for the standard smtplib
and email libraries.

Smtplib and email are no fun to work with, for example if you want to
attach a file, you have to import the right MIMEType.

I built this wrapper to make sending emails with Python easier, for
example:

::

    # create message
    msg = mail.Message('This will be the subject', 'This will be the body content',
     'sender@sender.com', 'to@you.com, and@you.com, foryou@too.com')

    # create server connection
    s = mail.Server('localhost', '25') 

    # attach file
    msg.attach('/path/to/file')
    # send
    s.send(msg)

Mailclient is on pypi, so if you want to install, just use pip:

::

    pip install mailclient

For full documentation, examples and source code, please refer to the
project on `Github`_.

.. _mailclient: https://github.com/aesptux/mailclient
.. _Github: https://github.com/aesptux/mailclient
