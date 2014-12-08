##Creation of Geo-Rep with a non-root non-mountbroker priviledged user

### Requires:
* Priviledged user say u1 with access to gluster commands.
* Initial password-less SSH connection with a different public key, say at path1.

### How to run:
* Use command:
> gluster volume geo-repliaction master-vol slave-host::slave-vol create
> push-pem geomgmt_user pem-key-path
* Run the set_geo_rep_pem_keys.sh with root and geomgmt_user as argument.
> ./set_geo_rep_pem_keys.sh root geomgmt_user
