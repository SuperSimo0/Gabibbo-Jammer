import random
import socket
import sys

logo = '''

░██████╗░░█████╗░██████╗░██╗██████╗░██████╗░░█████╗░
██╔════╝░██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗
██║░░██╗░███████║██████╦╝██║██████╦╝██████╦╝██║░░██║
██║░░╚██╗██╔══██║██╔══██╗██║██╔══██╗██╔══██╗██║░░██║
╚██████╔╝██║░░██║██████╦╝██║██████╦╝██████╦╝╚█████╔╝
░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░

░░░░░██╗░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
░░░░░██║██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
░░░░░██║███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
██╗░░██║██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝

                                


                                                 ███████████████████                                                                                                     
                                           ██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████                                                                                             
                                       ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                                                                                         
                                   ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                      ██████  ██████  ██     ██████  ██████  ██  ██  ██                
                                 ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                    ██      ██  ██  ██     ██  ██  ██      ██  ██  ██                
                               ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓██                  ██████  ██████  ██     ██████  ██████  ██████  ██                
                             ██▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████▓▓▓▓▓▓▓▓▓▓██                    ██  ██      ██     ██  ██      ██  ██  ██                    
                           ████▓▓▓▓▓▓▓▓▓▓██████████▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████▓▓▓▓▓▓▓▓████              ██████  ██      ██████ ██  ██  ██████  ██  ██  ██                
                           ██▓▓▓▓▓▓▓▓▓▓▓▓██████████▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓██                                                                               
                         ██▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██                                                                             
                       ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██                                                                           
                     ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                                         
                   ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                                         
                   ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      ██▓▓▓▓▓▓▓▓▓▓▓▓▓██          ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███                                                                       
                 ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          ██▓▓▓▓▓▓▓▓▓██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███                                                                     
                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██              ██▓▓▓▓▓▓▓██                ██▓▓▓▓▓▓▓▓▓▓▓▓▓███                                                                     
                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██              ██▓▓▓▓▓▓▓██                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                                    
              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    ██████    ██▓▓▓▓▓▓▓██    ██████      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                                    
            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    ██████    ██▓▓▓▓▓▓▓██    ██████      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                                  
            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    ██████    ██▓▓▓▓▓▓▓██    ██████      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                                  
          ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██              ██▓▓▓▓▓▓▓██                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                                
          ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██              ██▓▓▓▓▓▓▓██                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                                
        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            ██▓▓▓▓▓▓▓██                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                              
        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            ██▓▓▓▓▓▓▓██▒▒            ▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                              
        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            ██▓▓▓▓▓▓▓▓▓██            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                              
        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        ██▓▓▓▓▓▓▓▓▓▓▓▓▓██        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                            
        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                            
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                            
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                          
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                          
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                          
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                        
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                        
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                        
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                        
      ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                          
      ██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██         
        ██▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████        
        ██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████                                                        
          ██▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓██████    
            ██▓▓███████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓██▓▓▓▓██  
              ██▓▓▓████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████▓▓▓▓██▓▓▓▓▓▓██       
            ██▓▓██▓▓▓██████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████▓▓▓██▓▓▓▓▓▓▓▓▓▓██      
          ██▓▓▓▓▓███▓▓▓▓▓█████████████████████████████████████████████████████████████████████████▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██          
          ██▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓███████████████████████████████████████████████████████████████▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██             
        ██▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓███████████████████████████████████████████████████▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                  
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████████████████████████████▓▓▓▓▓▓▓▓███▓ ▒██▓▓▓▓▓▓▓▓▓▓▓▓▓██               
    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓█████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████     ▒██▓▓▓▓▓▓▓▓▓▓▓██                 
    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██▒▒▒▒▒▒████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████▒▒██       ▓███▓▓▓▓▓▓██                 
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒██           ██▓▓▓▓██                 
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▓█▓▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██               ██▓▓██             
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒████████▒▓█▓▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██                 ██               
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  ██▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒████                   ██             
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███   ██▓▓▓▓▓▓▓▓██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒██  ██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██    ██           ░░    ██              
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓████ ████▓▓▓▓▓▓▓▓██▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒██  ▓▓▓▓▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓    ▓▓▒▒         ░░  ▒▒██             
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓███   ██▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒██    ██▒▒▒▒▒▒▒▒▒▒████        ██             ██               
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓███   ██▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒██      ██▒▒██████            ███▓         ██                
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓███ ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██          ██                  ██▓████░   ██       
  ██▓▓▓▓██████▓▓▓███ ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▒▒▒▒▒▒▒▒▒▒▒▒▒██    ░░                        ██▓███ ████        
  ██████      ████   ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  ██████▒▒▒▒▒▓█░                               ██▓▓▓███            
██               ░██ ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        ██▒▒▒▓█░                                 ██▓███    
██               ░██ ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        ███▒           ░░                      ██▓███ 

⠀⠀                                                                                                                              
'''

