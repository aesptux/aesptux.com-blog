Active Directory - Concepts.
############################
:date: 2011-10-07 00:43
:author: aesptux
:category: Server 2003, Windows
:tags: 2003, active directory, concepts, domain, forest, objects, organizational, ou, server, tree, trusts, unit, Windows
:slug: active-directory-concepts

Active Directory is the central repository of information on a Windows
2003 based network. It stores information about all resources that are
used on the network, like user and group accounts, shared folders,
computers, printers, etc.

Active Directory can be used to locate this resources quickly so that
Administrators can create, configure, delete and maintain them as
needed.

Logical structure of Active Directory
-------------------------------------

.. raw:: html

   <ul>

.. raw:: html

   <li>

**Forest**

.. raw:: html

   </li>

-  A forest is a collection of domain trees linked together at their
   roots by transitive trusts

.. raw:: html

   <li>

**Tree**

.. raw:: html

   </li>

-  Also called a domain tree, a hierarchical grouping of domains
   beggining with a root domain and branching out to child domains. Must
   have a contiguous DNS namespace

.. raw:: html

   <li>

**Domain**

.. raw:: html

   </li>

-  The primary administrative boundary for WS2003 networks. Domains are
   named using DNS, and a tree consists of one or more domains
   hierarchically joined by transitive trusts.

.. raw:: html

   <li>

**Organizational Unit (OU)**

.. raw:: html

   </li>

-  Logical containers you can use to group objects in a domain for
   security and administration purposes. For example you can reflect
   your company's geographical, organizational or administrative
   structure.

.. raw:: html

   <li>

**Object**

.. raw:: html

   </li>

-  A user, group, computer, printer, shared folder or anything else
   which can be contained within a domain or OU.

.. raw:: html

   <li>

**Trust**

.. raw:: html

   </li>

-  Secure communications between domains, domains trees, or forests

.. raw:: html

   </ul>

 
