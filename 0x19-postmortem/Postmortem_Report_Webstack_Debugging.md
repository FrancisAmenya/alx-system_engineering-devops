# Postmortem Report

## 504 Error while accessing a given URL

<p align="center">
<img src="https://raw.githubusercontent.com/MitaliSengupta/alx-system_engineering-devops/master/0x19-postmortem/image.jpg" width=100% height=100% />
</p>

### Incident report for [504 error / Site Outage](https://github.com/FrancisAmenya/alx-system_engineering-devops/tree/master/0x17-web_stack_debugging_3)

#### Summary

On September 02nd, 2024 at midnight the server access went down resulting in 504 error for anyone trying to access a website. Background on the server being based on a LAMP stack.

#### Timeline

00:00 GMT - The website experienced a 500 error, preventing access for all users.

00:05 GMT - Verified that Apache and MySQL services were operational.

00:10 GMT - Conducted a background check, confirming that both the server and the database were functioning correctly, but the website still failed to load properly.

00:12 GMT - Restarted the Apache server. A subsequent curl test returned a status of 200 OK.

00:18 GMT - Began reviewing error logs to identify the source of the issue.

00:25 GMT - Checked /var/log and discovered that the Apache server was shutting down prematurely. Notably, there were no PHP error logs.

00:30 GMT - Examined php.ini settings and found that error logging was disabled. Enabled error logging.

00:32 GMT - Restarted the Apache server and monitored the PHP error logs.

00:36 GMT - Reviewed PHP error logs and found a mistyped file name causing incorrect loading and premature server shutdown.

00:38 GMT - Corrected the file name and restarted the Apache server.

00:40 GMT - The server is now running normally, and the website is loading correctly.

#### Root Cause and Resolution

The issue was traced to an incorrect file name in the wp-settings.php file. When attempting to curl the server, a 500 error was returned. Upon reviewing the error logs, it was found that no PHP error log files were being generated, and the default Apache error log provided little information about the premature server shutdown.

Upon discovering that PHP errors were not being logged, the engineer checked the PHP error log settings in the php.ini file and found that all error logging was disabled. After enabling error logging and restarting the Apache server, the PHP log revealed a missing file with a .phpp extension in the wp-settings.php file, indicating a typographical error.

This mistake likely affected other servers as well. The engineer used Puppet to deploy a quick fix, correcting the file extension across all affected servers. Restarting the servers resolved the issue, allowing the site to load correctly.

#### Corrective and Preventive Measures

Enable error logging on all servers and websites to quickly identify any issues that arise.
Test all servers and websites locally before deploying to a multi-server environment. This helps catch and correct errors before going live, reducing downtime and minimizing the need for fixes after deployment.
