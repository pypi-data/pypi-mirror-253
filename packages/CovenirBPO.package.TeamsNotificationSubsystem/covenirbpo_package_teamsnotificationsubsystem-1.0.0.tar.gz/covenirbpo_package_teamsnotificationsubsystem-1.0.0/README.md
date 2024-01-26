# TeamsNotificationSubsystem

## Purpose
This package allows for the transmission of teams messages. 

## Prerequisites
```powershell
python -m pip install requests
```

## Install
```powershell
python -m pip install CovenirBPO.package.TeamsNotificationSubsystem
```

## Set your Teams Webhook Environment Variable
**NOTE: This environment variable is required**
|Name|Value|
|:--|:--|
|TEAMS_WEBHOOK|Your webhook|

## Usage
```python
# Import the package
from TeamsNotificationSubsystem import TeamsNotifier

# Create the notifier object
notifier = TeamsNotifier.TeamsNotifier()

# Choose the message type that you would like to send
notifier.send_error_message('title', 'message')
notifier.send_warning_message('title', 'message')
notifier.send_info_message('title', 'message')
```
