#!/bin/bash
set -u

TIMEOUT=180

getpid() {
 RUNNING_APP=$(ps -C java -o pid,cmd|grep org.apache.cassandra.service.CassandraDaemon || echo "")
 if [ "${RUNNING_APP}" = "" ]
 then
   PID=0
 else
   set $RUNNING_APP
   PID=$1
 fi
}

getpid
if [ "${PID}" -ne "0" ] ; then
  echo "Shutting down Cassandra server"
  timeout 180 /opt/app/cassandra/scripts/stopCassandra.sh -g || true
  echo "Verifying cassandra process has ended."
  getpid
  TIMEOUT=180

  while [ $TIMEOUT -gt 0 ]; do
    getpid
    if  [ "${PID}" -eq "0" ] ; then
      echo "Cassandra has been shutdown."
      break
    fi
    sleep 1
    TIMEOUT=$(($TIMEOUT - 1))
  done
  
  getpid
  if [ "${PID}" -ne "0" ] ; then
    echo "Force KILLING Cassandra"
    kill -9 ${PID}
  fi

  getpid
  if [ "${PID}" -eq "0" ] ; then
    echo "Ensured - Cassandra has been shutdown."
  fi
fi
exit 0
