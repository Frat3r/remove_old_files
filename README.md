# remove_old_files
This script may be used to delete files with modification date older than specified in _config.yml_.
## config.yml
* **path** - path to folder containing files to be deleted
* **file_regex** - regular expression which file name should satisfy
* **days_back** - files older than specified number of days will be deleted
* **weeks_back** - files older than specified number of weeks will be deleted
* **months_back** - files older than specified number of months will be deleted
* **years_back** - files older than specified number of years will be deleted

File will be deleted only if it satisfy **file_regex** and its modification date is older than sum of number of days, weeks, months and years from **days_back**/**weeks_back**/**months_back**/**years_back**. 
Also log file will be created in folder _logs_ containing group of deleted files, modification date and path to that file.

## Use in SQL Server job
To use _remove_old_files.exe_ in SQL Server job you should modify **WorkingDirectory** and **Executable** from _SSISRunRemove.dtsx_ in such a way that **WorkingDirectory** leads to a folder containing _config.yml_ and **Executable** points to the _remove_old_files.exe_.  
In SQL Server job you should create new step with type _SQL Server Integration Services Package_, _Package source_ _File system_ and _Package_ path leading to _SSISRunRemove.dtsx_.
