"""An AWS Python Pulumi program"""

import pulumi_aws as aws
import datetime
import logging

logger = logging.getLogger(__name__)
ct = datetime.datetime.now()
ts = ct.timestamp()
source_instance = aws.ec2.get_instance(instance_id="i-07489eeacaa7bdf12")
target_instance = aws.ec2.get_instance(instance_id="i-0a7667569757abf84")

ebslist = source_instance.ebs_block_devices
snapshot_name = "vol_snapshots"+"-"+str(ts)
cloned_vol_name = "cloned_vol"+"-"+str(ts)
vol_attachment = "vol_attachment"+"-"+str(ts)
try:
    for i in ebslist:
        logger.info("Loop over EBS list to get volume-id and device_name")
        try:
         source_snapshot = aws.ebs.Snapshot(snapshot_name+str(i.volume_id),volume_id=i.volume_id)
        except RuntimeError:
            logger.exception("Snapshot creation failed")
            raise
        try:
            source_cloned_volume = aws.ebs.Volume(cloned_vol_name+str(i.volume_id),availability_zone="us-east-1c",snapshot_id=source_snapshot.id)
        except RuntimeError:
            logger.exception("Volume creation from snapshots failed")
            raise
        try:
            cloned_vol_attachment = aws.ec2.VolumeAttachment(vol_attachment+str(i.volume_id),device_name=i.device_name,volume_id=source_cloned_volume.id,instance_id=target_instance.instance_id)
        except RuntimeError:
            logger.exception("Volume attachment to target instance failed")
            raise
except RuntimeError:
    logger.exception("Looping through EBS block list failed")
    raise


