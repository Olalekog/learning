# EC2 Start / Stop / Status — SSM Automation Document

`ec2-start-stop-status.yaml` is a single SSM Automation document that checks the
status of an EC2 instance, starts it, or stops it, based on an `Action`
parameter. After a Start or Stop, it always finishes by fetching current
status, so you get state back regardless of which action you ran.

## Parameters

| Name | Required | Values | Notes |
|---|---|---|---|
| `InstanceId` | Yes | e.g. `i-0123456789abcdef0` | Instance to manage |
| `Action` | Yes | `Status`, `Start`, `Stop` | What to do |
| `AutomationAssumeRole` | No | Role ARN | Leave blank to run as your own IAM identity |

## 1. Create the document in AWS

```bash
aws ssm create-document \
  --name "EC2-Start-Stop-Status" \
  --document-type "Automation" \
  --document-format YAML \
  --content file://ec2-start-stop-status.yaml
```

To update it later (creates a new version):

```bash
aws ssm update-document \
  --name "EC2-Start-Stop-Status" \
  --document-version '$LATEST' \
  --document-format YAML \
  --content file://ec2-start-stop-status.yaml
```

## 2. Run it

Check status:

```bash
aws ssm start-automation-execution \
  --document-name "EC2-Start-Stop-Status" \
  --parameters InstanceId=i-0123456789abcdef0,Action=Status
```

Start the instance:

```bash
aws ssm start-automation-execution \
  --document-name "EC2-Start-Stop-Status" \
  --parameters InstanceId=i-0123456789abcdef0,Action=Start
```

Stop the instance:

```bash
aws ssm start-automation-execution \
  --document-name "EC2-Start-Stop-Status" \
  --parameters InstanceId=i-0123456789abcdef0,Action=Stop
```

Each call returns an `AutomationExecutionId`.

## 3. Check execution status / output

```bash
aws ssm get-automation-execution \
  --automation-execution-id <execution-id>
```

The instance state, type, and IPs are under
`AutomationExecution.Outputs` (e.g. `GetInstanceStatus.InstanceState`).

## Required IAM permissions

Whoever (or whatever role) runs this automation needs:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssm:StartAutomationExecution",
        "ssm:GetAutomationExecution",
        "ssm:StopAutomationExecution"
      ],
      "Resource": "*"
    }
  ]
}
```

If you set `AutomationAssumeRole`, that role needs the `ec2:*Instances` actions
above plus a trust policy allowing `ssm.amazonaws.com` to assume it.

## How it works

1. `BranchOnAction` (`aws:branch`) routes to `StartInstance`, `StopInstance`,
   or falls through to `GetInstanceStatus` when `Action` is `Status`.
2. `StartInstance` / `StopInstance` (`aws:changeInstanceState`) — the same
   built-in action AWS's own `AWS-StartEC2Instance` / `AWS-StopEC2Instance`
   documents use; it waits for the instance to reach the desired state.
3. `GetInstanceStatus` (`aws:executeAwsApi`) calls `DescribeInstances` and
   extracts state, instance type, and IPs as outputs.
