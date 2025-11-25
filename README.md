# Cost-Optimization-AWS

Cost Optimization in AWS – EBS Snapshot Cleanup with Lambda

🚀 Hands-On AWS Cost Optimization with Lambda & Python!
In my journey to strengthen real-world DevOps skills, I implemented a serverless solution to automatically delete unused EBS snapshots — a small but powerful way to trim down cloud costs.

📌 Problem:
AWS charges for every EBS snapshot, even those no longer linked to running instances. Over time, these “orphaned” snapshots quietly rack up unnecessary charges. 

🔧Solution: Snapshot Cleanup Lambda
I built an AWS Lambda function (Python + boto3) that runs periodically and:
 ✅ Lists all snapshots owned by the account
 ✅ Cross-references active EC2 volumes
 ✅ Deletes orphaned snapshots not associated with any instance
 ✅ Returns a summary of deleted resources

This simple automation helps eliminate wasteful storage costs in a clean, scalable way.

🧰 Here are other proven strategies to optimize the cost:
 🔹 EC2 Right Sizing – Stop or downsize underutilized instances
 🔹 S3 Lifecycle Policies – Auto-move infrequent data to Glacier
 🔹 AWS Compute Optimizer – AI-based recommendations
 🔹 Use Spot Instances – For non-critical workloads
 🔹 EBS Volume Cleanup – Delete unattached volumes
 🔹 CloudWatch Log Retention – Set shorter retention where needed
 🔹 Trusted Advisor – Regularly review cost optimization checks

Why this matters: In the real world, cloud bills can grow silently. Knowing how to monitor and control cost at scale is a vital DevOps & CloudOps skill.

Note: Attached the necessary IAM policy to allow:
