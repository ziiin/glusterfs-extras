# Post-Snap xtime inconsistency correction.

## Issue:
* Geo-replication unable to sync few files to geo-rep slave for snapped
  volume.

## Root-Cause:
* During Barrier, file-operations other than rename and unlink were allowed.
  Among those file operations few actually hit the posix, are avilable in
  snapped volume but not recorded in changelogs of snapped volume.
* These Changelogs when reused using History-api used to miss these
  unrecorded changes.
* Further, Xsync crawl was expected to catch these modifications and sync them
  to slave. But marker translator being crash-inconsistent could not propagate
  xtime change till root. Hence missing the changes in xsync crawl too.

## Result:
* Inconsistency in Geo-replication session between snapped-master and
  its respective slave.

## Soluton:
* Modifications in changelog translator to barrier all but Data file-
  operations.
* Modifications in changelog has been made to detect probable files that
  would have suffered data-operations. And yet not propagated the xtime
  updation till root.
* Running the Script "parse_csnap.py" would update xtime till root.

## Usage:
* Start the snapped-volume. Before starting geo-replication session,
  run the provided python script on all bricks of the snapped-volume.
* Requires name of the snapped volume.
* $>> python parse_cnap.py @brick_path [@destination-path]