# Pool di curiosità sul Gabibbo
gabibbo_curiosities = [
    "Il primo Gabibbo è stato Gero Caldarelli, che lo ha animato fin dal 1990, anno della nascita del personaggio",
    "Il Gabibbo è alto 1.65m",
    "Il Gabibbo non è solo la mascotte di Striscia la Notizia, ma anche di vari altri progammi Mediaset, come Paperissima Sprint e Cultura Moderna",
    "Il Gabibbo è un cantante e personaggio televisivo italiano ideato da Antonio Ricci",
    "Il Gabibbo NON è un furry",
    "Il Gabibbo appare per la prima volta il 1 Ottobre 1990 a Striscia la Notizia",
    "E' esistito un programma condotto dal Gabibbo, intitolato 'Mondo Gabibbo'",
    "Il Gabibbo è un grande Besugo",
    "Il Gabibbo canta ed anima i balli di diverse canzoni, come 'My name is Gabibbo', 'Ti Spacco la Faccia' ed il celebre 'Fritto Misto'",
    "Attorno al Gabibbo si è creato un vero e proprio mercato, con oggetti per la scuola, gioielli, costumi di carnevale ed addirittura coperte e pigiami.",
    "Il Gabibbo è l'unico pupazzo ad aver vinto il Telegatto, nel 1991.",
    "Il Gabibbo ha pubblicato 3 album: 'My Name Is Gabibbo', 'Un Attimino' e 'Fu Fu Dance'",
    "Il Gabibbo ha pubblicato 2 singoli: 'Ti Spacco la Faccia' e 'Ma sei scemo!?'",
    "Il termine 'Gabibbo' è una parola Genovese, titolo che i marinai di Genova erano soliti dare agli scaricatori di porto",
    "Il Gabibbo non ha orecchie, in quanto ha sempre la verità in tasca e non ha mai dubbi",
    "Il Gabibbo è stato ribattezzato dal cast di Striscia come 'Vendicatore Rosso', in quanto giustiziere",
    "Il Gabibbo è il terzo pupazzo in attività più longevo della TV Italiana",
    "Nel 1992 il Gabibbo ha preso 15 voti nelle elezioni per il Presidente della Repubblica",
    "Nel 1997 venne fondato il P.d.G. (Partito del Gabibbo)",
    "All'inizio degli anni 90, in alcuni programmi Mediaset, è apparsa in alcune occasioni la Gabibba, moglie del Gabibbo",
    "Il Gabibbo è apparso per ben tre volte al cinema, prendendo parte a vari film",
    "Nella sua carriera, il Gabibbo ha presentato ben 16 programmi TV",
    "Nel 18 Giugno 2014 il Gabibbo è apparso in TV completamente in nero, per vestire i panni del calciatore Mario Balotelli",
    "Il Telegatto vinto dal Gabibbo è ora conservato nel museo di Striscia",
    "Il Gabibbo ha partecipato in diversi TikTok creati da Striscia",
    "E sotto l'onda, profonda, Insieme io e te, Che bello i pesci Stare a guardare",
    "Che baraonda, gioconda, Pepperrepeppè, È il pesce tromba che sta a suonare",
    "Seppie e acciughe con te (ballano), Scampi e orate con me (saltano, danzano)",
    "I besughi, come il Gabibbo, sono quei tipi di pesci che fanno parte della famiglia dei pagari, come ad esempio l’occhialone.",
    "La parola 'Besugo' vuol dire anche sciocco/credulone, in quanto questa tipologia di pesci abboccano con grande facilità",
    "L'espressione 'Belandi', spesso usata dal Gabibbo, è un'espressione principalmente usata in Liguria, con lo stesso significato di 'diamine'",
    "Il Gabibbo è nato l'1/10/1990",
    "Il Gabibbo pesa 73kg",
    "Il numero di scarpe del Gabibbo è 83",
    "Il Gabibbo, durante il suo percorso con Striscia la Notizia, ha registrato quasi 900 servizi diversi, in tutt'Italia",
    "Il Gabibbo è un pupazzo rosso che parla in dialetto genovese e che da sempre anima le sigle di Striscia la notizia, cantate in coda al programma.",
    "Durante gli anni novanta, era attivo un numero verde, S.O.S. Gabibbo, in cui i cittadini potevano segnalare facilmente ingiustizie.",
    "Il Gabibbo è il membro più longevo del cast attuale di Striscia la Notizia",
    "Il primo Tapiro d'Oro è stato consegnato nel 1996 dal Gabibbo",
    "Il Gabibbo ha compiuto 30 anni nel 1° Ottobre 2020",
    "Secondo il 'Codice di Striscia', pubblicato nel 1998, all'interno del programma si deve evitare la retorica e l'indignazione (treanne quella parodistica), dunque frasi come 'E' una vergogna' può dirle solo il Gabibbo, in quanto un pupazzo",
    "Il primo 'attapirato' della storia fu il giudice Alberto Cardino, consegnato dal Gabibbo nel 27 Novembre 1996"
]

