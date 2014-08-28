import socket
import os

def setupPasswordlessSSH ():
    ''' sets up passwordless SSH from root to root user of self IP '''
    hostFqdn = socket.getfqdn()
    # ssh -o "StrictHostKeyChecking no" user@host
    try:
        os.stat("~/.ssh/id_rsa.pub")
    except OSError:
        ssh_keygen_cmd = 'ssh-keygen -b 4096 -t rsa -f ~/.ssh/id_rsa -P "glusterfs"'
        print "Executing : ", ssh_keygen_cmd
    copy_id_cmd = "ssh-copy-id root@" + hostFqdn
    print "Executing : ",copy_id_cmd
    os.system (copy_id_cmd)
    ssh_cmd = 'ssh -o "StrictHostKeyChecking no" root@' + hostFqdn
    print "Executing : ", ssh_cmd
    # run ssh_cmd

setupPasswordlessSSH()

