
## Add-on dobump for Splunk

**Usage**

This is a Add-on for Splunk to provide a custom search command called '| dobump'
to reload application server cache. This is need if you update Javascript or CSS related content in Dashboards.

This should give you a possibility to automate cache refreshing in a deployment pipeline or development environment. 

**Testing and reproducing**

You'll find a "testcss" app in the subfolder of the app. 
- Copy this app to \$SPLUNK_HOME\$/etc/apps and restart. 
- Open the testcss dashboard located in the app.. 
- Now update the file
appserver/static/show_rule_details.js file in the app in line 17:

        ``document.getElementById("outputName").innerHTML = "version5";``

and output a new string.. 
- do a reload of the dashboard and notice, that appserver cache will still deliver javascript "version5".

- run " | dodump", reload the dashboard and notice the new string.. 

**Support**

This is an open source project, no support provided, but you can ask questions
on answers.splunk.com and I will most likely answer it.
Github repository: https://github.com/schose/ta-dobump

**Links**

- https://answers.splunk.com/answers/31289/can-i-issue-a-bump-from-the-command-line.html
- https://docs.splunk.com/Documentation/Splunk/7.3.1/AdvancedDev/CustomizationOptions
-  https://answers.splunk.com/answers/315160/how-to-update-splunk-after-javascript-changes-with.html
- https://answers.splunk.com/answers/390115/how-do-you-programmatically-bump-a-search-head.html
