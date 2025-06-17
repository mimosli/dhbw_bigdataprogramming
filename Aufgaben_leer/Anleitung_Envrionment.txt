# Kafka Environment Setup

This manual is written for Windows. Last Test: 11.06.2020

# Setup a VM

This is here is only a summary. Full description: https://github.com/TrivadisPF/platys/blob/master/vagrant/Platys_with_Vagrant.md

- Install Vagrant https://www.vagrantup.com/downloads.html
- In command line install `vagrant-docker-compose`: `vagrant plugin install vagrant-docker-compose`
- Create a new folder and copy the [`Vagrantfile`](https://raw.githubusercontent.com/TrivadisPF/platys/master/vagrant/Vagrantfile) into this folder.
- Change directory to this folder
- Run `vagrant up`. This takes a while
- Once done: connect to your vm with `vagrant ssh`

Hint:

- To suspend: `vagrant suspend`
- To restart: `vagrant resume`

# Setup Kafka and Docker environment

- Connect to your previously created vm with `vagrant ssh`
- `git clone https://github.com/gschmutz/kafka-workshop.git`
- `cd kafka-workshop/01-environment/docker/`
- `docker-compose up -d` (this takes quite a while)
- `docker ps` should show several docker containers

# Common commands used with Kafka and Docker

- Connect to a docker container 'kafka-1' and open a command line: `docker exec -ti kafka-1 bash`
- Create a new kafka topic 'test-topic': `kafka-topics --create --if-not-exists --zookeeper zookeeper-1:2181 --topic test-topic --partitions 6 --replication-factor 2`
- To test consume your 'test-topic' on console: `kafka-console-consumer --bootstrap-server kafka-1:19092,kafka-2:19093 --topic test-topic`
- produce messages to 'test-topic': `kafka-console-producer --broker-list kafka-1:19092,kafka-2:19093 --topic test-topic`

# Useful Links on your host machine

- Jupyter: http://127.0.0.1:28888 (login token: abc123!)
- AKHQ: http://127.0.0.1:28107
- Kafka Topics UI: http://127.0.0.1:28141