def generate_random_text():
    random_curiosity = random.choice(gabibbo_curiosities)
    return random_curiosity

def send_traffic(ip_address, ports):
    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                curiosity = generate_random_text()
                sock.sendall(curiosity.encode())
                sock.close()
                print(f"Curiosità mandata a {ip_address}:{port}")
            else:
                print(f"Impossibile stabilire una connessione a {ip_address}:{port}")
    except socket.error as e:
        print(f"Errore: {e}")

def main():
    print(logo)
    print("Benvenuto in Gabibbo-Jammer!")
    cidr = input("Inserisci il CIDR di gara (es. 10.60.0.0/16): ")
    service_ports = input("Inserisci le porte dei servizi separate da virgola: ")
    service_ports = [int(port) for port in service_ports.split(",")]
    numero_quadre = input("Inserisci il numero di squadre partecipanti: ")

    # Ottiene i primi due ottetti dell'indirizzo di rete
    network_address, subnet_mask = cidr.split('/')
    network_address = network_address.strip()
    subnet_mask = int(subnet_mask.strip())
    network_prefix = ".".join(network_address.split(".")[:2])

    tempo_massimo = len(service_ports)*int(numero_quadre)
    print(f"Con i dati inseriti è stimato un tempo massimo di {massimo} secondi per completare un giro. \n")
    scelta = input("Desideri proseguire? (si/no): ")
    if scelta.lower() == "si":
        print("E sotto l'onda, profonda, Insieme io e te, Che bello i pesci Stare a guardare...")
    else:
        print("Chiusura di Gabibbo-Jammer.")
        sys.exit()


    while True:
        # Cicla sui terzi ottetti da 1 a numero_quadre
        for i in range(1, int(numero_quadre)+1):
            # Costruisce l'indirizzo IP con i primi due ottetti fissi e il terzo ottetto variabile
            ip_address = f"{network_prefix}.{i}.1"
            send_traffic(ip_address, service_ports)

if __name__ == '__main__':
    main()
