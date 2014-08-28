killall -15 glusterfs glusterfsd glusterd 2>/dev/null || true;
echo "killed glusterfs, glusterfsd, glusterd \n"
killall -9 glusterfs glusterfsd glusterd 2>/dev/null || true;
rm -rf /var/lib/glusterd/* /etc/glusterd/* /usr/local/var/run/gluster/* /usr/local/var/log/glusterfs/* /usr/local/var/lib/misc/glusterfsd/* /var/log/glusterfs/* ;
echo "removed gluster related file"
rm -rf /export1/* /export2/*;
echo "clean brick"
rm -rf /mnt/volumes/*;
echo "cleaned mount points"
ps -ef | grep gsyncd | awk '{print $2}' | xargs kill -9
