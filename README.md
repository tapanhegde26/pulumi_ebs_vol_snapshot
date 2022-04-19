# pulumi_ebs_vol_snapshot

This pulumi .py script is being written to do following tasks

* read all the EBS volumes attached to source ec2-instance
* take snapshot of all EBS volumes attached to source ec2-instance
* create cloned EBS volumes from created snapshots
* attach cloned EBS volumes to target instance

User Input : Source EC2 Instance-ID , Target EC2 Instance-ID, Availabilty Zone

Give this input in __main__.py file

Pre-requistite
--------------
* Pulumi should be installed in your machine
    Reference Link : [https://www.pulumi.com/docs/get-started/aws/begin/]
* AWS account should be configured
* New pulumi project should be created. Ref :- https://www.pulumi.com/docs/get-started/aws/create-project/
* Review created project and make sure all necessary files are generated.


How-to-run
----------
* once you have your 'Pulumi.yaml' , 'Pulumi.dev.yaml' and '__main__.py' in place (same dir), copy paste content of __main__.py of this repo into your __main__.py file. Ref -> https://www.pulumi.com/docs/get-started/aws/review-project/
* Next run 'pulumi up' command
