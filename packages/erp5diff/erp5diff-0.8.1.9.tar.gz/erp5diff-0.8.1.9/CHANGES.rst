0.8.1.8 (2022/09/14)
--------------------
 * Support python3

0.8.1.7 (2015/04/23)
--------------------
 * Fix a regression that was introduced in 0.8.1.6.

0.8.1.6 (2015/04/23)
--------------------
 * Disable _removeStrictEqualsSubNodeList that can make a wrong result

0.8.1.5 (2011/08/08)
--------------------
 * Fix rst syntax
 * Improve Handling of mixed content

0.8.1.4 (2011/08/05)
--------------------
 * Tail text nodes was not detected (...<node/>blablabla...)
 * fix import issue of main() function

0.8.1.3 (2011/01/25)
--------------------
 * add long_description, improve README
 * add missing namespace declaration of egg

0.8.1.2 (2011/01/25)
--------------------
 * [fix] installation of egg

0.8.1.1 (2011/01/25)
--------------------
 * [Fix] position starts to 1 [Nicolas Delaby]

version 0.8.1 Nicolas Delaby
============================
Bug Fix
--------
* Some nodes stay orphans if they are replaced by another one and followed
  by a modification (test 30)
* Exclude comments or processing instruction as sibling node

version 0.8 Nicolas Delaby
==========================
Features
--------
* Include 'gid' in attributes allowed to build an xpath expression
  with a unique identifier.
* Use better algorithm to compare two xml nodes (faster).

Bug Fix
-------
* In node comparaison discard text nodes with only withe-spaces.
* Fix relative calculation of position for xupdate:insert-before nodes
* Add namespace declaration on xupdate nodes which are using
  prefix in builded xpath expression.


version 0.7 Nicolas Delaby
==========================
Bug fix
-------
* Nodes whose position change were discarded.
* Declare namespaces used in xpath expression on xupdate output.

version 0.6 Nicolas Delaby
==========================
Bug Fix
-------
* Fix generated xpath expression, the root element was missing.


version 0.5 Nicolas Delaby
==========================
Features
--------

* Add support of namespaces
* Support xupdate:insert-after

version 0.4 Nicolas Delaby
==========================
Features
--------
* Change output of xupdate:append by adding Implied attribute child


version 0.3 Nicolas Delaby
==========================
Bug Fix
-------
* Append position in xpath expression when value of id attribute is not unique regarding is sibling


version 0.2 Nicolas Delaby
==========================
Bug Fix
-------
* Position in xpath starts from 1


version 0.1 Tatuya Kamada
=========================
Features
--------
* ERP5diff implemented with ElemenTree (lxml)


version 0 Yoshinori Okuji
=========================

* initial ERP5diff with DOM API (minidom)
