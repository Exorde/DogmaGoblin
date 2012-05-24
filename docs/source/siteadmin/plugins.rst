=========
 Plugins
=========

GNU MediaGoblin supports plugins that allow you to augment MediaGoblin's
behavior.

This chapter covers discovering, installing, configuring and removing
plugins.


Discovering plugins
===================

MediaGoblin comes with core plugins. Core plugins are located in the
``mediagoblin.plugins`` module of the MediaGoblin code. Because they
come with MediaGoblin, you don't have to install them, but you do have
to add them to your config file if you're interested in using them.

You can also write your own plugins and additionally find plugins
elsewhere on the Internet. Once you find a plugin you like, you need
to first install it, then add it to your configuration.

.. todo: how do you find plugins on the internet?


Installing plugins
==================

Core plugins
------------

MediaGoblin core plugins don't need to be installed because they come
with MediaGoblin. Further, when you upgrade MediaGoblin, you will also
get updates to the core plugins.


Other plugins
-------------

If the plugin is available on the `Python Package Index
<http://pypi.python.org/pypi>`_, then you can install the plugin with pip::

    pip install <plugin-name>

For example, if we wanted to install the plugin named
"mediagoblin-restrictfive", we would do::

    pip install mediagoblin-restrictfive

.. Note::

   If you're using a virtual environment, make sure to activate the
   virtual environment before installing with pip. Otherwise the
   plugin may get installed in a different environment than the one
   MediaGoblin is installed in.

Once you've installed the plugin software, you need to tell
MediaGoblin that this is a plugin you want MediaGoblin to use. To do
that, you edit the ``mediagoblin.ini`` file and add the plugin as a
subsection of the plugin section.

For example, say the "mediagoblin-restrictfive" plugin had the Python
package path ``restrictfive``, then you would add ``restrictfive`` to
the ``plugins`` section as a subsection::

    [plugins]

    [[restrictfive]]


Configuring plugins
===================

Configuration for a plugin goes in the subsection for that plugin. Core
plugins are documented in the administration guide. Other plugins
should come with documentation that tells you how to configure them.

Example 1: Core MediaGoblin plugin

If you wanted to use the core MediaGoblin flatpages plugin, the module
for that is ``mediagoblin.plugins.flatpages`` and you would add that
to your ``.ini`` file like this::

    [plugins]

    [[mediagoblin.plugins.flatpages]]
    # configuration for flatpages plugin here!
    directory = /srv/mediagoblin/flatpages

Example 2: Plugin that is not a core MediaGoblin plugin

If you installed a hypothetical restrictfive plugin which is in the
module ``restrictfive``, your ``.ini`` file might look like this (with
comments making the bits clearer)::

    [plugins]

    [[restrictfive]]
    # configuration for restrictfive here!

Check the plugin's documentation for what configuration options are
available.


Removing plugins
================

To remove a plugin, use ``pip uninstall``. For example::

    pip uninstall mediagoblin-restrictfive

.. Note::

   If you're using a virtual environment, make sure to activate the
   virtual environment before uninstalling with pip. Otherwise the
   plugin may get installed in a different environment.


Upgrading plugins
=================

Core plugins
------------

Core plugins get upgraded automatically when you upgrade MediaGoblin
because they come with MediaGoblin.


Other plugins
-------------

For plugins that you install with pip, you can upgrade them with pip::

    pip install -U <plugin-name>

The ``-U`` tells pip to upgrade the package.