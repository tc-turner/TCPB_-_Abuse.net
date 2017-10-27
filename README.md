# Release Notes


# Disclaimer
```
This is not an official TC app and will not be supported.  This is for demo purposes only.  Use only as a learning tool.
```

Full documentation of the TC Platform API and SDKs can be found at [ThreatConnect Developer Documentation](https://docs.threatconnect.com/en/latest/)

# TCPB_-_AbuseNet
This is a simple demo app for TC PlayBooks that will query [abuse.net](https://abuse.net).

## Input Parameters
* Host: Host to query abuse.net for


## Output Parameters
* abuse.debug: String containing error messages
* abuse.contacts: StringArray containing abuse contacts

## Build
`pip install tcex`
`git clone https://github.com/tc-turner/TCPB_-_Abuse.net.git`
`cd TCPB_-_Abuse.net`
`tclib --config none`
`tcpackage --bundle`

This will build TCPB_-_AbuseNet_v0.0.tcx in the target directory. Install this app in your ThreatConnect instance.

## 0.0.1
+ Initial release
