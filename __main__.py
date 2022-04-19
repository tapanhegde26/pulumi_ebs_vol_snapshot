"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws
import datetime;

ct = datetime.datetime.now()
ts = ct.timestamp()
foo = aws.ec2.get_instance(instance_id="i-00590118d16b5ed8f")
foo2 = aws.ec2.get_instance(instance_id="i-055c551c95629c394")

ebslist = foo.ebs_block_devices
snapshot_name = "vol-snapshots"+"-"+str(ts)
cloned_vol_name = "cloned_vol"+"-"+str(ts)
vol_attachment = "vol_attachment"+"-"+str(ts)
for i in ebslist:
    print(i.volume_id)
    foo_snapshot = aws.ebs.Snapshot(snapshot_name+str(i.volume_id),volume_id=i.volume_id)
    foo_cloned_volume = aws.ebs.Volume(cloned_vol_name+str(i.volume_id),availability_zone="us-east-1b",snapshot_id=foo_snapshot.id)
    cloned_vol_attachment = aws.ec2.VolumeAttachment(vol_attachment+str(i.volume_id),device_name=i.device_name,volume_id=foo_cloned_volume.id,instance_id=foo2.instance_id)

