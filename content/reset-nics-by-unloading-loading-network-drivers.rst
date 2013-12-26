Reset NICs by unloading / loading network drivers
#################################################
:date: 2012-03-30 23:24
:author: aesptux
:category: Linux, Networking
:tags: bash, card, delete, driver, Linux, load, modprobe, network, Networking, nic, remove, reset, rmmod, rules.d, script, shell, udev, unload
:slug: reset-nics-by-unloading-loading-network-drivers

This script is specially useful when you clone VMs, but can be used in
any other kind of situation where you have problems with network cards,
say, duplicated cards for X reason.

Try to run this script I wrote:

::

    if [ $UID -ne 0 ] 
    then
        echo "Sorry, you have to run this script as root"
    else
        cat /etc/udev/rules.d/70-persistent-net.rules | grep PCI | cut -d' ' -f5 | cut -b 2-6 | uniq > /tmp/drivers
        for driver in $(cat /tmp/drivers); do
            rm -rf /etc/udev/rules.d/70-persistent-net.rules && echo "Removing 70-persistent-net.rules"
            rmmod $driver && echo "Removing $driver"
            modprobe $driver && echo "Loading $driver"
        done
        echo "Done."
        rm -rf /tmp/drivers
    fi

Tested under Debian and Fedora, but should work fine on other
distributions.

The code is also on my `github`_

.. _github: https://github.com/aesptux/bash-scripts/blob/master/reset-nic.sh
