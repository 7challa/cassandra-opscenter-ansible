This folder (Utilities) consists of scripts that are frequently used 


To getcompaction throughput across the cluster:
ansible all -i inventory/test_inventory_file.txt --sudo --sudo-user=cassandra -m shell -a "export JAVA_HOME=/opt/app/jdk1.8.0_65 && /opt/app/dse/bin/nodetool getcompactionthroughput"

To getstreamthroughput 
ansible all -i inventory/test_inventory_file.txt --sudo --sudo-user=cassandra -m shell -a "export JAVA_HOME=/opt/app/jdk1.8.0_65 && /opt/app/dse/bin/nodetool getstreamthroughput"


To setcompaction throughput to 64 across the cluster:
ansible all -i inventory/test_inventory_file.txt --sudo --sudo-user=cassandra -m shell -a "export JAVA_HOME=/opt/app/jdk1.8.0_65 && /opt/app/dse/bin/nodetool setcompactionthroughput 64"

To setstreamthroughput to 400Mb/s
ansible all -i inventory/test_inventory_file.txt --sudo --sudo-user=cassandra -m shell -a "export JAVA_HOME=/opt/app/jdk1.8.0_65 && /opt/app/dse/bin/nodetool setstreamthroughput 400"
