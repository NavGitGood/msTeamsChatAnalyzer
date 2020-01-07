# msTeamsChatAnalyzer
Steps to run:
1. git clone https://github.com/NavGitGood/msTeamsChatAnalyzer.git
2. cd msTeamsChatAnalyzer
3. Create a virtual environment python -m venv <name_of_virtual_environment>
4. Activate virtual environment (powershell) .\<name_of_virtual_environment>\Scripts\Activate.ps1
5. pip install -r requirements.txt
6. run using command python .\run.py
7. Use following options in interactive session to generate required report:
    --> group : to generate group report
    --> individual firstname lastname : to generate individual report 

PDFs will be generated in output folder:
1. Group_Report.pdf --> group report
2. <firstname lastname>.pdf --> individual report

<firstname lastname> can have any one of following values (from sample data):
1. User 7
2. User 6
3. Adele Vance
4. Joe Bloggs
5. Juan Perez
6. John Doe
7. Miriam Graham
8. Jane Doe
9. User 5
