# AirBnB clone - The console  
The project revolves around creating an innovative Airbnb-like platform designed to provide a streamlined and efficient property rental experience. Its core components include:  
  
1. Data Model Creation  
2. Console Interfacee  
  
## Clone the repository:  
$ git clone https://github.com/Lamia1406/AirBnB_clone.git  
$ cd AirBnB_clone  
## Start the application:  
- interactive mode  
$ ./console.py  
(hbnb) help  
` Documented commands (type help <topic>):`  
========================================  
EOF  help  quit  
(hbnb)  
(hbnb)  
(hbnb) quit  
$  
  
- non_interactive mode  
$ echo "help" | ./console.py    
(hbnb)     
` Documented commands (type help <topic>):`  
========================================  
EOF  help  quit  
(hbnb)  
$  
$ cat test_help  
help  
$  
$ cat test_help | ./console.py  
(hbnb)  
` Documented commands (type help <topic>):`  
========================================  
EOF  help  quit  
(hbnb)  
$

## Unittests for interactive mode:
it was tested with python3 -m unittest discover tests

##Unittests for non interactive mode:
Was tested with echo "python3 -m unittest discover tests" | bash
