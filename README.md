Item Catalog

How do I run this?
1. Setup: Configure VM & Database
Step 1: Download and install Vagrant and VirtualBox. We’ll need these tools to setup and manage the Virtual Machine (VM).

I used version 2.2.4 of Vagrant.

Step 2: Once you've cloned this project from https://github.com/udacity/fullstack-nanodegree-vm, open the terminal and then run the following commands:

# Install & Configure VM
cd /path/to/vagrant
vagrant up

# Log into machine
vagrant ssh

# Log out of machine
# <Ctrl + D>

# Destroy machine once done
vagrant destroy

2. Run the website
Open the terminal. Then, run the following commands:

# Open shared folder
cd /vagrant/catalog 

# Run the program
python catalogApp.py