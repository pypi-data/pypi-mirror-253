# BlazeBase: A replacement to Pyrebase written in modern python

## Warning

Currently in **very very very** early developpement... Not much has been added yet...

## Config

**Initial Setup:**

```python

from BlazeBase import BlazeBase

config = {
    "serviceAccount": "Dict with service account information or the path to the json file",
    # Optional arguments below, omit if not useful
    "databaseURL": "Url to the firebase database", 
    "storageBucket": "Url to storagebucket",
    "projectId": "Project Id",
    "databaseAuthVariableOverride": "Auth variable override",
    "serviceAccountId": "Service account Id",
    "httpTimeout": "Time in seconds"
}


blaze = BlazeBase(config)

```
