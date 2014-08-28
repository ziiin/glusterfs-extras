echo "start"
cd /home/ajha/git/g_d/rhs-glusterfs
./autogen.sh && ./configure --enable-debug CFLAGS='-ggdb -O0' && make -j4
make uninstall
make clean
make dist clean
make install && glusterd
mkdir -p /export1/rep_v1/b1
mkdir -p /export1/v1/b1
printf "compiled and bricks created\n"
printf "create master volume (y/n)\t"
read var1
if [ "x$var1" = "xy" ] ;then
	gluster volume create v1 geo:/export1/v1/b1/ force
	gluster volume start v1
else
	exit 0
fi
printf "create slave volume (y/n)\t"
read var2
if [ "x$var2" = "xy" ] ;then
	gluster volume create rep_v1 geo:/export1/rep_v1/b1/ force
	gluster volume start rep_v1
else
	exit 0
fi
printf "volume created\n"
cp /home/ajha/git/g_d/rhs-glusterfs/extras/hook-scripts/S56glusterd-geo-rep-create-post.sh /var/lib/glusterd/hooks/1/gsync-create/post/
gluster system:: execute gsec_create
printf "create geo session (y/n)\t"
read var3
if [ "x$var3" = "xy" ] ;then
	gluster volume geo-replication v1 geo::rep_v1 create push-pem force
else
	exit 0
fi
echo "geo-rep create, please start using \"gluster volume geo-replication v1 geo::rep_v1 start\""
