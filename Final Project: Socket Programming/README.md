                         Client–Server Secure Educational Portal (Sierra Leone Civil War)



# Project Overview

This project is a Python-based client-server system designed to store and share encrypted historical documents about the Sierra Leone Civil War (1991–2002). The system simulates a secure educational portal where students and educators can interact with historical content in a controlled and authenticated environment.

The system uses socket programming for communication, encryption/decryption for secure data transfer, and role-based authentication to control access.



## Project Features
* Client-server architecture using Python sockets
* User authentication (Login / Signup system)
* Role-based access control (Student / Educator)
* Encrypted document transfer (secure communication)
* Interactive quizzes for learning reinforcement
* Activity logging system
* Educator dashboard (add/delete quiz questions, view grades)
* Student dashboard (view documents, take quizzes, view grades)



## Tools & Technologies
* Python 3.x
* Socket Programming (socket library)
* File Handling
* Encryption & Decryption (symmetric encryption)
* Data Structures (lists & dictionaries)
* VS Code 
* Kali Linux


# System Architecture

#### Server Side
* Stores encrypted documents
* Manages user database (files/dictionaries)
* Handles authentication
* Sends documents securely to authenticated users
* Maintains quiz database and logs

#### Client Side
* Allows user login/signup
* Sends requests to server
* Receives decrypted documents
* Takes quizzes and receives feedback



# Project Workflow 

### 1. System Startup
   
   <img width="495" height="89" alt="Screenshot 2026-06-23 at 1 01 02 PM" src="https://github.com/user-attachments/assets/2a0b8dbf-303a-4d71-b915-d0562f41bdd0" />


### 2. User Registration (3 Students)


   <img width="962" height="182" alt="image" src="https://github.com/user-attachments/assets/dc23896c-918c-48f6-b879-3a5f93e3f5be" />


   <img width="886" height="220" alt="image" src="https://github.com/user-attachments/assets/07019ac0-7e4b-4596-ba9a-430b6db8252a" />


   <img width="818" height="212" alt="image" src="https://github.com/user-attachments/assets/fd2ea06a-f380-4b6e-a27d-0791abdfbece" />


### 3. Student Accessing Civil War Document

  <img width="818" height="458" alt="image" src="https://github.com/user-attachments/assets/bf7b8e25-02a6-4b36-9877-ecf37af5c92f" />



### 4. Student Taking Quiz

  <img width="1044" height="562" alt="image" src="https://github.com/user-attachments/assets/92ca252e-b976-454f-8472-739681c4eb86" />


### 5. Educator Dashboard – Manage Questions
  
* Deleting question


  <img width="2638" height="1758" alt="image" src="https://github.com/user-attachments/assets/dcd79f6b-1f8a-42e2-a944-78d7fa181ec3" />



* Adding quiz question

   <img width="2638" height="908" alt="image" src="https://github.com/user-attachments/assets/d431682e-fea4-44ca-829a-2bb98553756f" />



### 8. Viewing Student Grades


  <img width="1952" height="594" alt="image" src="https://github.com/user-attachments/assets/98f64da6-e5f8-41a5-8fa9-12adfe36f38b" />



## Security Implementation

The system encrypts all transmitted documents between client and server to ensure confidentiality. Only authenticated users can access sensitive historical data. Role-based permissions ensure students and educators have different levels of access.


## Conclusion

This project demonstrates the practical application of socket programming, encryption, and authentication in a real-world educational system. It simulates a secure learning environment where historical data is protected while still being accessible to authorized users.






# Lessons Learned

Through this project, I learned how client-server systems communicate using sockets and how data can be securely transmitted using encryption techniques. I also gained experience implementing authentication systems, managing user roles, and structuring a full Python application using functions, loops, dictionaries, and file handling. Most importantly, I understood how cybersecurity principles such as confidentiality, integrity, and access control can be applied in real-world educational systems.
