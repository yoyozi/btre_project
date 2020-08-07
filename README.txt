######## DJANGO

Project is the site say
Apps are the additions you add to the project i.e : store

All projects are created in a virtual environment
To create a virtual environment

% python3 -m venv ./venv 

This creates a venv directory

To activate the environment
% source ./venv/bin/activate

Once activated it will use the version of python that activated 
the environment

% python --version                                                                   !2946
Python 3.8.5
(venv) 

So we dont need to run python3 or pip3 as long as we are in this 
env folder

To leave the environment we need to de-activate it

% deactivate
  
% python --version                                                                   !2948
Python 2.7.16

Activate and see what packages are installed
% source ./venv/bin/activate
% pip freeze

No packages  
% pip freeze                                                                         !2950
(venv)











