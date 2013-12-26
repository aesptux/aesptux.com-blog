Python script to backup and restore rpm packages
################################################
:date: 2012-04-28 13:36
:author: aesptux
:category: backup, Linux, Programming, Python
:tags: backup, centos, fedora, installed, manage, packages, python, red hat, restore, rpm, script
:slug: python-script-to-backup-and-restore-rpm-packages

I've written a simple Python script to backup and restore installed rpm
packages.

On Ubuntu, I used APTonCD for this matter, but in this case, for Fedora
I decided to use my own script.

The usage is quite simple, only two parameters:

Backup:

::

    python rpm-backup.py --backup

Restore:

::

    python rpm-backup.py --restore

 

This is source code, although you can download it from my
`github`_ (link to the gh-page of the entire repository)

::

    #!/usr/bin/python

    ''' Backup script for installed packages.
    Only RPM.
    Tested under Fedora
    Error list:
    Code 1: Missing modules
    Code 2: Not root
    Code 3: Tried to restore without backup file'''

    print "     ____  ____  __  ___"
    print "    / __ \/ __ \/  |/  /"
    print "   / /_/ / /_/ / /|_/ / "
    print "  / _, _/ ____/ /  / /  "
    print " /_/ |_/_/   /_/  /_/   "


    print "        ____  ___   ________ ____  ______ "
    print "       / __ )/   | / ____/ //_/ / / / __ \ "
    print "      / __  / /| |/ /   / ,< / / / / /_/ /"
    print "     / /_/ / ___ / /___/ /| / /_/ / ____/ "
    print "    /_____/_/  |_\____/_/ |_\____/_/      "

    #Import modules
    try:
        import os
        import argparse
    except ImportError:
        print "Could not find required modules. Exiting..."
        exit(1)

    # Create parser
    parser = argparse.ArgumentParser(description='Backup your installed packages.', epilog="Written by Adrian Espinosa (aesptux).")


    # if user types --backup it will be stored as true in variable backup
    #if user types --restore it will be stored as true in variable backup
    parser.add_argument('--backup', action='store_true', dest='backup', help='Backup your packages.')
    parser.add_argument('--restore',  action='store_true', dest='restore', help='Restore your packages.')


    args = parser.parse_args()
    #print args
    #print(args.option(args.integers))

    #variables
    userlogged = os.environ['LOGNAME']
    directory = '/%s' % (userlogged)
    filename = 'packages-installed.bak'
    path = directory + '/' + filename
    rpm_list = []
    print " "
    print "Hello %s!" % (userlogged)
    print "If you are having troubles using the script, use the argument '--help'"


    def dobackup():

        ''' Create backup '''
        print "Starting copy..."
        command = 'rpm -qa > ' + path
        #os.system('touch '+path)
        os.system(command)
        os.system('echo Total packages: ; cat ' + path + ' | wc -l ')
        print "Done."


    def dorestore():

        ''' Restore packages'''
        print "Starting restore..."
        global rpm_list
        # try, except, to see if the backup file exists
        try:
            for line in open(path, 'r'):
                rpm_list.append(line)
        except IOError:
            print "The backup file does not exist. Please, create a backup first. "
            exit(3)
        # take the list and join it
        rpm_list = ''.join(rpm_list)
        # remove \n
        rpm_list = rpm_list.replace('\n', ' ')
        os.system('yum install ' + rpm_list)


    #This script must be run as root
    if userlogged != 'root':
        print "You have to run the script as root"
        exit(2)


    # if backup is true, dobackup. Else if restore is true, dorestore
    if args.backup == True:
        dobackup()
    elif args.restore == True:
        dorestore()

 

Then, you can set up a cron job like this:

::

    0 22 * * * /usr/bin/python /root/rpm-backup.py --backup

 

.. _github: http://aesptux.github.com/python-scripts/
