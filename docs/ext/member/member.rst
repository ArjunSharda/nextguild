The Member and User Classes
=============================

This document provides information for all the information you can receive
from a member-related classes.

UserSummary
-------------

Provides basic information about a user.

+-----------+------+---------------------------------------------------------------------------+
| Attribute | Type | Description                                                               |
+===========+======+===========================================================================+
| id        | str  | Guilded user UUID.                                                        |
+-----------+------+---------------------------------------------------------------------------+
| type      | str  | Could be 'user' or 'bot'.                                                 |
+-----------+------+---------------------------------------------------------------------------+
| name      | str  | User's name. (Not display name!)                                          |
+-----------+------+---------------------------------------------------------------------------+
| avatar    | str  | URL-like string leading to user's avatar. It's '' if user has no avatar.  |
+-----------+------+---------------------------------------------------------------------------+
| is_bot    | bool | Returns 'True' if user is bot otherwise 'False'.                          |
+-----------+------+---------------------------------------------------------------------------+

User
------

Inherits from UserSummary. Provides all information about a user.

+------------+-------------------+--------------------------------------------------------------------------+
| Attribute  | Type              | Description                                                              |
+============+===================+==========================================================================+
| banner     | str               | URL-like string leading to user's banner. It's '' if user has no banner. |
+------------+-------------------+--------------------------------------------------------------------------+
| created_at | datetime.datetime | User's profile creation date.                                            |
+------------+-------------------+--------------------------------------------------------------------------+

ServerMemberSummary
---------------------

Provides basic global and server-specific information.

+-----------+------------------------------+------------------------------+
| Attribute | Type                         | Description                  |
+===========+==============================+==============================+
| user      | nextguild.member.UserSummary | Basic global information.    |
+-----------+------------------------------+------------------------------+
| role_ids  | list[str]                    | List of member's roles' ids. |
+-----------+------------------------------+------------------------------+

ServerMember
--------------

Inherits from ServerMemberSummary. Provides complete global and server-specific information.

.. warning::
    'user' field has different type here than in inherited class.

+-------------+---------------------------+--------------------------------------------------------------+
| Attribute    | Type                     | Description                                                  |
+==============+==========================+==============================================================+
| user         | nextguild.member.User    | Complete global information.                                 |
+--------------+--------------------------+--------------------------------------------------------------+
| nickname     | str                      | Nickname in current server. It's '' if user has no nickname. |
+--------------+--------------------------+--------------------------------------------------------------+
| joined_at    | datetime.datetime        | Member's join date.                                          |
+--------------+--------------------------+--------------------------------------------------------------+
| is_owner     | bool                     | 'True' if member is the owner otherwise 'False'.             |
+--------------+--------------------------+--------------------------------------------------------------+
| display_name | str                      | Returns nickname if exists otherwise 'user.name'.            |
+--------------+--------------------------+--------------------------------------------------------------+

