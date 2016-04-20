# cassandra-opscenter-ansible
Ansible script to install Cassandra (DataStaxEnterprise) and OpsCenter to a set of servers

Usage:

If you have SSH keys already setup between Ansible server and the Cassandra hosts:
	ansible-playbook -vvv -i inventory-file cassandra-install.yml

If you DO NOT have SSH keys setup between Ansible server and the Cassandra hosts (not recommended):	
    ansible-playbook -vvv -i inventory-file cassandra-install.yml -u username -k 
	where, 
	username = remote cassandra machine user with sudo to root privileges
	
