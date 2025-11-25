
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Get all snapshots owned by the account
    snapshots_response = ec2.describe_snapshots(OwnerIds=['self'])
    snapshots = snapshots_response['Snapshots']
    
    # Get all active volumes (in-use or available)
    volumes_response = ec2.describe_volumes(
        Filters=[{'Name': 'status', 'Values': ['in-use', 'available']}]
    )
    active_volume_ids = {vol['VolumeId'] for vol in volumes_response['Volumes']}
    
    deleted_snapshots = []
    
    # Iterate through snapshots
    for snapshot in snapshots:
        snapshot_id = snapshot.get('SnapshotId')
        volume_id = snapshot.get('VolumeId')
        
        if volume_id not in active_volume_ids:
            try:
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                deleted_snapshots.append(snapshot_id)
                print(f"Deleted snapshot: {snapshot_id}")
            except Exception as e:
                print(f"Error deleting snapshot {snapshot_id}: {str(e)}")
        else:
            print(f"Skipped: Snapshot {snapshot_id} is associated with active volume {volume_id}.")
    
    return {
        'statusCode': 200,
        'body': f"Deleted {len(deleted_snapshots)} orphaned snapshots: {deleted_snapshots}"
    }
