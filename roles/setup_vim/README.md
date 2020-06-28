Role Name
=========

setup_vim

Description
-----------

Install and setup vim in debain based system. It installs 'vim_plug'(plugin manager) using the code in ~/.vimrc file from 
https://github.com/junegunn/vim-plug/wiki/tips#automatic-installation


Requirements
------------

None

Role Variables
--------------
None

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: setup_vim }

Post Role instruction:
----------------------
Install plugins as instructed in https://github.com/junegunn/vim-plug/wiki/tutorial#installing-plugins

    - Run 				    :source ~/.vimrc to load vimrc file
    - Install plugin		:PlugInstall
    - Update plugin 		:PlugUpdate
    - Check plugin diff 	:PlugDiff


Removing plugins

    - Delete or comment out Plug commands for the plugins you want to remove.
    - Reload vimrc (:source ~/.vimrc) or restart Vim
    - Run :PlugClean. It will detect and remove undeclared plugins.


License
-------

BSD

Author Information
------------------

Mohammad Badruzzama (shakib37@ymail.com)
