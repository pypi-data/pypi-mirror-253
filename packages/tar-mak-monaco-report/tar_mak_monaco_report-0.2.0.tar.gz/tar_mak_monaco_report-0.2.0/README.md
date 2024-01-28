# tar_mak_monaco_report

This is a simple package that can be used to create a report on the drivers of Formula 1 - Monaco 2018 Racing.
Нhe package has a number of arguments that will help you get the information you need.

-f or --files FILE - an argument that requires specifying the path to the folder which contains the required files(abbreviations.txt, end.log, start.log)

--asc - an argument that follow after --files to specify ascending order.

--desc - an argument that follow after --files to specify descending order.

--driver "driver_name" - an argument that follow after --files to get information about specific raser.


Output of the package is ordered by places racers, their time and cars.

Example: report_mon -f " Folder_path " --desc

In this case In this case, the package will show full report in descending order. If remove --desc, order will be ascending(by default)

Example 2: report_mon --files " Folder_path " --driver "driver_name"

In this case, the package will show information about certain racer